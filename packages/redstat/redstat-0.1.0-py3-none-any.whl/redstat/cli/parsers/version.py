from argparse import ArgumentParser

from redstat.cli.arguments import func
from redstat.functions.version import get_version


def register_parser(subparser):
    parents = [
        func.create_func_default(get_version)
    ]
    parser: ArgumentParser = subparser.add_parser('version', help='get version', parents=parents)

    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '-n', '--name-only',
        help='Show application name',
        action='store_true'
    )
    group.add_argument(
        '-d', '--digit-only',
        help='Show version only',
        action='store_true'
    )
