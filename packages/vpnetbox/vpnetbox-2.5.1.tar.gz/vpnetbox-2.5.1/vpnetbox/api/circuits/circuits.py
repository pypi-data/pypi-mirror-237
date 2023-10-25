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
        self._sliced = "address"
        self._concurrent = (
            "q",
            "status",
            "tag",
        )

    def get(self, **kwargs) -> LDAny:
        """Get circuits objects from Netbox.

        :param kwargs: Finding parameters.

        ===================== =================== ==================================================
        Parameter             single-value        multiple-values
        ===================== =================== ==================================================
        cid                   "circuit_id1"       ["circuit_id1", "circuit_id2"]
        id                     636                [636, 734]
        q                     "_id1"              ["_id1", "_id2"]
        tag                   "tag1"              ["tag1", "tag2"]
        provider              "provider1"         ["provider1", "provider2"]
        provider_id           1                   [1, 2]
        type                  "wan-link"          ["wan-link", "dia"]
        type_id               1                   [1, 2]
        status                "active"            ["reserved", "deprecated"]
        site                  "site1"             ["site1", "site2"]
        site_id               50                  [50, 60]
        cf_name              "cf_name1"           ["cf_name1", "cf_name2"]
        tenant                "tenant1"           ["tenant1", "tenant2"]
        tenant_id             8                   [2, 8]
        ===================== =================== ==================================================

        :return: List of circuit objects.
        """
        kwargs = self._param_vrf(**kwargs)
        params: LDAny = self._validate_concurrent_params(**kwargs)
        params = self._join_params(*params)

        items: LDAny = self._query_params_ld(params)
        self._check_keys(items=items, denied=self._reserved_ipam_keys)
        return items
