#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Check for old profiles in the backup folder.
Python 3.8+
Date created: February 19th, 2021
Date modified: July 14th, 2022
"""

import os
import shutil

from profiles_backup import common


def sorting(director_name) -> tuple:
    """
    Sorts the directories containing the backed up data.

    Args:
        director_name: Directory conatinaing backed up data.

    Returns: Sorted directories

    """
    splitup = director_name.split("-")
    return splitup[3], splitup[2], splitup[1]


def delete_old_profiles() -> None:
    """
    There should only ever be five saved profiles.
    Older profiles will be deleted.
    """
    # Current operating system
    operating_system = common.system_info()

    # Path to the backup directory
    backup_path = common.backup_directory(operating_system)

    # Check if backup directory exists
    if os.path.isdir(backup_path):
        dir_list = os.listdir(backup_path)

        temp_list = []

        for i in dir_list:
            if i.startswith("th"):
                temp_list.append(i)

        temp_list = sorted(temp_list, key=sorting)
        backups_to_delete = len(temp_list) - 5

        print()
        print("Delete old backups:")
        for j in temp_list:
            while backups_to_delete > 0:
                print(f"deleted backup: {j}")
                backup_to_delete_dir = backup_path + "/" + j
                shutil.rmtree(backup_to_delete_dir)
                backups_to_delete -= 1
                break
    else:
        print("No old backups available. Nothing to clean up!")
