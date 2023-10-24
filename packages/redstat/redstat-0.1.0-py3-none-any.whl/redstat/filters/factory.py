from typing import Type

from redstat.filters.base import Filter


class FilterFactory:
    _filters_map = {}

    @classmethod
    def register_filter(cls, name):
        def wrapper(filter_class):
            cls._filters_map[name] = filter_class

        return wrapper

    @classmethod
    def get(cls, filter_type: str | None) -> Type[Filter] | None:
        return cls._filters_map.get(filter_type, None)
