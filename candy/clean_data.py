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
from stat import S_ISDIR, ST_ATIME, ST_MODE

logging.basicConfig(level=logging.DEBUG)


def last_4chars(x):
    return x[-2:]


def delete_old_profiles():
    documents = '/Users/{0}/Documents/Thunderbird-Backup'.format(getpass.getuser())
    logging.debug(documents)

    dir_list = os.listdir(documents)
    print(dir_list)

    # th-02-Feb-2021_14.42
    # grab last 4 characters of the file name:

    # for i in dir_list:

    new_list = sorted(dir_list, key=last_4chars)
    for i in new_list:
        print(i)


    """
    documents = '/Users/{0}/Documents/Thunderbird-Backup'.format(getpass.getuser())

    # Get all entries in the directory
    entries = (os.path.join(documents, file_name) for file_name in os.listdir(documents))

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
    """
