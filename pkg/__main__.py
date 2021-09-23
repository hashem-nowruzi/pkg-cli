from .commands import init, publish
from argparse import ArgumentParser
from . import __version__


def get_parser():
    parser = ArgumentParser(prog='pkg')
    parser.add_argument('--version', action='version', version=__version__)

    subparsers = parser.add_subparsers(dest='command')
    parser_init = subparsers.add_parser('init', help='Create "package.json" file')
    parser_init.set_defaults(func=init)
    parser_publish = subparsers.add_parser('publish', help='Publish package to PyPi')
    parser_publish.set_defaults(func=publish)

    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    if args.command is None:
        parser.parse_args(['-h'])
    else:
        args.func(args)


if __name__ == '__main__':
    main()
