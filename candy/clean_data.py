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
from pathlib import Path

logging.basicConfig(level=logging.DEBUG)


def delete_old_profiles():
    backup_path = '/Users/{0}/Documents/Thunderbird-Backup'.format(getpass.getuser())
    paths = sorted(Path(backup_path).iterdir(), key=os.path.getctime)

    temp_paths = []

    for i in paths:
        if i.name.startswith("th"):
            temp_paths.append(i)

    for k in temp_paths:
        print(k)

    backups_to_delete = len(temp_paths) - 5
    print(backups_to_delete)

    for j in temp_paths:
        while backups_to_delete > 0:
            print(f"backup to delete: {j.name}")
            backup_dir = backup_path + "/" + j.name
            # shutil.rmtree(backup_dir)
            backups_to_delete -= 1
