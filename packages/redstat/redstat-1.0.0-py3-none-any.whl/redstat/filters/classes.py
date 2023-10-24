from typing import Generator

from redstat.filters.base import Filter
from redstat.filters.factory import FilterFactory


@FilterFactory.register_filter('include')
class IncludeFilter(Filter):
    @staticmethod
    def filter(data: Generator[dict, None, None], fields: list[str]) -> list[dict]:
        return [{field: child.pop(field, None) for field in fields} for child in data]


@FilterFactory.register_filter('exclude')
class ExcludeFilter(Filter):
    @staticmethod
    def filter(data: Generator[dict, None, None], fields: list[str]) -> list[dict]:
        result = []
        for child in data:
            for field in fields:
                child.pop(field, None)
            result.append(child)
        return result


@FilterFactory.register_filter(None)
class NotFilter(Filter):
    @staticmethod
    def filter(data: Generator[dict, None, None], fields: list[str]) -> list[dict]:
        return list(data)
