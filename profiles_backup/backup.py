#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Backup Thunderbird's Profiles Folder
Python 3.8+
Date created: July 14th, 2022
Date modified: -
"""

import sys
import logging
import datetime
import shutil

from profiles_backup import common, clean_data

logging.basicConfig(level=logging.DEBUG)


def backup():
    """
    If necessary, create the "Thunderbird-Backup" directory in the user's
    Documents directory and copy all user data into this directory.
    The default directory can be recognized by the 'default-release' suffix.
    """

    # Check if thunderbird is running
    is_running = common.check_process()
    if is_running:
        print("Thunderbird is running! Quit Thunderbird and restart this program.")
        sys.exit()

    # Get the path of the source folder (Thunderbird folder)
    _, _, src = common.check_default_profile()
    logging.debug(f"Source folder: {src}")

    # Get current date and time
    current_date = datetime.datetime.now()

    # Current operating system
    operating_system = common.system_info()

    # Path to the Documents directory
    documents = common.documents_directory(operating_system)

    backup_folder = "Thunderbird-Backup/"
    dst = documents + backup_folder + "th-" + current_date.strftime("%d-%m-%Y")

    logging.debug(dst)

    try:
        shutil.copytree(
            src,
            dst,
            dirs_exist_ok=True,
            symlinks=False,
            ignore=shutil.ignore_patterns("*.ini", "*.default"),
        )
    except OSError as e:
        print(f"Creation of the directory {dst} failed")
        print(f"Error message: {e}")
        sys.exit("Program terminated!")
    else:
        print("Successfully created the backup!")
        print(f"You can find the backup data in {dst}")

    # Check for old Backups and delete them
    clean_data.delete_old_profiles()
