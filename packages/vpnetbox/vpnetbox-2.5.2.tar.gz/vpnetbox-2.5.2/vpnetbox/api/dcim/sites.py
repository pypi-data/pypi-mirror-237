"""Sites."""

from vpnetbox.api.base import Base
from vpnetbox.types_ import LDAny


class Sites(Base):
    """Sites."""

    def __init__(self, **kwargs):
        """Init Sites.

        :param kwargs: Parameters documented in parent object.
        """
        super().__init__(**kwargs)
        self._query = "dcim/sites/"
        self._concurrent = (
            "q",
            "tag",
        )

    def get(self, **kwargs) -> LDAny:
        """Get sites objects from Netbox.

        :param kwargs: Finding parameters.

        =============== =================== ========================================================
        Parameter       single-value        multiple-values
        =============== =================== ========================================================
        name            "site1"             ["site1", "site2"]
        id              50                  [50, 51]
        q               "site1"             [site1", "site2"]
        tag             "tag1"              ["tag1", "tag2"]
        status          "active"            ["planned", "retired"]
        region          "eu"                ["eu", "usa"]
        asn             65017               [65017, 65018]
        tenant          "tenant1"           ["tenant1", "tenant2"]
        cf_name         "cf_name1"          ["cf_name1", "cf_name2"]
        =============== =================== ========================================================

        :return: List of sites objects.
        """
        params: LDAny = self._validate_concurrent_params(**kwargs)
        params = self._join_params(*params)
        items: LDAny = self._query_params_ld(params)
        return items
