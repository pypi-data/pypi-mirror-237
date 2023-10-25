"""NbData, Sets of Netbox objects, like aggregates, prefixes, etc., are joined together."""

from __future__ import annotations

from copy import deepcopy
from datetime import datetime

from packaging.version import Version

from vpnetbox import init
from vpnetbox.types_ import LDAny, ODatetime, DiDAny

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


class NbData:
    """NbData, Sets of Netbox objects, like aggregates, prefixes, etc., are joined together."""

    _cache_attrs = [
        "aggregates",
        "prefixes",
        "addresses",
        "vlans",
        "sites",
        "devices",
        "circuits",
        "terminations",
        "last_update",
    ]

    def __init__(self, **kwargs):
        """Init NbData.

        ipam
        :param aggregates: List of Netbox aggregates data.
        :param prefixes: List of Netbox prefixes data.
        :param addresses: List of Netbox addresses data.
        :param vlans: List of Netbox vlans data.

        dcim
        :param sites: List of Netbox sites data.
        :param devices: List of Netbox devices data.

        circuits
        :param circuits: List of Netbox circuits data.
        :param terminations: List of Netbox terminations data.

        Other
        :param version: Netbox version.
        :param last_update:  Last requested datetime (data age).
        """
        self.name = self._init_name(**kwargs)
        self.version: Version = self._init_version(**kwargs)
        self.last_update: ODatetime = self._init_last_update(**kwargs)

        # LISTS
        # ipam
        self.addresses: LDAny = kwargs.get("addresses") or []
        self.aggregates: LDAny = kwargs.get("aggregates") or []
        self.prefixes: LDAny = kwargs.get("prefixes") or []
        self.vlans: LDAny = kwargs.get("vlans") or []
        # dcim
        self.devices: LDAny = kwargs.get("devices") or []
        self.sites: LDAny = kwargs.get("sites") or []
        # circuits
        self.circuits: LDAny = kwargs.get("circuits") or []
        self.terminations: LDAny = kwargs.get("terminations") or []

        # RECURSIONS
        # ipam
        self.addresses_d: DiDAny = {d["id"]: d for d in self.addresses}
        self.aggregates_d: DiDAny = {d["id"]: d for d in self.aggregates}
        self.prefixes_d: DiDAny = {d["id"]: d for d in self.prefixes}
        self.vlans_d: DiDAny = {d["id"]: d for d in self.vlans}
        # dcim
        self.devices_d: DiDAny = {d["id"]: d for d in self.devices}
        self.sites_d: DiDAny = {d["id"]: d for d in self.sites}
        # circuits
        self.circuits_d: DiDAny = {d["id"]: d for d in self.circuits}
        self.terminations_d: DiDAny = {d["id"]: d for d in self.terminations}

    def __repr__(self) -> str:
        """__repr__."""
        params = init.repr_params(
            aggr=len(self.aggregates),
            pref=len(self.prefixes),
            addr=len(self.addresses),
            vlan=len(self.vlans),
            site=len(self.sites),
            dev=len(self.devices),
            cid=len(self.circuits),
            ter=len(self.terminations),
        )
        return f"<{self.name}: {params}>"

    # ============================= init =============================

    @staticmethod
    def _init_last_update(**kwargs) -> ODatetime:
        """Init time when data was requested last time."""
        value = kwargs.get("last_updated")
        if isinstance(value, datetime):
            return value
        if isinstance(value, str):
            return datetime.strptime(value, DATE_FORMAT)
        if isinstance(value, int):
            return datetime.fromtimestamp(value)
        return None

    def _init_name(self, **kwargs) -> str:
        """Init name."""
        host = str(kwargs.get("host") or "")
        return " ".join([s for s in (self.__class__.__name__, host) if s])

    @staticmethod
    def _init_version(**kwargs) -> Version:
        """Init version."""
        version = kwargs.get("version") or "0"
        if isinstance(version, Version):
            return version
        return Version(str(version))

    def init_recursive_data(self) -> None:
        """Init the dictionaries of Netbox objects.

        Convert Netbox data lists to dict, where key is unique id.
        Create recursive links between objects.
        :return: None. Create dictionaries of Netbox objects with recursive links.
        """
        for attr in self._cache_attrs:
            items = getattr(self, attr)
            if not isinstance(items, list):
                continue
            items: LDAny = deepcopy(items)
            items_d: DiDAny = {int(d["id"]): d for d in items}
            items_d[0] = {}  # dummy
            setattr(self, f"{attr}_d", items_d)

        self._join_circuit_terminations()

    def _join_circuit_terminations(self) -> None:
        """Join circuit-terminations."""
        for term_d in self.terminations_d.values():
            circuit_id = int(dict(term_d.get("circuit") or {}).get("id") or 0)
            term_d["circuit"] = self.circuits_d[circuit_id]

            id_ = int(dict(term_d.get("site") or {}).get("id") or 0)
            term_d["site"] = self.sites_d[id_]

            link_peers = list(term_d.get("link_peers") or [])  # interfaces
            for link_peer in link_peers:
                id_ = int(dict(link_peer.get("device") or {}).get("id") or 0)
                link_peer["device"] = self.devices_d[id_]

        for circuit_d in self.circuits_d.values():
            id_ = int(dict(circuit_d.get("termination_a") or {}).get("id") or 0)
            circuit_d["termination_a"] = self.terminations_d[id_]
            id_ = int(dict(circuit_d.get("termination_z") or {}).get("id") or 0)
            circuit_d["termination_z"] = self.terminations_d[id_]

    # =========================== method =============================

    def copy(self) -> NbData:
        """Return copy of self (deepcopy)."""
        nb_data = NbData()
        nb_data.version = Version(self.version.public)
        for attr in self._cache_attrs:
            setattr(nb_data, attr, deepcopy(getattr(self, attr)))
        return nb_data

    def clear(self) -> None:
        """Clear NbData."""
        self.version = Version("0")
        for attr in self._cache_attrs:
            setattr(self, attr, [])

    def is_empty(self) -> bool:
        """Return True if NbData is empty (has no any data)."""
        return not any(getattr(self, s) for s in self._cache_attrs)
