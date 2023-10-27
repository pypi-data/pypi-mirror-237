"""Roles - Prefix/VLAN Roles."""

from vpnetbox.api.base import Base
from vpnetbox.types_ import LDAny


class Roles(Base):
    """Roles - Prefix/VLAN Roles."""

    def __init__(self, **kwargs):
        """Init Roles.

        :param kwargs: Parameters documented in parent object.
        """
        super().__init__(**kwargs)
        self._query = "ipam/roles/"
        self._concurrent = (
            "q",
            "tag",
        )

    def get(self, **kwargs) -> LDAny:
        """Get Roles objects from Netbox.

        :param kwargs: Finding parameters.

        =============== =================== ========================================================
        Parameter       single-value        multiple-values
        =============== =================== ========================================================
        id              1                   [1, 3]
        q               "role1"             ["role1", "role2"]
        tag             "tag1"              ["tag1", "tag2"]
        =============== =================== ========================================================

        :return: List of Roles objects.
        """
        params: LDAny = self._validate_concurrent_params(**kwargs)
        params = self._join_params(*params)
        items: LDAny = self._query_params_ld(params)
        return items
