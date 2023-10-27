"""CircuitTypes."""

from vpnetbox.api.base import Base
from vpnetbox.types_ import LDAny


class CircuitTypes(Base):
    """CircuitTypes."""

    def __init__(self, **kwargs):
        """Init CircuitTypes.

        :param kwargs: Parameters documented in parent object.
        """
        super().__init__(**kwargs)
        self._query = "circuits/circuit-types/"
        self._concurrent = (
            "q",
            "tag",
        )

    # noinspection PyIncorrectDocstring
    def get(self, **kwargs) -> LDAny:
        """Get /circuits/circuit-types/ objects.

        Each finding parameter can be a value or a list of values.
        Not all finding parameters are documented.
        You can use any finding parameter that are present in the WEB UI.
        You can use some of the keys in data object as
        finding parameters that are missing in the WEB UI.

        WEB UI Finding parameters
        -------------------------

        :param q: Search. Substring of circuit type name.
        :type q: str or List[str]
        :example q: ["DIA", "WAN"]

        API Finding parameters
        ----------------------

        :param id: Object ID.
        :type id: int or List[int]
        :example id: [1, 2]

        :param name: Circuit type name.
        :type name: str or List[str]
        :example name: ["PROVIDER1", "PROVIDER2"]

        :param slug: Circuit type slug.
        :type slug: str or List[str]
        :example slug: ["provider1", "provider2"]

        :param tag: Tag.
        :type tag: str or List[str]
        :example tag: ["TAG1", "TAG2"]

        :return: List of found objects.
        """
        kwargs = self._change_param_name_to_id(kwargs)
        params: LDAny = self._validate_concurrent_params(**kwargs)
        params = self._join_params(*params)

        items: LDAny = self._query_params_ld(params)
        self._check_keys(items=items, denied=self._reserved_ipam_keys)
        return items
