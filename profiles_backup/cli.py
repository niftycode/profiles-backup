#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Backup Thunderbird's Profiles Folder
Python 3.8+
Date created: April 25th, 2020
Date modified: June 25th, 2022
"""

import argparse
import logging

from typing import NamedTuple

from profiles_backup import common, info, backup

logging.basicConfig(level=logging.DEBUG)


class Args(NamedTuple):
    """Command-line arguments"""
    path: bool
    backup: bool
    restore: bool
    version: bool


def user_input():
    """
    Check user input
    """
    print()
    print("----------------------------------------------------------")
    print("What do you want to do?")
    print()
    print("-1- Show the path of the default profile")
    print("-2- Backup the default profile")
    print("-3- Restore the default profile")
    print("-4- Show version")
    print("-5- Quit the application")
    print("----------------------------------------------------------")

    while True:
        choice = input("Your choice: ")

        if choice == "1":
            show_default_path()
            break
        elif choice == "2":
            backup()
            break
        elif choice == "3":
            restore_from_documents()
            break
        elif choice == "4":
            info.app_info()
            break
        elif choice == "5":
            quit_application()

        else:
            print("Unknown input! Try again.")
            continue


def get_arguments() -> Args:
    """
    Get command-line arguments
    Returns: arguments
    """
    parser = argparse.ArgumentParser(
        description="Backup Thunderbird's profiles directory.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "-p",
        "--path",
        help="Show the path of the default profile.",
        action="store_true"
    )

    parser.add_argument(
        "-b",
        "--backup",
        help="Backup the profiles directory.",
        action="store_true"
    )

    parser.add_argument(
        "-r",
        "--restore",
        help="Restore the profiles directory.",
        action="store_true"
    )

    parser.add_argument(
        "-v",
        "--version",
        help="Show the current version.",
        action="store_true"
    )

    args = parser.parse_args()

    return Args(
        path=args.path,
        backup=args.backup,
        restore=args.restore,
        version=args.version
    )


def main():
    """
    The entry point of this program.
    """
    args = get_arguments()
    logging.debug(args)

    if args.path:
        common.show_default_path()

    if args.backup:
        backup.backup()

    if args.restore:
        logging.debug("invoke restore")

    if args.version:
        info.app_info()


if __name__ == "__main__":
    main()
