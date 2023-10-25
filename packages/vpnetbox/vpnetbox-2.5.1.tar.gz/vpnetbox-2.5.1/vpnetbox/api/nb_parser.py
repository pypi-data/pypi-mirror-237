"""NbParser, Extracts a value from a Netbox object using a long chain of keys."""
import re
import string
from typing import Type

from packaging.version import Version
from vhelpers import vre

from vpnetbox.api.exceptions import NbParserError
from vpnetbox.types_ import DAny, SStr, LStr, T2Str

RE_PREFIX = r"\d+\.\d+\.\d+\.\d+/\d+"


class NbParser:
    """NbParser, Extracts a value from a Netbox object using a long chain of keys."""

    def __init__(self, data: DAny = None, strict: bool = False, **kwargs):
        """Init NbParser.

        :param data: Netbox object.
        :param strict: True - Raise ERROR if data is invalid,
                       False - Return empty data if self.data is invalid.
        :param kwargs:
            version: Netbox version. Helpful for compatibility with Netboxes of different versions.
            type: str
        """
        self.data = data or {}
        self.strict = strict
        self.version: Version = _init_version(**kwargs)

    # =========================== method =============================

    def address(self) -> str:
        """ipam/ip-addresses/address.

        :raises: NbParserError - if the address does not match the naming convention x.x.x.x/x
            and self.strict=True.
        """
        address = self.get_str(keys=["address"], data=self.data)
        if self.strict:
            if not self.is_prefix(subnet=address):
                raise NbParserError(f"invalid {address=}")
        return address

    def aggr_cf_super_aggr(self) -> T2Str:
        """ipam/aggregates/custom_fields/super_aggregate/value."""
        keys = ["custom_fields", "super_aggregate"]
        cf_value = self.get_str(keys=keys, data=self.data).strip()
        prefix, descr = vre.find2(f"^({RE_PREFIX})(.*)", cf_value)
        descr = descr.strip()
        return prefix, descr

    def assigned_object__device_name(self) -> str:
        """ipam/ip-addresses/assigned_object/device/name."""
        return self.get_str(keys=["assigned_object", "device", "name"], data=self.data)

    def cf_end_of_support(self) -> str:
        """dcim/devices/custom_fields/end_of_support/value.

        dcim/device_types/custom_fields/end_of_support/value.
        """
        keys = ["custom_fields", "end_of_support"]
        cf_value = self.get_str(keys=keys, data=self.data).strip()
        return cf_value

    def cloud_account(self) -> str:
        """ipam/aggregates/custom_fields/cloud_account/label."""
        keys = ["custom_fields", "cloud_account"]
        return self.get_str(keys=keys, data=self.data)

    def env(self) -> str:
        """ipam/prefixes/custom_fields/env/label."""
        keys = ["custom_fields", "env"]
        return self.get_str(keys=keys, data=self.data)

    def id_(self) -> int:
        """ipam/prefixes/id."""
        return self.get_int(keys=["id"])

    def name(self) -> str:
        """dcim/devices/name.

        dcim/vlans/name.
        :raises: NbParserError - if device has no name and self.strict=True.
        """
        name = self.get_str(keys=["name"], data=self.data)
        if not name and self.strict:
            raise NbParserError(f"absent name in {self.data=}")
        return name

    def overlapped(self) -> str:
        """ipam/prefixes/overlapped."""
        return self.get_str(keys=["overlapped"], data=self.data)

    def prefix(self) -> str:
        """ipam/prefixes/prefix, ipam/aggregates/prefix.

        :raises: NbParserError - if the prefix does not match the naming convention x.x.x.x/x
            and self.strict=True
        """
        prefix = self.get_str(keys=["prefix"], data=self.data)
        if self.strict:
            if not self.is_prefix(subnet=prefix):
                raise NbParserError(f"invalid {prefix=}")
        return prefix

    def role(self) -> str:
        """ipam/prefixes/role/slug."""
        return self.get_str(keys=["role", "slug"], data=self.data)

    def site(self, **kwargs) -> str:
        """ipam/prefixes/site/name from self.data (default) or from `kwargs`.

        NOTE: In different objects name has different upper|lower case.
            Netbox.sites.name="SITE1",
            Netbox.devices.site.name="SITE1"
            Netbox.vlans.site.name="site1"
        :return: Site name
        """
        data = kwargs or self.data
        return self.get_str(keys=["site", "name"], data=data)

    def status(self) -> str:
        """ipam/prefixes/status/value."""
        return self.get_str(keys=["status", "value"], data=self.data)

    def tenant(self) -> str:
        """ipam/prefixes/tenant/name."""
        return self.get_str(keys=["tenant", "name"], data=self.data)

    def vid(self) -> int:
        """Netbox.vlans.vid."""
        return int(self.data.get("vid") or 0)

    def vlan(self) -> int:
        """ipam/prefixes/vlan/vid."""
        return self.get_int(keys=["vlan", "vid"])

    def vlan_group(self) -> str:
        """Netbox.vlans.group.name."""
        return self.get_str(keys=["group", "name"])

    def tags(self) -> LStr:
        """ipam/prefixes/tags/id/slug."""
        tags_ = self.get_list(keys=["tags"], data=self.data)
        if not tags_:
            return []
        tags: LStr = []
        for tag_ in tags_:
            if tag := self.get_str(keys=["slug"], data=tag_):
                tags.append(tag)
        return tags

    def url(self) -> str:
        """Netbox.prefixes.id."""
        url = self.get_str(keys=["url"])
        if not url and self.strict:
            raise NbParserError(f"invalid {url=}")
        return url

    # ========================= firewalls in =========================

    def firewalls__in_aggregate(self) -> SStr:
        """Firewalls hostnames from Netbox.Aggregate.custom_fields or description."""
        if hostnames := self.firewalls__in_aggregate_custom_fields():
            return hostnames
        if hostnames := self.firewalls__in_aggregate_description():
            return hostnames
        return set()

    def firewalls__in_aggregate_custom_fields(self) -> SStr:
        """Firewalls hostnames from Netbox.aggregate.custom_fields."""
        try:
            value = self.data["custom_fields"]["firewalls"]
        except (KeyError, TypeError):
            return set()
        if not value or not isinstance(value, str):
            return set()
        hostnames_ = self.split_punctuation(value)
        hostnames = re.findall(r"^(\w+-\w+-\w+-\w+)", hostnames_, re.M)
        return set(hostnames)

    def firewalls__in_aggregate_description(self) -> SStr:
        """Firewalls hostnames from Netbox.aggregate.description."""
        tags = self.tags()
        if "noc_aggregates_belonging" not in tags:
            return set()
        try:
            description = self.data["description"]
        except (KeyError, TypeError):
            if self.strict:
                raise
            return set()
        if not isinstance(description, str):
            if self.strict:
                raise TypeError(f"{description=}, {str} expected")
            return set()
        descriptions = self.split_punctuation(description)
        hostnames = set(re.findall(r"^(\w+-\w+-\w+-\w+)", descriptions, re.M))
        return hostnames

    # ============================ device ============================

    def device_name(self) -> str:
        """Netbox.devices.name.

        :raises: NbParserError - if device has no name and self.strict=True
        """
        name = self.get_str(keys=["name"], data=self.data)
        if not name and self.strict:
            raise NbParserError(f"absent name in {self.data=}")
        return name

    def device_model(self) -> str:
        """Netbox.devices.device_type.model.

        :raises: NbParserError - if device has no model and self.strict=True
        """
        model = self.get_str(keys=["device_type", "model"], data=self.data)
        if not model and self.strict:
            raise NbParserError(f"absent model in {self.data=}")
        return model

    def device_role(self) -> str:
        """Netbox.devices.device_role.name.

        :raises: NbParserError - if device has no device_role and self.strict=True
        """
        device_role = self.get_str(keys=["device_role", "name"], data=self.data)
        if not device_role and self.strict:
            raise NbParserError(f"absent device_role in {self.data=}")
        return device_role

    def device_platform(self) -> str:
        """Netbox.devices.platform.slug.

        :raises: NbParserError - if device has no platform and self.strict=True
        """
        platform = self.get_str(keys=["platform", "slug"], data=self.data)
        if not platform and self.strict:
            raise NbParserError(f"absent platform slug in {self.data=}")
        return platform

    def device_primary_ip4(self) -> str:
        """Netbox.devices.primary_ip4.

        :raises: NbParserError - if device has no primary_ip4 and self.strict=True
        """
        try:
            primary_ip4 = self.data["primary_ip4"]["address"]
        except (KeyError, TypeError):
            primary_ip4 = ""
        if not isinstance(primary_ip4, str):
            primary_ip4 = ""
        if not primary_ip4 and self.strict:
            raise NbParserError(f"absent primary_ip4 in {self.data=}")
        regex = r"^\d+\.\d+\.\d+\.\d+(/\d+)?$"
        if not re.match(regex, primary_ip4) and self.strict:
            raise NbParserError(f"invalid {primary_ip4=}, expected {regex=}")
        return primary_ip4

    def hostname_net_id(self) -> str:
        """Network ID, 3rd item in the hostname."""
        name = self.name()
        net_id = (re.findall(r"\w+-\w+-.(\w+)-\w+", name) or [""])[0]
        return net_id

    def hostname_platform(self) -> str:
        """-asa-,-cnx-,-ios-. 4th item (split by "-") in Netbox.devices.name."""
        name = self.name()
        platform = (re.findall(r"\w+-\w+-\w+-(\w+)", name) or [""])[0]
        return platform

    def hostname_role(self) -> str:
        """-fw-,-ic-,-sw-,-wn-. 2nd item (split by "-") in Netbox.devices.name."""
        name = self.name()
        role = (re.findall(r"\w+-(\w+)-\w+-\w+", name) or [""])[0]
        if re.match(r"\d+$", role):
            role = "sw"
        return role

    def sw_version(self) -> str:
        """Netbox.custom_fields.sw_version."""
        return self.get_str(keys=["custom_fields", "sw_version"], data=self.data)

    def hostname_site(self) -> str:
        """1st item (split by "-") in Netbox.devices.name."""
        name = self.name()
        site = (re.findall(r"(\w+)-\w+-\w+-\w+", name) or [""])[0]
        return site

    # ============================ device-types ============================

    def model(self) -> str:
        """Netbox.device type model.

        :raises: NbParserError - if device type has no model and self.strict
        """
        model = self.get_str(keys=["model"], data=self.data)
        if not model and self.strict:
            raise NbParserError(f"absent model in {self.data=}")
        return model

    def planned_version(self) -> str:
        """Netbox.device types planned software version."""
        return self.get_str(keys=["custom_fields", "sw_planned"], data=self.data)

    # ============================== is ==============================

    def is_ipam(self, ipam: str) -> bool:
        """Return True if object is ipam.

        If ipam url "/api/ipam/" contains "aggregate", "prefix", "address".
        :raises: NbParserError - if url is not /api/ipam/aggregate or prefix or address
            and self.strict=True
        """
        try:
            url = self.data["url"]
            if re.search(f"/api/ipam/{ipam}/", url):
                return True
            return False
        except (KeyError, TypeError):
            if self.strict:
                raise NbParserError(f"invalid url in {self.data=}")
            return False

    def is_dcim(self, dcim: str) -> bool:
        """Return True if object is dcim/devices.

        :raises: NbParserError - if url is not /api/dcim/ and self.strict=True
        """
        try:
            url = self.data["url"]
            if re.search(f"/api/dcim/{dcim}/", url):
                return True
            return False
        except (KeyError, TypeError):
            if self.strict:
                raise NbParserError(f"invalid url in {self.data=}")
            return False

    def is_vrf(self) -> bool:
        """Return True if data has vrf."""
        if self.data.get("vrf"):
            return True
        return False

    @staticmethod
    def is_ip(subnet: str) -> bool:
        """Return True if subnet has x.x.x.x format."""
        if re.match(r"^\d+\.\d+\.\d+\.\d+$", subnet):
            return True
        return False

    @staticmethod
    def is_prefix(subnet: str) -> bool:
        """Return True if subnet has x.x.x.x/x format."""
        if re.match(fr"^{RE_PREFIX}$", subnet):
            return True
        return False

    # ======================== public helpers ========================

    def get_dict(self, keys: LStr, **kwargs) -> dict:
        """Get dict value by keys from kwargs or self.data."""
        data = kwargs.get("data") or self.data
        return self._get_keys(type_=dict, keys=keys, data=data)

    def get_int(self, keys: LStr, **kwargs) -> int:
        """Get int value by keys from kwargs or self.data."""
        data = kwargs.get("data") or self.data
        try:
            for key in keys:
                data = data[key]
        except (KeyError, TypeError) as ex:
            if self.strict:
                name = type(ex).__name__
                raise NbParserError(f"{name}: {ex}, {keys=} {data=}")
            return 0
        if isinstance(data, int):
            return data
        if isinstance(data, str) and data.isdigit():
            return int(data)
        if self.strict:
            raise NbParserError(f"invalid, {keys=} {data=}")
        return 0

    def get_list(self, keys: LStr, **kwargs) -> list:
        """Get list value by keys from kwargs or self.data."""
        data = kwargs.get("data") or self.data
        return self._get_keys(type_=list, keys=keys, data=data)

    def get_str(self, keys: LStr, **kwargs) -> str:
        """Get string value by keys from kwargs or self.data."""
        data = kwargs.get("data") or self.data
        return self._get_keys(type_=str, keys=keys, data=data)

    @staticmethod
    def split_punctuation(text: str) -> str:
        """Split string by punctuation chars."""
        chars = string.punctuation.replace("_", "").replace("-", "")
        chars = fr"[\s{chars}]+"
        items = re.split(chars, text)
        items = [s for s in items if s]
        return "\n".join(items)

    # =========================== helper =============================

    def _get_keys(self, type_: Type, keys: LStr, data: dict):
        """Get value from data by chain keys, check data type_.

        :param type_: Interested type.
        :param keys: Interested chain keys in data.
        :param data: dict.
        :return: searching value.
        :raises: KeyError if key absent in data and self.strict == True.
        :raises: TypeError if type not match and self.strict == True.
        """
        try:
            for key in keys:
                data = data[key]
        except (KeyError, TypeError) as ex:
            if self.strict:
                name = type(ex).__name__
                raise NbParserError(f"{name}: {ex}, {keys=} {data=}")
            return type_()
        if not isinstance(data, type_):
            if self.strict:
                name = "TypeError"
                raise NbParserError(f"{name}: {keys=} {data=}, {type_} expected")
            return type_()
        return data


# ============================== helper ==============================

def _init_version(**kwargs) -> Version:
    """Init version."""
    version = kwargs.get("version") or "0"
    if isinstance(version, Version):
        return version
    return Version(str(version))
