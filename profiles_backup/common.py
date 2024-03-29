#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Common methods
Python 3.8+
Date created: April 28th, 2020
Date modified: July 14th, 2022
"""

import os
import sys
import getpass
import logging
import platform
import psutil  # type: ignore

logging.basicConfig(level=logging.INFO)


def system_info() -> str:
    """
    Check the running operating system.

    Returns: Operating system (and Windows version).

    """
    operating_system = "None"

    if platform.system() == "Darwin":
        operating_system = "macOS"
    elif platform.system() == "Linux":
        operating_system = "Linux"
    elif platform.system() == "Windows":
        operating_system = platform.system() + " " + platform.release()

    return operating_system


def check_default_profile() -> tuple:
    """
    Call functions to check the operating system, Thunderbird's directory and
    the path to the user's default-release directory.
    :return: A tuple containing the OS, Thunderbird's Profiles folder and
    the user's xyz.default-release folder.
    """

    operating_system = system_info()
    thunderbird_dir = thunderbird_directory(operating_system)
    default_release_dir = default_release_directory(operating_system)

    logging.debug(f"OS: {operating_system}")
    logging.debug(f"Thunderbird directory: {thunderbird_dir}")
    logging.debug(f"Profiles directory: {default_release_dir}")

    return operating_system, thunderbird_dir, default_release_dir


def show_default_path():
    """
    Invoke check_default_profile() to get the operating system and
    the default directory. Show this information.
    """
    operating_system, _, default_folder = check_default_profile()

    print()
    print("--------------------------------------------------------------")
    print(f"You are running a {operating_system} system.")
    print("Your default profile directory is located in:")
    print(f"{default_folder}")
    print("--------------------------------------------------------------")
    print()


def thunderbird_directory(installed_os) -> str:
    """
    Get the path to the Thunderbird directory

    Args:
        installed_os: The installed operating system

    Returns: Thunderbird's directory

    """
    platform_paths = {
        "Windows 10": "C:\\Users\\{0}\\AppData\\Local\\Thunderbird\\".format(
            getpass.getuser()
        ),
        "Linux": "/home/{0}/.thunderbird/".format(getpass.getuser()),
        "Darwin": "/Users/{0}/Library/Thunderbird/".format(getpass.getuser()),
    }

    if installed_os == "macOS":
        thunderbird_path = platform_paths["Darwin"]
    elif installed_os == "Linux":
        thunderbird_path = platform_paths["Linux"]
    else:
        thunderbird_path = platform_paths["Windows 10"]

    return thunderbird_path


def default_release_directory(installed_os):
    """
    Get the path to the default-release directory.
    This is the default profile located in the Profiles directory.

    Args:
        installed_os: The installed operating system.

    Returns: The path to the default-release directory.

    """
    platform_paths = {
        "Windows 10": "C:\\Users\\{0}\\AppData\\Local\\Thunderbird\\Profiles\\".format(
            getpass.getuser()
        ),
        "Linux": "/home/{0}/.thunderbird/".format(getpass.getuser()),
        "Darwin": "/Users/{0}/Library/Thunderbird/Profiles/".format(getpass.getuser()),
    }

    if installed_os == "macOS":
        profiles_path = platform_paths["Darwin"]
    elif installed_os == "Linux":
        profiles_path = platform_paths["Linux"]
    else:
        profiles_path = platform_paths["Windows 10"]

    try:
        for item in os.listdir(profiles_path):
            if (
                os.path.isdir(os.path.join(profiles_path, item))
                and "default-release" in item
            ):
                return os.path.join(profiles_path)  # Path to the default-release dir
    except FileNotFoundError as e:
        print(e)
        sys.exit(
            "Thunderbird's Profiles directory could not be found!\n"
            "Are you sure Thunderbird is installed on this system?"
        )


def backup_directory(installed_os) -> str:
    """
    Get the path to the backup directory depending on the operating system.

    Args:
        installed_os: The installed operating system

    Returns: The backup directory located in the user's Documents directory.

    """
    platform_paths = {
        "Windows 10": "C:\\Users\\{0}\\Documents\\Thunderbird-Backup\\".format(
            getpass.getuser()
        ),
        "Linux": "/home/{0}/Documents/Thunderbird-Backup/".format(getpass.getuser()),
        "Darwin": "/Users/{0}/Documents/Thunderbird-Backup/".format(getpass.getuser()),
    }

    if installed_os == "macOS":
        backup_path = platform_paths["Darwin"]
    elif installed_os == "Linux":
        backup_path = platform_paths["Linux"]
    else:
        backup_path = platform_paths["Windows 10"]

    return backup_path


def documents_directory(installed_os):
    """
    Get the path to the user's Documents directory
    depending on the operating system.

    Args:
        installed_os: The installed operating system

    Returns: The user's Documents directory

    """
    platform_paths = {
        "Windows 10": "C:\\Users\\{0}\\Documents\\".format(getpass.getuser()),
        "Linux": "/home/{0}/Documents/".format(getpass.getuser()),
        "Darwin": "/Users/{0}/Documents/".format(getpass.getuser()),
    }

    if installed_os == "macOS":
        directory_path = platform_paths["Darwin"]
    elif installed_os == "Linux":
        directory_path = platform_paths["Linux"]
    else:
        directory_path = platform_paths["Windows 10"]

    return directory_path


def check_process() -> bool:
    """
    Check if Thunderbird is running

    Returns: True (running) or False (not running)

    """
    return "thunderbird" in (p.name() for p in psutil.process_iter())


def quit_application():
    """Quit the application."""
    print("Goodbye!")
    sys.exit()
