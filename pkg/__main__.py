from .commands import init, publish, freeze, build
from argparse import ArgumentParser
from . import __version__


def get_parser():
    parser = ArgumentParser(prog='pkg')
    parser.add_argument('--version', action='version', version=__version__)

    subparsers = parser.add_subparsers(dest='command')

    parser_init = subparsers.add_parser('init', help='Create "setup.cfg" file')
    parser_init.set_defaults(func=init)

    parser_build = subparsers.add_parser('build', help='Build the package')
    parser_build.set_defaults(func=build)

    parser_publish = subparsers.add_parser('publish', help='Publish package to PyPi')
    parser_publish.set_defaults(func=publish)

    parser_freeze = subparsers.add_parser('freeze', help='Output only top-level packages in requirements format')
    parser_freeze.set_defaults(func=freeze)

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
