import argparse
import inspect

from . import cmd


def parse_args() -> tuple[argparse.ArgumentParser, argparse.Namespace]:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    add_subparsers = [
        fn
        for name, fn in inspect.getmembers(cmd, inspect.isfunction)
        if name.startswith('add_subparser_')
    ]

    for add_subparser in add_subparsers:
        add_subparser(subparsers)

    return parser, parser.parse_args()

def main() -> None:
    parser, args = parse_args()

    if hasattr(args, 'handler'):
        args.handler(args)
        return

    parser.print_help()
