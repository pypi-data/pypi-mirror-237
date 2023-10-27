"""Device Types."""

from vpnetbox.api.base import Base
from vpnetbox.types_ import LDAny


class DeviceTypes(Base):
    """Device Types."""

    def __init__(self, **kwargs):
        """Init DeviceTypes.

        :param kwargs: Parameters documented in parent object.
        """
        super().__init__(**kwargs)
        self._query = "dcim/device-types/"
        self._sliced = "display_name"
        self._concurrent = (
            "q",
            "tag",
        )

    def get(self, **kwargs) -> LDAny:
        """Get device_types from Netbox.

        :param kwargs: Finding parameters.

        =============== ============================== =============================================
        Parameter       single-value                   multiple-values
        =============== ============================== =============================================
        q               "2960x"                        ["2911", "2960"]
        manufacturer    "cisco"                        ["cisco", "hp"]
        tag             "tag1"                         ["tag1", "tag2"]
        =============== ============================== =============================================

        :return: List of device_types objects.
        """
        params: LDAny = self._validate_concurrent_params(**kwargs)
        params = self._join_params(*params)
        items: LDAny = self._query_params_ld(params)
        return items
