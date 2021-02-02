# -*- mode:python; coding:utf-8 -*-

# Copyright (c) 2020 IBM Corp. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Top level script for running trestle assemble on every file.

The purpose of this is to act as a naive validation script.
"""
import sys
import pathlib
from unittest import mock
from trestle.cli import Trestle


subcommand_list = [
    'catalog',
    'profile',
    'target-definition',
    'component-definition',
    'system-security-plan',
    'assessment-plan',
    'assessment-results',
    'plan-of-action-and-milestones'
]

def run_all_files():
    """Not the efficient way to do this."""
    testargs_root = ['trestle', 'assemble']
    sub_directories = list(map(lambda x: x if x[-1] == 's' else x + 's', subcommand_list))
    for command in subcommand_list:    
        directory = command if command[-1] == 's' else command + 's'
        dir_path = pathlib.Path(directory)
        for case in dir_path.iterdir():
            case_name = case.stem
            if case_name[0] == '.':
                continue
            print(case_name)
            test_args = testargs_root + [command] + ['-n', case_name]
            with mock.patch.object(sys, 'argv', test_args):
                rc = Trestle().run()
                if rc != 0:
                    print('Error')
                    print(f'command: {command}')
                    print(f'case: {case_name}')
                    assert 0 == 1

if __name__ == '__main__':
    run_all_files()