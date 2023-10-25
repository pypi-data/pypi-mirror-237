import argparse
import csv
import datetime as dt
from datetime import date, datetime
import sys
from typing import Any, Optional

import boto3


def main(args: argparse.Namespace):
    sfn_client = boto3.client('stepfunctions')
    pagenator = sfn_client.get_paginator('list_executions')
    pages = pagenator.paginate(
        stateMachineArn=args.state_machine_arn,
        PaginationConfig={
            'MaxItems': args.max_items,
        }
    )

    obj: list[dict[str, Any]] = []
    for page in pages:
        for execution in page['executions']:
            obj.append({
                'name': execution['name'],
                'status': execution['status'],
                'start_date': execution['startDate'],
                'stop_date': execution.get('stopDate'),
                'duration': execution.get('stopDate') - execution['startDate'] if execution.get('stopDate') else '',
            })

    writer = csv.DictWriter(sys.stdout, obj[0].keys())
    writer.writeheader()
    def fmt(x: Any, timespec: str = 'milliseconds') -> str:
        if isinstance(x, datetime):
            return x.isoformat(timespec=timespec)
        if isinstance(x, date):
            return x.isoformat()
        if isinstance(x, dt.timedelta):
            x_mod = x - dt.timedelta(microseconds=x.microseconds)
            return str(x_mod)
        if x is None:
            return ''
        return str(x)

    for row_ in obj:
        row = {
            k: fmt(v, timespec='seconds')
            for k, v in row_.items()
        }
        writer.writerow(row)


def add_subparser(subparsers: argparse._SubParsersAction) -> None:  # type: ignore
    parser = subparsers.add_parser('list-executions')
    parser.add_argument('--state-machine-arn', required=True)
    parser.add_argument('--max-items', type=int, default=100)
    parser.set_defaults(handler=main)
