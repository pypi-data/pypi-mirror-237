"""Devices."""

from vpnetbox.api.base import Base
from vpnetbox.types_ import LDAny


class Devices(Base):
    """Devices."""

    def __init__(self, **kwargs):
        """Init Devices.

        :param kwargs: Parameters documented in parent object.
        """
        super().__init__(**kwargs)
        self._query = "dcim/devices/"
        self._sliced = "name"
        self._concurrent = (
            "cf_sw_version",
            "has_primary_ip",
            "q",
            "status",
            "tag",
            "virtual_chassis_member",
        )

    def get(self, **kwargs) -> LDAny:
        """Get devices objects from Netbox.

        :param kwargs: Finding parameters.

        ======================= =================== ================================================
        Parameter               single-value        multiple-values
        ======================= =================== ================================================
        name                    "device1"           ["device1", "device2"]
        id                      19280               [19280, 5737]
        q                       "device1"           ["device1", "device12"]
        tag                     "tag1"              ["tag1", "tag2"]
        site                    "site1"             ["site1", "site2"]
        rack_group_id           7                   [7, 8]
        rack_id                 33                  [32, 33]
        status                  "active"            ["inventory", "planned"]
        role                    "router"            ["router", "switch"]
        tenant                  "tenant1"           ["tenant1", "tenant2"]
        model                   "pa-820"            ["pa-820", "pa-850"]
        has_primary_ip          True, False
        manufacturer            "paloalto"          ["paloalto", "fortinet"]
        platform                "paloalto_panos"    ["paloalto_panos", "fortinet"]
        virtual_chassis_member  True, False
        cf_sw_version           "9.1.12"            ["9.1.12", "9.1.13"]
        ======================= =================== ================================================

        :return: List of devices objects.
        """
        params: LDAny = self._validate_concurrent_params(**kwargs)
        params = self._join_params(*params)
        items: LDAny = self._query_params_ld(params)
        return items
