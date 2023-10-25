import argparse
import csv
import datetime as dt
from datetime import date, datetime
import json
import re
import sys
from typing import Any, Optional

import boto3

from .. import util


def main(args: argparse.Namespace):
    obj = json.loads(sys.stdin.read())

    print('digraph {')
    print('node [shape=box, margin="0.3,0"];')
    print('node [fontname="Helvetica,Arial,sans-serif"];')
    print('edge [fontname="Helvetica,Arial,sans-serif"];')
    print('START [shape=ellipse];')
    print('END [shape=doublecircle, margin=0.05];')
    print(f'START -> {obj["StartAt"]}')

    for state_name, state_body in obj['States'].items():
        regexp = r'arn:aws:states:::(?P<service>[^:]+):(?P<action>[^:]+)'
        if (m := re.match(regexp, state_body.get('Resource', ''))):
            service = m.group('service')
            action = m.group('action')
            print(f'{state_name} [label=<<FONT POINT-SIZE="10" COLOR="gray40">{service}.{action}</FONT><BR />{state_name}>]')
            if icon := util.asset.aws_icon.aws_icon(service):
                print(f'{state_name} [image="{icon}", imagepos="tl"]')

        else:
            print(f'{state_name} [label=<<FONT POINT-SIZE="10" COLOR="gray40">{state_body["Type"]}</FONT><BR />{state_name}>]')

        if state_body['Type'] == 'Pass':
            pass

        elif state_body['Type'] == 'Task':
            pass

        elif state_body['Type'] == 'Choice':
            for choice in state_body['Choices']:
                print(f'{state_name} -> {choice["Next"]}')
            if state_body.get('Default'):
                print(f'{state_name} -> {state_body["Default"]}[style="bold"]')

        elif state_body['Type'] == 'Wait':
            pass

        elif state_body['Type'] == 'Succeed':
            print(f'{state_name} -> END')

        elif state_body['Type'] == 'Fail':
            pass

        elif state_body['Type'] == 'Parallel':
            pass

        elif state_body['Type'] == 'Map':
            pass

        if state_body.get('End'):
            print(f'{state_name} -> END')

        if state_body.get('Next'):
            print(f'{state_name} -> {state_body["Next"]}')

        if state_body.get('Catch'):
            for catch in state_body['Catch']:
                print(f'{state_name} -> {catch["Next"]}[style="dashed"]')

    print('}')


def add_subparser(subparsers: argparse._SubParsersAction) -> None:  # type: ignore
    parser = subparsers.add_parser('state-machine-graph')
    parser.set_defaults(handler=main)
