"""Vlans."""

from vpnetbox.api.base import Base
from vpnetbox.types_ import LDAny


class Vlans(Base):
    """Vlans."""

    def __init__(self, **kwargs):
        """Init Vlans.

        :param kwargs: Parameters documented in parent object.
        """
        super().__init__(**kwargs)
        self._query = "ipam/vlans/"
        self._concurrent = (
            "cf_env",
            "q",
            "status",
            "tag",
            "vlan",
        )

    def get(self, **kwargs) -> LDAny:
        """Get Vlans objects from Netbox.

        :param kwargs: Finding parameters.

        =============== =================== ========================================================
        Parameter       single-value        multiple-values
        =============== =================== ========================================================
        vid             22                  [22, 24]
        id              7683                [7683, 7684]
        q               "22"                ["22", "24"]
        tag             "tag1"              ["tag1", "tag2"]
        group_id        12                  [12, 13]
        status          "active"            ["reserved", "deprecated"]
        site            "site1"             ["site1", "site2"]
        role            "role1"             ["role1", "role2"]
        tenant          "tenant1"           ["tenant1", "tenant2"]
        =============== =================== ========================================================

        :return: List of Vlans objects.
        """
        params: LDAny = self._validate_concurrent_params(**kwargs)
        params = self._join_params(*params)
        items: LDAny = self._query_params_ld(params)
        self._check_keys(items=items, denied=self._reserved_ipam_keys)
        return items
