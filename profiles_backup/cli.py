#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Backup Thunderbird's Profiles Folder
Python 3.8+
Author: @niftycode
Date created: April 25th, 2020
Date modified: July 14th, 2022
"""

import argparse
import logging

from argparse import Namespace

from profiles_backup import common, info, backup, restore

logging.basicConfig(level=logging.DEBUG)


# TODO: Delete in upcoming version
'''
class Args(NamedTuple):
    """Command-line arguments"""

    path: bool
    backup: bool
    restore: bool
    version: bool
'''


def create_parser() -> argparse.ArgumentParser:
    """
    Create a command-line parser

    Returns: parser
    """
    parser = argparse.ArgumentParser(
        description="Backup Thunderbird's profiles directory.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-p",
        "--path",
        help="show the path of the default profile",
        action="store_true",
    )

    parser.add_argument(
        "-b", "--backup", help="backup the profiles directory", action="store_true"
    )

    parser.add_argument(
        "-r", "--restore", help="restore the profiles directory", action="store_true"
    )

    parser.add_argument(
        "-v", "--version", help="show the current version.", action="store_true"
    )

    return parser


def evaluate_arguments(args: Namespace):
    """
    Evaluate the given argument
    Args:
        args: given arguments
    """
    if args.path:
        common.show_default_path()

    if args.backup:
        backup.backup()

    if args.restore:
        restore.restore_from_documents()

    if args.version:
        info.app_info()


def main():
    """
    The entry point of this program.
    """
    parser = create_parser()
    args = parser.parse_args()
    evaluate_arguments(args)


if __name__ == "__main__":
    main()
