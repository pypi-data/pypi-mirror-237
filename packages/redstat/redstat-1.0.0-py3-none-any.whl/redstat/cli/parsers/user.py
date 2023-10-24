from argparse import ArgumentParser

from redstat.cli.arguments import func, name, output, url
from redstat.cli.arguments import filter
from redstat.functions.download import get_data
from redstat.variables.urls import USER_POSTS_URL, USER_COMMENTS_URL


def _register_comment_parser(subparser, root_parents: list[ArgumentParser]):
    parents = [
        *root_parents,
        url.create_url_template_default(USER_COMMENTS_URL)
    ]
    parser = subparser.add_parser(
        'comments',
        help='download user',
        aliases=['co'],
        parents=parents
    )


def _register_post_parser(subparser, root_parents: list[ArgumentParser]):
    parents = [
        *root_parents,
        url.create_url_template_default(USER_POSTS_URL),
    ]

    parser = subparser.add_parser(
        'post',
        help='download post',
        aliases=['po'],
        parents=parents
    )


def register_parser(subparser):
    parser: ArgumentParser = subparser.add_parser(
        'user',
        help='user manager'
    )
    user_subparser = parser.add_subparsers(required=True)

    parents = [
        name.create_name_argument('user name'),
        func.create_func_default(get_data),
        filter.create_filter_parser(),
        output.create_output_parser()
    ]

    _register_comment_parser(user_subparser, parents)
    _register_post_parser(user_subparser, parents)
