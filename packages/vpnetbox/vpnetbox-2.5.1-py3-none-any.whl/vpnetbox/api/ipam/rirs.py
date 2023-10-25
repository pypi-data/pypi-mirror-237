"""RIRs - Regional Internet Registries."""

from vpnetbox.api.base import Base
from vpnetbox.types_ import LDAny


class Rirs(Base):
    """RIRs - Regional Internet Registries."""

    def __init__(self, **kwargs):
        """Init Rirs.

        :param kwargs: Parameters documented in parent object.
        """
        super().__init__(**kwargs)
        self._query = "ipam/rirs/"
        self._concurrent = (
            "q",
            "tag",
        )

    def get(self, **kwargs) -> LDAny:
        """Get RIRs objects from Netbox.

        :param kwargs: Finding parameters.

        =============== =================== ========================================================
        Parameter       single-value        multiple-values
        =============== =================== ========================================================
        name            "RFC 1918"          ["RFC 1918", "RIPE"]
        id              1                   [1, 3]
        q               "RFC"               ["RFC", "RIPE"]
        tag             "tag1"              ["tag1", "tag2"]
        slug            "rfc-1918"          ["rfc-1918", "ripe"]
        is_private      True
        description     "text"              ["text", "text2"]
        =============== =================== ========================================================

        :return: List of RIRs objects.
        """
        params: LDAny = self._validate_concurrent_params(**kwargs)
        params = self._join_params(*params)
        items: LDAny = self._query_params_ld(params)
        return items
