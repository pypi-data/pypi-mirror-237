from argparse import ArgumentParser


def create_url_template_default(url_template):
    parser = ArgumentParser(add_help=False)

    parser.set_defaults(url_template=url_template)

    return parser
