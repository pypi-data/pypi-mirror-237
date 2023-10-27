"""NbData, Sets of Netbox objects, like aggregates, prefixes, etc., are joined together."""

from __future__ import annotations

from copy import deepcopy
from datetime import datetime

from vpnetbox import init, NbParser
from vpnetbox.types_ import LDAny, ODatetime, DiDAny

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


class NbData:
    """NbData, Sets of Netbox objects, like aggregates, prefixes, etc., are joined together."""

    _data_attrs = [
        # ipam
        "addresses",
        "aggregates",
        "prefixes",
        "vlans",
        # dcim
        "devices",
        "sites",
        # circuits
        "circuit_types",
        "circuits",
        "providers",
        "terminations",
        # tenancy
        "tenants",
    ]
    _helper_attrs = [
        "name",
        "version",
        "last_update",
    ]

    def __init__(self, **kwargs):
        """Init NbData.

        ipam
        :param aggregates: List of Netbox ipam/aggregates objects.
        :param prefixes: List of Netbox ipam/prefixes objects.
        :param addresses: List of Netbox ipam/addresses objects.
        :param vlans: List of Netbox ipam/vlans objects.

        dcim
        :param sites: List of Netbox dcim/sites objects.
        :param devices: List of Netbox dcim/devices objects.

        circuits
        :param circuit_types: List of Netbox circuits/circuit_types objects.
        :param circuits: List of Netbox circuits/circuits objects.
        :param providers: List of Netbox circuits/providers objects.
        :param terminations: List of Netbox circuits/circuit-terminations objects.

        tenancy
        :param tenants: List of Netbox tenancy/tenants objects.

        Other
        :param version: Netbox version.
        :param last_update: Last requested datetime (data age).
        """
        self.name = self._init_name(**kwargs)
        self.version: str = str(kwargs.get("version") or "0")
        self.last_update: ODatetime = _init_last_update(**kwargs)

        # LISTS
        # ipam
        self.addresses: LDAny = list(kwargs.get("addresses") or [])
        self.aggregates: LDAny = list(kwargs.get("aggregates") or [])
        self.prefixes: LDAny = list(kwargs.get("prefixes") or [])
        self.vlans: LDAny = list(kwargs.get("vlans") or [])
        # dcim
        self.devices: LDAny = list(kwargs.get("devices") or [])
        self.sites: LDAny = list(kwargs.get("sites") or [])
        # circuits
        self.circuit_types: LDAny = list(kwargs.get("circuit_types") or [])
        self.circuits: LDAny = list(kwargs.get("circuits") or [])
        self.providers: LDAny = list(kwargs.get("providers") or [])
        self.terminations: LDAny = list(kwargs.get("terminations") or [])
        # tenancy
        self.tenants: LDAny = list(kwargs.get("tenants") or [])

        # RECURSIONS
        # ipam
        self.addresses_d: DiDAny = {}
        self.aggregates_d: DiDAny = {}
        self.prefixes_d: DiDAny = {}
        self.vlans_d: DiDAny = {}
        # dcim
        self.devices_d: DiDAny = {}
        self.sites_d: DiDAny = {}
        # circuits
        self.circuit_types_d: DiDAny = {}
        self.circuits_d: DiDAny = {}
        self.providers_d: DiDAny = {}
        self.terminations_d: DiDAny = {}
        # tenancy
        self.tenants_d: DiDAny = {}

    def __repr__(self) -> str:
        """__repr__."""
        params = init.repr_params(
            # ipam
            addr=len(self.addresses),
            aggr=len(self.aggregates),
            pref=len(self.prefixes),
            vlan=len(self.vlans),
            # dcim
            dev=len(self.devices),
            site=len(self.sites),
            # circuits
            ctyp=len(self.circuit_types),
            cid=len(self.circuits),
            prov=len(self.providers),
            ter=len(self.terminations),
            # tenancy
            ten=len(self.tenants),
        )
        return f"<{self.name}: {params}>"

    # ============================= init =============================

    def _init_name(self, **kwargs) -> str:
        """Init name."""
        host = str(kwargs.get("host") or "")
        items = [self.__class__.__name__, host]
        items = [s for s in items if s]
        return " ".join(items)

    def init_dicts(self) -> None:
        """Convert a list of Netbox objects into a dictionary where the key is the object ID.

        :return: None. Update self object.
        """
        for attr in self._data_attrs:
            items = getattr(self, attr)
            if not isinstance(items, list):
                raise TypeError(f"{attr} {list} expected")
            items_: LDAny = deepcopy(items)
            data = {int(d["id"]): d for d in items_}
            id_ = 0
            if data.get(id_):
                raise ValueError(f"{attr} object with {id_=} is unexpected")
            data[0] = {}
            setattr(self, f"{attr}_d", data)

    def init_recursions(self) -> None:
        """Init the Netbox object recursions.

        Convert Netbox data lists to dict, where key is unique id.
        Create recursive links between objects.
        :return: None. Update self object.
        """
        # ipam
        self._join_addresses()
        self._join_aggregates()
        self._join_prefixes()
        self._join_vlans()
        # dcim
        self._join_devices()
        self._join_sites()
        # circuits
        self._join_circuits()
        self._join_terminations()
        # tenancy
        self._join_tenants()

    def _join_addresses(self):
        """Join addresses.

        # todo
        tenant
        assigned_object
        """

    def _join_aggregates(self):
        """Join aggregates.

        # todo
        rir
        """

    def _join_prefixes(self):
        """Join prefixes.

        # todo
        tenant
        role
        """

    def _join_vlans(self):
        """Join vlans.

        # todo
        site
        group
        tenant
        role
        """

    def _join_devices(self):
        """Join devices: tenant, site.

        # todo
        device_type
        device_role
        platform

        location
        rack
        virtual_chassis
        """
        for device_d in self.devices_d.values():
            if not device_d:
                continue
            parser = NbParser(device_d)
            # tenant
            id_ = parser.get_int("tenant", "id")
            if tenant_d := self.tenants_d.get(id_) or {}:
                device_d["tenant"] = tenant_d
            # site
            id_ = parser.get_int("site", "id")
            if site_d := self.sites_d.get(id_) or {}:
                device_d["site"] = site_d

    def _join_sites(self):
        """Join sites.

        # todo
        region
        tenant
        asns
        """

    def _join_circuits(self):
        """Join circuits: provider, type, tenant, termination_a, termination_z."""
        for circuit_d in self.circuits_d.values():
            if not circuit_d:
                continue
            parser = NbParser(circuit_d)
            # provider
            id_ = parser.get_int("provider", "id")
            if provider_d := self.providers_d.get(id_) or {}:
                circuit_d["provider"] = provider_d
            # type
            id_ = parser.get_int("type", "id")
            if type_d := self.circuit_types_d.get(id_) or {}:
                circuit_d["type"] = type_d
            # tenant
            id_ = parser.get_int("tenant", "id")
            if tenant_d := self.tenants_d.get(id_) or {}:
                circuit_d["tenant"] = tenant_d
            # termination_a
            id_ = parser.get_int("termination_a", "id")
            if term_d := self.terminations_d.get(id_) or {}:
                circuit_d["termination_a"] = term_d
                term_d["circuit"] = circuit_d
            # termination_z
            id_ = parser.get_int("termination_z", "id")
            if term_d := self.terminations_d.get(id_) or {}:
                circuit_d["termination_z"] = term_d
                term_d["circuit"] = circuit_d

    def _join_terminations(self) -> None:
        """Join circuit-terminations: circuit, site, link_peers (devices).

        # todo
        cable
        """
        for term_d in self.terminations_d.values():
            if not term_d:
                continue
            parser = NbParser(term_d)
            # circuit
            id_: int = parser.get_int("circuit", "id")
            if circuit_d := self.circuits_d.get(id_) or {}:
                term_d["circuit"] = circuit_d
                if term_d["term_side"] == "A":
                    circuit_d["termination_a"] = term_d
                elif term_d["term_side"] == "Z":
                    circuit_d["termination_z"] = term_d
            # site
            id_ = parser.get_int("site", "id")
            if site_d := self.sites_d.get(id_) or {}:
                term_d["site"] = site_d
            # link_peers (devices)
            link_peers: LDAny = parser.get_list("link_peers")  # interfaces
            for interface_d in link_peers:
                parser_ = NbParser(interface_d)
                id_ = parser_.get_int("device", "id")
                if device_d := self.devices_d.get(id_) or {}:
                    interface_d["device"] = device_d

    def _join_tenants(self) -> None:
        """Join tenants.

        # todo
        group
        """

    # =========================== method =============================

    def copy(self) -> NbData:
        """Return copy of self (deepcopy)."""
        nb_data = NbData()
        nb_data.version = self.version
        for attr in self._data_attrs:
            setattr(nb_data, attr, deepcopy(getattr(self, attr)))
        return nb_data

    def clear(self) -> None:
        """Clear NbData."""
        self.version = "0"
        for attr in self._data_attrs:
            setattr(self, attr, [])

    def is_empty(self) -> bool:
        """Return True if NbData is empty (has no any data)."""
        return not any(getattr(self, s) for s in self._data_attrs)


# ============================= helpers ==============================

def _init_last_update(**kwargs) -> ODatetime:
    """Init time when data was requested last time.

    :return: Last updated datetime or None.
    """
    value = kwargs.get("last_updated")
    if isinstance(value, datetime):
        return value
    if isinstance(value, str):
        return datetime.strptime(value, DATE_FORMAT)
    if isinstance(value, int):
        return datetime.fromtimestamp(value)
    return None
