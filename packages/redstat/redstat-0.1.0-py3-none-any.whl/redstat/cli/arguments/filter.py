from argparse import ArgumentParser


def create_filter_parser():
    parser = ArgumentParser(add_help=False)

    filter_type_help = """select filter type:
    1. include - save only selected fields
    2. exclude - save all fields except selected"""

    choice_list = ('include', 'exclude')

    group = parser.add_argument_group(title='Filter argument')
    group.add_argument(
        '-ft', '--filter-type',
        help=filter_type_help,
        choices=choice_list
    )
    group.add_argument(
        '-f', '--fields',
        help='selected fields',
        default=[],
        nargs='+'
    )

    return parser
