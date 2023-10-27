"""IpRanges."""

from vpnetbox.api.base import Base
from vpnetbox.types_ import LDAny


class IpRanges(Base):
    """IpRanges."""

    def __init__(self, **kwargs):
        """Init IpRanges.

        :param kwargs: Parameters documented in parent object.
        """
        super().__init__(**kwargs)
        self._query = "ipam/ip-ranges/"
        self._concurrent = (
            "q",
            "tag",
        )

    def get(self, **kwargs) -> LDAny:
        """Get IP-Ranges objects from Netbox.

        :param kwargs: Finding parameters.

        ===================== =================== ==================================================
        Parameter             single-value        multiple-values
        ===================== =================== ==================================================
        id                    14                  [14, 15]
        q                     "127.255.254.1/30"  ["127.255.254.1/30", "127.255.254.101/30"]
        tag                   "tag1"              ["tag1", "tag2"]
        family                4                   [4, 6]
        vrf_id                40                  [40, 41]
        status                "active"            ["reserved", "deprecated"]
        role                  "role1"             ["role1", "role2"]
        tenant                "tenant1"           ["tenant1", "tenant2"]
        ===================== =================== ==================================================

        :return: List of IP-Ranges objects.
        """
        params: LDAny = self._validate_concurrent_params(**kwargs)
        params = self._join_params(*params)
        items: LDAny = self._query_params_ld(params)
        if not self._is_vrf_in_params(params):
            items = self._items_wo_vrf(items=items)
        self._check_keys(items=items, denied=self._reserved_ipam_keys)
        return items
