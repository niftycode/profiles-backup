#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Check for old profiles in the backup folder.
Python 3.8+
Author: @niftycode
Date created: February 19th, 2021
Date modified: -
"""

import os
import getpass
from stat import S_ISDIR, ST_ATIME, ST_MODE


def delete_old_profiles():
    desktop = '/Users/{0}/Desktop/Thunderbird-Backup'.format(getpass.getuser())

    # Get all entries in the directory
    entries = (os.path.join(desktop, file_name) for file_name in os.listdir(desktop))

    # for entry in entries:
    #     print(entry)

    # Get their stats
    entries = ((os.stat(path), path) for path in entries)

    # leave only regular files, insert creation date
    entries = ((stat[ST_ATIME], path)
               for stat, path in entries if S_ISDIR(stat[ST_MODE]))

    sorted_list = sorted(entries, key=lambda x: x[0])

    for i in sorted_list:
        print(i)
