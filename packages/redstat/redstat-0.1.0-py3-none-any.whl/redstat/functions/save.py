from json import dump
from io import TextIOWrapper


def save_json(stream: TextIOWrapper, obj: list):
    with stream:
        dump(obj, stream, ensure_ascii=False, indent=2)
