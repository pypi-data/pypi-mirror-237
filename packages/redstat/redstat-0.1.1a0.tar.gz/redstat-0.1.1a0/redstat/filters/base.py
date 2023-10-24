from typing import Generator


class Filter:
    @staticmethod
    def filter(data: Generator[dict, None, None], fields: list[str]) -> list[dict]: ...
