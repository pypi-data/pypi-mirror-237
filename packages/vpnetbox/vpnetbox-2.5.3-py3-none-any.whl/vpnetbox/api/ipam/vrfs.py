"""Vrfs - Virtual Routing and Forwarding (VRF)."""

from vpnetbox.api.base import Base
from vpnetbox.types_ import LDAny


class Vrfs(Base):
    """Vrfs - Virtual Routing and Forwarding (VRF)."""

    def __init__(self, **kwargs):
        """Init Vrfs.

        :param kwargs: Parameters documented in parent object.
        """
        super().__init__(**kwargs)
        self._query = "ipam/vrfs/"
        self._concurrent = (
            "q",
            "tag",
        )

    def get(self, **kwargs) -> LDAny:
        """Get Vrf objects from Netbox.

        :param kwargs: Finding parameters.

        =============== =================== ========================================================
        Parameter       single-value        multiple-values
        =============== =================== ========================================================
        id              1                   [1, 3]
        q               "vrf1"              ["vrf1", "vrf2"]
        tag             "tag1"              ["tag1", "tag2"]
        =============== =================== ========================================================

        :return: List of Vrf objects.
        """
        params: LDAny = self._validate_concurrent_params(**kwargs)
        params = self._join_params(*params)
        items: LDAny = self._query_params_ld(params)
        return items
