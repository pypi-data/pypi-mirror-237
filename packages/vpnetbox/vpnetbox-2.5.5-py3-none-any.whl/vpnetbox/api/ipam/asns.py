"""ASNs - Autonomous System Numbers."""

from vpnetbox.api.base import Base
from vpnetbox.types_ import LDAny


class Asns(Base):
    """ASNs - Autonomous System Numbers."""

    def __init__(self, **kwargs):
        """Init Asns.

        :param kwargs: Parameters documented in parent object.
        """
        super().__init__(**kwargs)
        self._query = "ipam/asns/"
        self._concurrent = (
            "q",
            "tag",
        )

    def get(self, **kwargs) -> LDAny:
        """Get ASNs objects from Netbox.

        :param kwargs: Finding parameters.

        =============== =================== ========================================================
        Parameter       single-value        multiple-values
        =============== =================== ========================================================
        asn             65016               [65016, 65017]
        id              1                   [1, 3]
        q               "65016"             ["65016", "65017"]
        tag             "tag1"              ["tag1", "tag2"]
        rir             "rfc-1918"          ["ripe", "rfc-1918"]
        rir_id          6                   [2, 6]
        site            "site1"             ["site1", "site2"]
        site_id         50                  50, 60
        =============== =================== ========================================================

        :return: List of ASNs objects.
        """
        params: LDAny = self._validate_concurrent_params(**kwargs)
        params = self._join_params(*params)
        items: LDAny = self._query_params_ld(params)
        return items
