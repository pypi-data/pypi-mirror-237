from argparse import ArgumentParser


def create_func_default(func):
    parser = ArgumentParser(add_help=False)

    parser.set_defaults(func=func)

    return parser
