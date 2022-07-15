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

from typing import NamedTuple

from profiles_backup import common, info, backup, restore

logging.basicConfig(level=logging.INFO)


class Args(NamedTuple):
    """Command-line arguments"""

    path: bool
    backup: bool
    restore: bool
    version: bool


def get_arguments() -> Args:
    """
    Get command-line arguments

    Returns: arguments
    """
    parser = argparse.ArgumentParser(
        description="Backup Thunderbird's profiles directory.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-p",
        "--path",
        help="Show the path of the default profile.",
        action="store_true",
    )

    parser.add_argument(
        "-b", "--backup", help="Backup the profiles directory.", action="store_true"
    )

    parser.add_argument(
        "-r", "--restore", help="Restore the profiles directory.", action="store_true"
    )

    parser.add_argument(
        "-v", "--version", help="Show the current version.", action="store_true"
    )

    args = parser.parse_args()

    return Args(
        path=args.path, backup=args.backup, restore=args.restore, version=args.version
    )


def main():
    """
    The entry point of this program.
    """
    args = get_arguments()

    if args.path:
        common.show_default_path()

    if args.backup:
        backup.backup()

    if args.restore:
        restore.restore_from_documents()

    if args.version:
        info.app_info()


if __name__ == "__main__":
    main()
