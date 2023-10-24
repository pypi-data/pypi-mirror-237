import importlib.util
from pathlib import Path

parsers_path = Path(__file__).parent


def import_parsers(subparser):
    files = [file for file in parsers_path.iterdir() if not file.name.startswith('_')]
    for file in files:
        spec = importlib.util.spec_from_file_location(file.name, file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        module.register_parser(subparser)
