#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Check for old profiles in the backup folder.
Python 3.8+
Author: @niftycode
Date created: February 19th, 2021
Date modified: April 16th, 2021
"""

import os
import shutil
import getpass
import logging

logging.basicConfig(level=logging.DEBUG)


def sorting(director_name):
    splitup = director_name.split('-')
    return splitup[3], splitup[2], splitup[1]


def delete_old_profiles():
    backup_path = '/Users/{0}/Documents/Thunderbird-Backup'.format(getpass.getuser())

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
