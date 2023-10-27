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
        self._concurrent = (
            "q",
            "tag",
        )
        self._change_params = {
            "cid": {"query": "circuits/circuits/", "key": "cid"},
            "site": {"query": "dcim/sites/", "key": "name"},
        }

    # noinspection PyIncorrectDocstring
    def get(self, **kwargs) -> LDAny:
        """Get /circuits/circuit-terminations/ objects.

        Each finding parameter can be a value or a list of values.
        Not all finding parameters are documented.
        You can use any finding parameter that are present in the WEB UI.
        You can use some of the keys in data object as
        finding parameters that are missing in the WEB UI.

        WEB UI Finding parameters
        -------------------------

        API Finding parameters
        ----------------------

        :param id: Object ID.
        :type id: int or List[int]
        :example id: [1, 2]

        :param cid: Circuit ID.
        :type cid: str or List[str]
        :example cid: ["CID1", "CID2"]
        :param circuit_id: Circuit object ID.
        :type circuit_id: int or List[int]
        :example circuit_id: [1, 2]

        :param site: Site name.
        :type site: str or List[str]
        :example site: ["FRA1", "FFL1"]
        :param site_id: Site object ID.
        :type site_id: int or List[int]
        :example site_id: [1, 2]

        :param port_speed: Port speed.
        :type port_speed: int or List[int]
        :example port_speed: [100000, 1000000]

        :return: List of found objects.
        """
        kwargs = self._change_param_name_to_id(kwargs)
        params: LDAny = self._validate_concurrent_params(**kwargs)
        params = self._join_params(*params)

        items: LDAny = self._query_params_ld(params)
        self._check_keys(items=items, denied=self._reserved_ipam_keys)
        return items
