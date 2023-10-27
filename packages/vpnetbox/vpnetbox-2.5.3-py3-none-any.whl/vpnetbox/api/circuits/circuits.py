"""Circuits."""

from vpnetbox.api.base import Base
from vpnetbox.types_ import LDAny


class Circuits(Base):
    """Circuits."""

    def __init__(self, **kwargs):
        """Init Circuits.

        :param kwargs: Parameters documented in parent object.
        """
        super().__init__(**kwargs)
        self._query = "circuits/circuits/"
        self._concurrent = (
            "q",
            "status",
            "tag",
        )
        self._change_params = {
            "provider": {"query": "circuits/providers/", "key": "name"},
            "provider_account": {"query": "circuits/provider-accounts/", "key": "name"},
            "region": {"query": "dcim/regions/", "key": "name"},
            "site": {"query": "dcim/sites/", "key": "name"},
            "site_group": {"query": "dcim/site-groups/", "key": "name"},
            "tenant": {"query": "tenancy/tenants/", "key": "name"},
            "tenant_group": {"query": "tenancy/tenant-groups/", "key": "name"},
            "type": {"query": "circuits/circuit-types/", "key": "name"},
        }

    # noinspection PyIncorrectDocstring
    def get(self, **kwargs) -> LDAny:
        """Get /circuits/circuits/ objects.

        Each finding parameter can be a value or a list of values.
        Not all finding parameters are documented.
        You can use any finding parameter that are present in the WEB UI.
        You can use some of the keys in data object as
        finding parameters that are missing in the WEB UI.

        WEB UI Finding parameters
        -------------------------

        :param q: Search. Substring of circuit ID.
        :type q: str or List[str]
        :example q: ["CID1", "CID2"]

        :param tag: Tag.
        :type tag: str or List[str]
        :example tag: ["TAG1", "TAG2"]

        :param provider: Provider name.
        :type provider: str or List[str]
        :example provider: ["PROVIDER1", "PROVIDER2"]
        :param provider_id: Provider object ID.
        :type provider_id: int or List[int]
        :example provider_id: [1, 2]

        :param provider_account: Provider account.
        :type provider_account: str or List[str]
        :example provider_account: ["PROVIDER1", "PROVIDER2"]
        :param provider_account_id: Provider account object ID.
        :type provider_account_id: int or List[int]
        :example provider_account_id: [1, 2]

        :param type: Circuit type.
        :type type: str or List[str]
        :example type: ["WAN", "DIA"]
        :param type_id: Circuit type object ID.
        :type type_id: int or List[int]
        :example type_id: [1, 2]

        :param status: Circuit status.
        :type status: str or List[str]
        :example status: ["active", "offline"]

        :param region: Region.
        :type region: str or List[str]
        :example region: ["USA", "EU"]
        :param region_id: Region object ID.
        :type region_id: int or List[int]
        :example region_id: [1, 2]

        :param site_group: Site group.
        :type site_group: str or List[str]
        :example site_group: ["FRA", "FFL"]
        :param site_group_id: Site group object ID.
        :type site_group_id: int or List[int]
        :example site_group_id: [1, 2]

        :param site: Site name.
        :type site: str or List[str]
        :example site: ["FRA1", "FFL1"]
        :param site_id: Site object ID.
        :type site_id: int or List[int]
        :example site_id: [1, 2]

        :param tenant_group: Tenant group.
        :type tenant_group: str or List[str]
        :example tenant_group: ["TENANT1", "TENANT2"]
        :param tenant_group_id: Tenant group object ID.
        :type tenant_group_id: int or List[int]
        :example tenant_group_id: [1, 2]

        :param tenant: Tenant.
        :type tenant: str or List[str]
        :example tenant: ["TENANT1", "TENANT2"]
        :param tenant_id: Tenant object ID.
        :type tenant_id: int or List[int]
        :example tenant_id: [1, 2]

        :param cf_monitoring_ip: Custom fields.
        :type cf_monitoring_ip: str or List[str]
        :example cf_monitoring_ip: ["10.0.0.1", "10.0.0.2"]

        API Finding parameters
        ----------------------

        :param id: Object ID.
        :type id: int or List[int]
        :example id: [1, 2]

        :param cid: Circuit ID.
        :type cid: str or List[str]
        :example cid: ["CID1", "CID2"]

        :return: List of circuit objects.
        """
        kwargs = self._change_param_name_to_id(kwargs)
        params: LDAny = self._validate_concurrent_params(**kwargs)
        params = self._join_params(*params)

        items: LDAny = self._query_params_ld(params)
        self._check_keys(items=items, denied=self._reserved_ipam_keys)
        return items
