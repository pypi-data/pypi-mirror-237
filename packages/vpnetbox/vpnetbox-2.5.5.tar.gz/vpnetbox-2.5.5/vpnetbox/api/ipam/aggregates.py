"""Aggregates."""

from vpnetbox.api.base import Base
from vpnetbox.types_ import LDAny


class Aggregates(Base):
    """Aggregates."""

    def __init__(self, **kwargs):
        """Init Aggregates.

        :param kwargs: Parameters documented in parent object.
        """
        super().__init__(**kwargs)
        self._query = "ipam/aggregates/"
        self._concurrent = (
            "family",
            "prefix",
            "q",
            "status",
            "tag",
        )

    def get(self, **kwargs) -> LDAny:
        """Get aggregates objects from Netbox.

        :param kwargs: Finding parameters.

        ================ =================================== =======================================
        Parameter        single-value                        multiple-values
        ================ =================================== =======================================
        prefix           "10.10.0.0/16"                      ["10.10.0.0/16", "10.31.64.0/18"]
        id               93                                  [93, 120]
        q                "10.10.0"                           ["10.10.0", "10.31"]
        tag              "tag1"                              ["tag1", "tag2"]
        family           4                                   [4, 6]
        rir              "rfc-1918"                          ["rfc-1918", "rfc-3927"]
        cf_name          "name1"                             ["name1", "name2"]
        ================ =================================== =======================================

        :return: List of aggregates objects.
        """
        params: LDAny = self._validate_concurrent_params(**kwargs)
        params = self._join_params(*params)
        items: LDAny = self._query_params_ld(params)
        self._check_keys(items=items, denied=self._reserved_ipam_keys)
        return items
