"""Providers."""

from vpnetbox.api.base import Base
from vpnetbox.types_ import LDAny


class Providers(Base):
    """Providers."""

    def __init__(self, **kwargs):
        """Init Providers.

        :param kwargs: Parameters documented in parent object.
        """
        super().__init__(**kwargs)
        self._query = "circuits/providers/"
        self._concurrent = (
            "q",
            "tag",
        )
        self._change_params = {
            "region": {"query": "dcim/regions/", "key": "name"},
            "site": {"query": "dcim/sites/", "key": "name"},
            "site_group": {"query": "dcim/site-groups/", "key": "name"},
        }

    # noinspection PyIncorrectDocstring
    def get(self, **kwargs) -> LDAny:
        """Get /circuits/providers/ objects.

        Each finding parameter can be a value or a list of values.
        Not all finding parameters are documented.
        You can use any finding parameter that are present in the WEB UI.
        You can use some of the keys in data object as
        finding parameters that are missing in the WEB UI.

        WEB UI Finding parameters
        -------------------------

        :param q: Search. Substring of provider name.
        :type q: str or List[str]
        :example q: ["PROVIDER1", "PROVIDER2"]

        :param tag: Tag.
        :type tag: str or List[str]
        :example tag: ["TAG1", "TAG2"]

        :param region: Region.
        :type region: str or List[str]
        :example region: ["USA", "EU"]
        :param region_id: Region object ID.
        :type region_id: int or List[int]
        :example region_id: [1, 2]

        :param site_group: Site group.
        :type site_group: str or List[str]
        :example site_group: ["FRA", "FFL"]
        :param site_group_id: Site group object ID.
        :type site_group_id: int or List[int]
        :example site_group_id: [1, 2]

        :param site: Site name.
        :type site: str or List[str]
        :example site: ["FRA1", "FFL1"]
        :param site_id: Site object ID.
        :type site_id: int or List[int]
        :example site_id: [1, 2]

        API Finding parameters
        ----------------------

        :param id: Object ID.
        :type id: int or List[int]
        :example id: [1, 2]

        :param name: Provider name.
        :type name: str or List[str]
        :example name: ["PROVIDER1", "PROVIDER2"]

        :param slug: Provider slug.
        :type slug: str or List[str]
        :example slug: ["provider1", "provider2"]

        :return: List of found objects.
        """
        kwargs = self._change_param_name_to_id(kwargs)
        params: LDAny = self._validate_concurrent_params(**kwargs)
        params = self._join_params(*params)

        items: LDAny = self._query_params_ld(params)
        self._check_keys(items=items, denied=self._reserved_ipam_keys)
        return items
