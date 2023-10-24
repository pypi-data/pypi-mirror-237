from argparse import ArgumentParser

from redstat.cli.arguments import func, name, output, url
from redstat.cli.arguments import filter
from redstat.functions.download import get_data
from redstat.variables.urls import SUBREDDIT_URL


def register_parser(subparser):
    parents = [
        name.create_name_argument('subreddit name'),
        func.create_func_default(get_data),
        url.create_url_template_default(SUBREDDIT_URL),
        output.create_output_parser(),
        filter.create_filter_parser()
    ]
    parser: ArgumentParser = subparser.add_parser(
        'subreddit',
        help='subreddit manager',
        aliases=['sub'],
        parents=parents
    )
