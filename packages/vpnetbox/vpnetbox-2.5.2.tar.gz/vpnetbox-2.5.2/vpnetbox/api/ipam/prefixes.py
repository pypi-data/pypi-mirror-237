"""Prefixes."""

from vpnetbox.api.base import Base
from vpnetbox.types_ import LDAny


class Prefixes(Base):
    """Prefixes."""

    def __init__(self, **kwargs):
        """Init Prefixes.

        :param kwargs: Parameters documented in parent object.
        """
        super().__init__(**kwargs)
        self._query = "ipam/prefixes/"
        self._concurrent = (
            "assigned_to_interface",
            "cf_env",
            "family",
            "mask_length",
            "prefix",
            "q",
            "status",
            "tag",
        )

    def get(self, **kwargs) -> LDAny:
        """Get prefixes objects from Netbox.

        :param kwargs: Finding parameters.
        param           single-value        multiple-values

        =============== =========== =================== ============================================
        Parameter       default     single-value        multiple-values
        =============== =========== =================== ============================================
        prefix                      "10.0.0.0/26"       ["10.0.0.0/26", "10.31.65.0/26"]
        id                          1728                [1728, 2067]
        q                           "10.10.119"         ["10.10.119", "10.31.65"]
        tag                         "tag1"              [tag1", "tag2"]
        family          4           6                   [4, 6]
        status          "active"    "reserved"          ["reserved", "deprecated"]
        role                        "role1"             ["role1", "role2"]
        mask_length                 24                  [24, 32]
        is_pool         		    True, False
        vrf                         "vrf1"              ["vrf1", "vrf2"]
        vrf_id          0           40                  [40, 41]
        site                        "site1"             ["site1", "site2"]
        tenant                      "tenant1"           ["tenant1", "tenant2"]
        env                         "env1"              ["env1", "env2"]
        =============== =========== =================== ============================================

        :return: List of prefixes objects.
        """
        kwargs = self._change_param_name_to_id(kwargs)
        params: LDAny = self._validate_concurrent_params(**kwargs)
        params = self._join_params(*params)

        items: LDAny = self._query_params_ld(params)
        if not self._is_vrf_in_params(params):
            items = self._items_wo_vrf(items=items)
        self._check_keys(items=items, denied=self._reserved_ipam_keys)
        return items
