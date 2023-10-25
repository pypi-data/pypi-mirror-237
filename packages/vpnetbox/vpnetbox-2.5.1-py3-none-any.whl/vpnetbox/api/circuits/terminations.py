"""Terminations."""

from vpnetbox.api.base import Base
from vpnetbox.types_ import LDAny


class Terminations(Base):
    """Terminations."""

    def __init__(self, **kwargs):
        """Init Terminations.

        :param kwargs: Parameters documented in parent object.
        """
        super().__init__(**kwargs)
        self._query = "circuits/circuit-terminations/"
        self._sliced = "address"
        self._concurrent = (
            "q",
            "status",
            "tag",
        )

    def get(self, **kwargs) -> LDAny:
        """Get circuit-terminations objects from Netbox.

        :param kwargs: Finding parameters.

        ===================== =================== ==================================================
        Parameter             single-value        multiple-values
        ===================== =================== ==================================================
        id                    636                 [636, 734]
        circuit_id            9                   [9, 14]
        ===================== =================== ==================================================

        :return: List of circuit-terminations objects.
        """
        kwargs = self._param_vrf(**kwargs)
        params: LDAny = self._validate_concurrent_params(**kwargs)
        params = self._join_params(*params)

        items: LDAny = self._query_params_ld(params)
        self._check_keys(items=items, denied=self._reserved_ipam_keys)
        return items
