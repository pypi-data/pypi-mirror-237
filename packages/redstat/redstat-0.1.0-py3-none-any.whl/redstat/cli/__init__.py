from argparse import ArgumentParser

from redstat.cli.parsers import import_parsers
from redstat.variables.application import APPLICATION_NAME


def parse_args():
    parser = ArgumentParser(prog=APPLICATION_NAME)
    subparser = parser.add_subparsers(required=True)

    import_parsers(subparser)

    return parser.parse_args()
