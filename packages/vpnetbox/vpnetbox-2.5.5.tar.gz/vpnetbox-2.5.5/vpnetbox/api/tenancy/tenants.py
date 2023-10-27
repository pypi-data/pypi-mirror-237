"""Tenants."""

from vpnetbox.api.base import Base
from vpnetbox.types_ import LDAny


class Tenants(Base):
    """Tenants."""

    def __init__(self, **kwargs):
        """Init Tenants.

        :param kwargs: Parameters documented in parent object.
        """
        super().__init__(**kwargs)
        self._query = "tenancy/tenants/"
        self._concurrent = (
            "q",
            "tag",
        )
        self._change_params = {
            "group": {"query": "tenancy/tenant-groups/", "key": "name"},
        }

    # noinspection PyIncorrectDocstring
    def get(self, **kwargs) -> LDAny:
        """Get tenancy/tenants/ objects.

        Each finding parameter can be a value or a list of values.
        Not all finding parameters are documented.
        You can use any finding parameter that are present in the WEB UI.
        You can use some of the keys in data object as
        finding parameters that are missing in the WEB UI.

        WEB UI Finding parameters
        -------------------------

        :param q: Search. Substring of tenant name.
        :type q: str or List[str]
        :example q: ["TENANT1", "TENANT2"]

        :param tag: Tag.
        :type tag: str or List[str]
        :example tag: ["TAG1", "TAG2"]

        :param group: Tenant group name.
        :type group: str or List[str]
        :example group: ["GROUP1", "GROUP2"]
        :param group_id: Tenant group object ID.
        :type group_id: int or List[int]
        :example group_id: [1, 2]

        API Finding parameters
        ----------------------

        :param id: Object ID.
        :type id: int or List[int]
        :example id: [1, 2]

        :param name: Tenant name.
        :type name: str or List[str]
        :example name: ["TENANT1", "TENANT1"]

        :param slug: Tenant slug.
        :type slug: str or List[str]
        :example slug: ["tenant1", "tenant1"]

        :return: List of found objects.
        """
        kwargs = self._change_param_name_to_id(kwargs)
        params: LDAny = self._validate_concurrent_params(**kwargs)
        params = self._join_params(*params)

        items: LDAny = self._query_params_ld(params)
        self._check_keys(items=items, denied=self._reserved_ipam_keys)
        return items
