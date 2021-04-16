#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Check for old profiles in the backup folder.
Python 3.8+
Author: @niftycode
Date created: February 19th, 2021
Date modified: February 25th, 2021
"""

import os
import getpass
import logging
from pathlib import Path

logging.basicConfig(level=logging.DEBUG)


def delete_old_profiles():
    backup_path = '/Users/{0}/Documents/Thunderbird-Backup'.format(getpass.getuser())
    paths = sorted(Path(backup_path).iterdir(), key=os.path.getmtime)

    for i in paths:
        if i.name.startswith("th"):
            print(i.name)
