"""Connector to https://{netbox}/api/ipam/ip-addresses/."""

from vpnetbox.api.base import Base
from vpnetbox.types_ import LDAny


class Addresses(Base):
    """Connector to https://{netbox}/api/ipam/ip-addresses/."""

    def __init__(self, **kwargs):
        """Init IPAM Addresses.

        :param kwargs: Parameters documented in parent object.
        """
        super().__init__(**kwargs)
        self._query = "ipam/ip-addresses/"
        self._sliced = "address"
        self._concurrent = (
            "assigned_to_interface",
            "family",
            "mask_length",
            "parent",
            "q",
            "status",
            "tag",
        )
        self._change_params = {
            "present_in_vrf": {"query": "ipam/vrfs/", "key": "name"},
            "vrf": {"query": "ipam/vrfs/", "key": "name"},
        }

    # noinspection PyIncorrectDocstring
    def get(self, **kwargs) -> LDAny:
        """Get /ipam/ip-addresses/ objects.

        Each finding parameter can be a value or a list of values.
        Not all finding parameters are documented.
        You can use any finding parameter that are present in the WEB UI.
        You can use some of the keys in data object as
        finding parameters that are missing in the WEB UI.


        WEB UI Finding parameters
        -------------------------------------------------

        :param q: Search. Substring of address value.
        :type q: str or List[str]
        :example q: ["10.0.0.", "10.31.65."]

        :param tag: Tag.
        :type tag: str or List[str]
        :example tag: ["TAG1", "TAG2"]

        :param parent: Parent Prefix. Addresses that are part of this prefix.
        :type parent: str or List[str]
        :example parent: ["10.0.0.0/24", "10.31.65.0/26"]

        :param family: Address family. IP version.
        :type family: int or List[int]
        :example family: [4, 6]

        :param status: Status.
        :type status: str or List[str]
        :example status: ["active", "reserved"]

        :param role: Role.
        :type role: str or List[str]
        :example role: ["secondary", "hsrp"]

        :param mask_length: Mask length.
        :type mask_length: int or List[int]
        :example mask_length: [24, 32]

        :param assigned_to_interface: Assigned to an interface.
        :type assigned_to_interface: bool
        :example assigned_to_interface: True

        :param dns_name: DNS name.
        :type dns_name: str or List[str]
        :example dns_name: ["host1.domain.com", "host2.domain.com"]

        :param vrf: Assigned VRF.
        :type vrf: str or List[str]
        :example vrf: ["customer1", "customer2"]

        :param present_in_vrf: Present in VRF.
        :type present_in_vrf: str or List[str]
        :example present_in_vrf: ["customer1", "customer2"]

        :param tenant: Tenant.
        :type tenant: str or List[str]
        :example tenant: ["team1", "team2"]


        API Finding parameters
        --------------------------------------------------

        :param id: IP-address object ID.
        :type id: int or List[int]
        :example id: [1, 2]

        :param address: IP Address with prefix length, A.B.C.D/LEN.
        :type address: str or List[str]
        :example address: ["10.0.0.1/26", "10.0.0.2/26"]

        :param vrf: VRF name.
        :type vrf: str or List[str]
        :example vrf: ["vrf1", "vrf2"]
        :param vrf_id: VRF object ID.
        :type vrf_id: int or List[int]
        :example vrf_id: [1, 2]

        :param present_in_vrf: VRF name.
        :type present_in_vrf: str or List[str]
        :example present_in_vrf: ["vrf1", "vrf2"]
        :param present_in_vrf_id: VRF object ID.
        :type present_in_vrf_id: int or List[int]
        :example present_in_vrf_id: [1, 2]

        :param tenant_id: Tenant object ID.
        :type tenant_id: int or List[int]
        :example tenant_id: [1, 2]

        :param tenant_group_id: Tenant group object ID.
        :type tenant_group_id: int or List[int]
        :example tenant_group_id: [1, 2]

        :param device_id: Device object ID.
        :type device_id: int or List[int]
        :example device_id: [1, 2]

        :param virtual_machine_id: Virtual machine object ID.
        :type virtual_machine_id: int or List[int]
        :example virtual_machine_id: [1, 2]

        :param description: Description.
        :type description: str or List[str]
        :example description: ["text1", "text2"]

        :param created: Datetime when the object was created.
        :type created: str or List[str]
        :example created: ["2000-12-31T23:59:59Z", "2001-01-01T01:01:01Z"]

        :param last_updated: Datetime when the object was updated.
        :type last_updated: str or List[str]
        :example last_updated: ["2000-12-31T23:59:59Z", "2001-01-01T01:01:01Z"]

        :return: List of found objects.
        """
        kwargs = self._change_param_name_to_id(kwargs)
        params: LDAny = self._validate_concurrent_params(**kwargs)
        params = self._join_params(*params)

        items: LDAny = self._query_params_ld(params)

        if not self._is_vrf_in_params(params):
            items = self._items_wo_vrf(items=items)
        self._check_keys(items=items, denied=self._reserved_ipam_keys)
        return items
