"""NbHandler.

Retrieves and caches a bulk of data from the Netbox to local system.
Collects sets of aggregates, prefixes, addresses, devices, sites data from Netbox
and saves it in NbData object.
"""

from __future__ import annotations

import copy
import logging

from vpnetbox.api.nb_api import NbApi
from vpnetbox.api.nb_parser import NbParser
from vpnetbox.cache import Cache, make_path
from vpnetbox.messages import Messages
from vpnetbox.nbh.nb_data import NbData
from vpnetbox.types_ import LStr, DAny


class NbHandler(Cache):
    """Retrieves and caches a bulk of data from the Netbox to local system.

    Collects sets of aggregates, prefixes, addresses, devices, sites data from Netbox
    and saves it in NbData object.
    """

    def __init__(self, **kwargs):
        """Init NbHandler.

        Parameters for NbApi are described in the NbApi class in ../api/nb_api.py.
        Parameters for NbData are described in the NbData class in ./nb_data.py.
        Parameters for Cache are described in the Cache class in ../cache.py.
        """
        cache_params = self._init_cache_params(**kwargs)
        Cache.__init__(self, **cache_params)
        self.api = NbApi(**kwargs)
        self.nbd = NbData(**kwargs)
        self.msgs = Messages(name=self.api.host)

    def __repr__(self) -> str:
        """__repr__."""
        return self.nbd.__repr__().replace(self.nbd.name, self.name)

    def __copy__(self) -> NbHandler:
        """Copy NbApi object and all data in NbData object.

        :return: Copy of NbHandler object.
        """
        names = getattr(self.api.addresses, "_init_params")
        params = {s: getattr(self.api.addresses, s) for s in names}
        nb_handler = NbHandler(**params)
        nb_handler.nbd = self.nbd.copy()
        return nb_handler

    # ============================= init =============================

    def _init_cache_params(self, **kwargs) -> DAny:
        """Init params for Cache."""
        path: str = make_path(**kwargs, **{"name": self.__class__.__name__})
        params = {"cache_path": path, "cache_attrs": ["data"]}
        return params

    # ========================== scenarios ===========================

    def get_addresses(self, **kwargs) -> None:
        """Get Netbox ipam/addresses objects by using the finding parameters in kwargs.

        :param kwargs: Finding parameters are described in the Addresses object.
        :return: None. Update self object.
        """
        self.nbd.addresses = self.api.addresses.get(**kwargs)

    def get_aggregates(self, **kwargs) -> None:
        """Get Netbox ipam/aggregates objects by using the finding parameters in kwargs.

        :param kwargs: Finding parameters are described in the Aggregates object.
        :return: None. Update self object.
        """
        self.nbd.aggregates = self.api.aggregates.get(**kwargs)

    def get_circuits(self, **kwargs) -> None:
        """Get Netbox circuits/circuits objects by using the finding parameters in kwargs.

        :param kwargs: Finding parameters are described in the Circuits object.
        :return: None. Update self object.
        """
        self.nbd.circuits = self.api.circuits.get(**kwargs)

    def get_devices(self, **kwargs) -> None:
        """Get Netbox dcim/devices objects by using the finding parameters in kwargs.

        :param kwargs: Finding parameters are described in the Devices object.
        :return: None. Update self object.
        """
        self.nbd.devices = self.api.devices.get(**kwargs)

    def get_prefixes(self, **kwargs) -> None:
        """Get Netbox ipam/prefixes objects by using the finding parameters in kwargs.

        :param kwargs: Finding parameters are described in the Prefixes object.
        :return: None. Update self object.
        """
        self.nbd.prefixes = self.api.prefixes.get(**kwargs)

    def get_vlans(self, **kwargs) -> None:
        """Get Netbox ipam/vlans objects by using the finding parameters in kwargs.

        :param kwargs: Finding parameters are described in the Vlans object.
        :return: None. Update self object.
        """
        self.nbd.vlans = self.api.vlans.get(**kwargs)

    def get_sites(self, **kwargs) -> None:
        """Get Netbox dcim/sites objects by using the finding parameters in kwargs.

        :param kwargs: Finding parameters are described in the Sites object.
        :return: None. Update self object.
        """
        self.nbd.sites = self.api.sites.get(**kwargs)

    def get_terminations(self, **kwargs) -> None:
        """Get Netbox circuits/terminations objects by using the finding parameters in kwargs.

        :param kwargs: Finding parameters are described in the Terminations object.
        :return: None. Update self object.
        """
        self.nbd.terminations = self.api.terminations.get(**kwargs)

    def scenario__demo(self) -> None:
        """Get minimum of aggregates/prefixes/addresses/devices for this tool demonstration.

        :return: None. Update self object.
        """
        aggregates = ["10.10.0.0/16", "10.31.64.0/18"]
        prefixes = ["10.10.0.0/24", "10.10.119.0/26", "10.31.65.0/26", "10.31.67.0/26"]
        addresses = ["10.10.0.1/24", "10.10.119.1/26", "10.31.65.18/26", "10.31.67.17/26"]
        devices = ["device1", "device2"]
        self.api.default_active()
        self.nbd.version = self.api.version()
        self.get_aggregates(prefix=aggregates)
        self.get_prefixes(prefix=prefixes)
        self.get_addresses(address=addresses)
        self.get_devices(name=devices)
        logging.debug("%s data loaded.", f"{self!r}")

    # =========================== method =============================

    def clear(self) -> None:
        """Delete all data in NbData.

        :return: None. Update self object.
        """
        self.nbd.clear()

    def copy(self) -> NbHandler:
        """Copy NbApi object and all data in NbData object.

        :return: Copy of NbHandler object.
        """
        return copy.copy(self)

    def is_empty(self) -> bool:
        """Check if all NbData data attributes are empty.

        :return: True if NbData is empty, otherwise Else.
        """
        return self.nbd.is_empty()

    # noinspection PyProtectedMember
    def print_warnings(self) -> None:
        """Print WARNINGS if found some errors/warnings in data processing."""
        data_attrs = self.nbd._cache_attrs  # pylint: disable=protected-access
        data_lists = [getattr(self.nbd, s) for s in data_attrs]
        for datas in data_lists:
            for data in datas:
                if warnings := data.get("warnings") or []:
                    for msg in warnings:
                        logging.warning(msg)

    # =========================== data methods ===========================

    def devices_primary_ip4(self) -> LStr:
        """Return the primary IPv4 addresses of Netbox devices with these settings.

        :return: primary_ip4 addresses of devices.
        """
        parsers = [NbParser(data=d) for d in self.nbd.devices]
        ip4s: LStr = sorted({o.device_primary_ip4() for o in parsers})
        ip4s = [s for s in ip4s if s]
        return ip4s

    def set_addresses_mask_32(self) -> None:
        """Change mask to /32 for all Netbox addresses.

        :return: None. Update self object.
        """
        for nb_addr in self.nbd.addresses:
            address = nb_addr["address"]
            nb_addr["address"] = address.split("/")[0] + "/32"
