#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Common methods
Python 3.7+
Date created: April 28th, 2020
Date modified: September 27th, 2020
"""

import os
import sys
import platform
import getpass
import psutil


def system_info():
    """
    Check the running operating system.
    :return: Operating system name (and Windows version).
    """
    if platform.system() == 'Darwin':
        return 'macOS'
    elif platform.system() == 'Linux':
        return 'Linux'
    elif platform.system() == 'Windows':
        version = platform.system() + " " + platform.release()
        return version


def profiles_folder(installed_os):
    """
    Returns the path to Thunderbird's profiles folder
    depending on the operating system.
    :param installed_os: The installed operating system
    :return: Thunderbird's profiles folder
    """
    platform_paths = {
        'Windows 10': 'C:\\Users\\{0}\\AppData\\Local\\Thunderbird\\'.format(getpass.getuser()),
        'Linux': '/home/{0}/.thunderbrid/'.format(getpass.getuser()),
        'Darwin': '/Users/{0}/Library/Thunderbird/'.format(getpass.getuser())}

    if installed_os == 'macOS':
        profiles_path = platform_paths['Darwin']
    elif installed_os == 'Linux':
        profiles_path = platform_paths['Linux']
    else:
        profiles_path = platform_paths['Windows 10']

    return profiles_path


def check_default_folder(profiles_path):
    """
    Check for the path of the user's Profiles folder
    :param profiles_path: The expected path of Thunderbird's profile folder
    :return: The path of the Profiles folder
    """

    try:
        for item in os.listdir(profiles_path):
            if os.path.isdir(os.path.join(profiles_path, item)) and 'Profiles' in item:
                return os.path.join(profiles_path, item)
    except FileNotFoundError as e:
        print(e)
        sys.exit(
            "Could not find Thunderbird's Profiles folder!\n "
            "Are you sure Thunderbird is installed on this system?"
        )


def check_process() -> bool:
    """
    Check if Thunderbird is running
    :return: 'true' or 'false'
    """
    return "thunderbird" in (p.name() for p in psutil.process_iter())


def check_old_backups():
    pass
