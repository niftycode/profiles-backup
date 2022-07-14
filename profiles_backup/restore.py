#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Restore Thunderbird's Profiles Folder
Python 3.8+
Date created: July 13th, 2022
Date modified: -
"""

import os
import sys
import shutil
import getpass
import logging

from profiles_backup import common

logging.basicConfig(level=logging.DEBUG)


def restore_from_documents():
    """
    Check if Thunderbird is not running,
    show available backups and
    let the user chose a saved profile folder.
    (Invoke the 'restore_data()' function.)
    """
    is_running = common.check_process()
    if is_running:
        print("Thunderbird is running! Quit Thunderbird and restart this program.")
        return

    documents = "/Users/{0}/Documents/Thunderbird-Backup".format(getpass.getuser())

    try:
        entries = os.listdir(documents)
        print(f"entries: {entries}")
        count = 1
        backup_list = []
        for entry in entries:
            if entry.startswith("t"):
                backup_list.append(f"-{count}- {entry}")
                count += 1

        backup_list.append("-q- Quit")

        print()
        print("----------------------------------------------------------")
        print("Select the backup you want to restore:")
        print()
        for item in backup_list:
            print(item)
        print("----------------------------------------------------------")

        while True:
            choice = input("Your choice: ")

            if choice == "1":
                restore_data(backup_list[0])
                break
            elif choice == "2":
                restore_data(backup_list[1])
                break
            elif choice == "3":
                restore_data(backup_list[2])
                break
            elif choice == "4":
                restore_data(backup_list[3])
                break
            elif choice == "5":
                restore_data(backup_list[4])
                break
            elif choice == "q":
                common.quit_application()
            else:
                print("Unknown input! Try again.")
                continue

    except FileNotFoundError as e:
        print(f"Error message: {e}")
        sys.exit(
            "Could not find a directory named 'Thunderbird-Backup'!\n "
            "(The backed up profiles must be located in a directory named 'Thunderbird-Backup'.)"
        )


def restore_data(backup_item: str) -> None:
    """Restore a backuped Profiles folder.

    Args:
        backup_item (str): The name of the folder, saved
        in the directory 'Thunderbird-Backup'.
    """
    logging.debug("Restore data...")
    logging.debug(f"Backup: {backup_item}")

    # Get the path of the source folder
    documents = "/Users/{0}/Documents/Thunderbird-Backup/".format(getpass.getuser())
    src = documents + backup_item[4:]
    logging.debug(f"Source folder: {src}")

    # Get the path of the destination directory
    # (Thunderbird's Profiles directory)
    _, _, dst = common.check_default_profile()

    try:
        print(f"Source directory: {src}")
        shutil.copytree(src,
                        dst,
                        dirs_exist_ok=True,
                        copy_function=shutil.copy2,
                        symlinks=False)
    except OSError as e:
        print(f"Cannot restore data to destination directory: {dst}")
        print(f"Error message: {e}")
        sys.exit("Program terminated!")
    else:
        print()
        print("------------------------------------------------------------")
        print("Successfully restored the data!")
        print(f"You can find the restored data in {dst}")
        print("------------------------------------------------------------")

