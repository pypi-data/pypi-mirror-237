import argparse

import boto3


def main(args: argparse.Namespace):
    sfn_client = boto3.client('stepfunctions')
    pagenator = sfn_client.get_paginator('list_state_machines')
    pages = pagenator.paginate(
        PaginationConfig={
            'MaxItems': args.max_items,
        }
    )
    for page in pages:
        for state_machine in page['stateMachines']:
            print(state_machine['stateMachineArn'])


def add_subparser(subparsers: argparse._SubParsersAction) -> None:  # type: ignore
    parser = subparsers.add_parser('list-state-machines')
    parser.add_argument('--max-items', type=int, default=100)
    parser.set_defaults(handler=main)
