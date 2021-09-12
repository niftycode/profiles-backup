#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Check for old profiles in the backup folder.
Python 3.8+
Author: @niftycode
Date created: February 19th, 2021
Date modified: August 5th, 2021
"""

import getpass
import logging
import os
import shutil

from profiles_backup import common_methods


def sorting(director_name):
    splitup = director_name.split('-')
    return splitup[3], splitup[2], splitup[1]


def delete_old_profiles():

    # Current operating system
    operating_system = common_methods.system_info()

    # Path to the backup directory
    backup_path = common_methods.backup_directory(operating_system)

    # Check if backup directory exists
    if os.path.isdir(backup_path):
        dir_list = os.listdir(backup_path)

        temp_list = []

        for i in dir_list:
            if i.startswith("th"):
                temp_list.append(i)

        temp_list = sorted(temp_list, key=sorting)

        backups_to_delete = len(temp_list) - 5

        for j in temp_list:
            while backups_to_delete > 0:
                print(f"delete backup: {j}")
                backup_to_delete_dir = backup_path + "/" + j
                shutil.rmtree(backup_to_delete_dir)
                backups_to_delete -= 1
                break

    else:
        print("A backup directory doesn't exists. Nothing to clean up!")