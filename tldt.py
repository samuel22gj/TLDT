#!/usr/bin/env python3

"""
Copyright 2020 Samuel Huang

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import argparse
import json
import os
import sys
from datetime import datetime, timedelta

VERSION = 'v1.0.0'

JSON_FILENAME = '.tldt.json'
JSON_NAME_KEY = 'key'
JSON_NAME_DESC = 'description'
JSON_NAME_CMD = 'command'

ACTION_KEY_QUIT = 'q'


def show_action_table(actions: list):
    max_key_len = len(JSON_NAME_KEY)
    max_desc_len = len(JSON_NAME_DESC)
    max_cmd_len = len(JSON_NAME_CMD)

    for action in actions:
        max_key_len = max(max_key_len, len(action[JSON_NAME_KEY]))
        max_desc_len = max(max_desc_len, len(action[JSON_NAME_DESC]))
        max_cmd_len = max(max_cmd_len, len(action[JSON_NAME_CMD]))

    print(f'{JSON_NAME_KEY:^{max_key_len}} | {JSON_NAME_DESC:^{max_desc_len}} | {JSON_NAME_CMD:^{max_cmd_len}}')
    print(f'{"-" * max_key_len}-+-{"-" * max_desc_len}-+-{"-" * max_cmd_len}')
    for action in actions:
        action_key = action[JSON_NAME_KEY]
        action_desc = action[JSON_NAME_DESC]
        action_cmd = action[JSON_NAME_CMD]
        print(f'{action_key:>{max_key_len}} | {action_desc:<{max_desc_len}} | {action_cmd:<{max_cmd_len}}')


def show_execution_time_info(start_time: datetime, end_time: datetime):
    print('   Execution Time Information')
    print('=================================')
    datetime_format = '%Y-%m-%d %H:%m:%S'
    print(f'  Start Time: {start_time.strftime(datetime_format)}')
    print(f'    End Time: {end_time.strftime(datetime_format)}')
    elapsed_time = end_time - start_time
    print(f'Elapsed Time: {str(timedelta(days=elapsed_time.days, seconds=elapsed_time.seconds)):>19}')


def main():
    # Check file exists
    if not os.path.exists(JSON_FILENAME):
        print(f'ERROR: {JSON_FILENAME} not exist.')
        sys.exit(1)

    # Parse file
    with open(JSON_FILENAME, 'r') as f:
        try:
            tldt = json.load(f)
        except:
            print(f'ERROR: Parsing {JSON_FILENAME} failed.')
            sys.exit(1)

    # Check "actions" node exists and at least one action
    actions = tldt['actions']
    if type(actions) is not list or len(actions) < 1:
        print(f'ERROR: There is no action.')
        sys.exit(1)

    # Parse "configuration"
    sort_by_key = False
    if 'configuration' in tldt:
        configuration = tldt['configuration']
        if configuration['sortByKey'] is True:
            sort_by_key = True

    # Parse argument
    parser = argparse.ArgumentParser(prog='tldt', description="Too Long; Didn't Type.")
    parser.add_argument('--version', '-v', action='version', version=f'TLDT {VERSION}')
    parser.add_argument('--no-time', '-nt', action='store_true', help="don't show execution time information")
    parser.add_argument('key', type=str, nargs='?', help='a key of the action')
    args = parser.parse_args()
    # print(args)

    if args.key:
        # Take the key from argument
        key = args.key
    else:
        # Sort action by key if need
        if sort_by_key:
            actions = sorted(actions, key=lambda act: act[JSON_NAME_KEY], reverse=False)

        show_action_table(actions)

        # Take the key from user input
        key = input(f'\nEnter the key of action to be executed ("{ACTION_KEY_QUIT}" to quit): ')

    # Quit program if the key is quit key
    if key.lower() == ACTION_KEY_QUIT:
        sys.exit()

    # Find action
    try:
        action = next(d for i, d in enumerate(actions) if d[JSON_NAME_KEY] == key)
    except:
        print('ERROR: Action not found.')
        sys.exit(1)

    # Record start time if need
    if not args.no_time:
        start_time = datetime.now()

    # Execute action
    print(f'Start >> [{action[JSON_NAME_KEY]}] {action[JSON_NAME_DESC]} >> {action[JSON_NAME_CMD]}')
    os.system(action[JSON_NAME_CMD])
    print(f'End   >> [{action[JSON_NAME_KEY]}] {action[JSON_NAME_DESC]} >> {action[JSON_NAME_CMD]}')

    # Show execution time information if need
    if not args.no_time:
        end_time = datetime.now()
        print('')
        show_execution_time_info(start_time, end_time)


if __name__ == '__main__':
    main()
