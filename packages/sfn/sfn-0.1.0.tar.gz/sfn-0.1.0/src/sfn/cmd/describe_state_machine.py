import argparse
import csv
import datetime as dt
from datetime import date, datetime
import json
import sys
from typing import Any, Optional

import boto3


def main(args: argparse.Namespace):
    sfn_client = boto3.client('stepfunctions')
    res = sfn_client.describe_state_machine(
        stateMachineArn=args.state_machine_arn,
    )
    print(json.dumps(res, default=str, indent=2))


def add_subparser(subparsers: argparse._SubParsersAction) -> None:  # type: ignore
    parser = subparsers.add_parser('describe-state-machine')
    parser.add_argument('--state-machine-arn', required=True)
    parser.set_defaults(handler=main)
