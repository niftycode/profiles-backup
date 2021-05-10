#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Backup Thunderbird's Profiles Folder
Python 3.8+
Author: @niftycode
Date created: April 25th, 2020
Date modified: May 10th, 2021
"""

import sys
import os
import getpass
import shutil
import datetime
import logging
from distutils.dir_util import copy_tree
from profiles_backup import common_methods
from profiles_backup import info
from profiles_backup import clean_data

logging.basicConfig(level=logging.DEBUG)


def check_default_profile():
    """
    Call functions to check the operating system, the profiles folder and
    the path to the user's default folder.
    :return: A tuple containing the OS, Thunderbird's Profiles folder and
    the user's xyz.default folder.
    """
    operating_system = common_methods.system_info()
    profiles_folder = common_methods.profiles_folder(operating_system)
    default_folder = common_methods.check_default_folder(profiles_folder)

    logging.debug(operating_system)
    logging.debug(profiles_folder)
    logging.debug(default_folder)

    return operating_system, profiles_folder, default_folder


def show_default_path():
    common_methods.check_process()
    operating_system, _, default_folder = check_default_profile()

    print()
    print("--------------------------------------------------------------")
    print(f"You are running a {operating_system} system.")
    print("Your default profiles folder is located in:")
    print(f"{default_folder}")
    print("--------------------------------------------------------------")
    print()


def backup():

    # Check if thunderbird is running
    is_running = common_methods.check_process()
    if is_running:
        print("Thunderbird is running! Quit Thunderbird and restart this program.")
        sys.exit()

    # Check for old Backups and delete them
    clean_data.delete_old_profiles()

    # Get the path of the source folder (Thunderbird folder)
    _, src, _ = check_default_profile()
    logging.debug(f"Source folder: {src}")

    # Just for debugging...
    # default_folder = os.path.basename(os.path.normpath(src))
    # logging.debug(default_folder)

    # Get current date and time
    current_date = datetime.datetime.now()

    backup_folder = 'Thunderbird-Backup/'
    dst = '/Users/{0}/Documents/{1}/'.format(getpass.getuser(),
                                             backup_folder + 'th-' +
                                             current_date.strftime('%d-%m-%Y'))

    logging.debug(dst)

    try:
        shutil.copytree(src, dst, dirs_exist_ok=True, symlinks=False)
    except OSError as e:
        print(f"Creation of the directory {dst} failed")
        print(f"Error message: {e}")
        sys.exit("Program terminated!")
    else:
        print("Successfully created the backup!")
        print(f"You can find the backup data in {dst}")


def restore_from_documents():
    # Check if thunderbird is running
    is_running = common_methods.check_process()
    if is_running:
        print("Thunderbird is running! Quit Thunderbird and restart this program.")
        return

    documents = '/Users/{0}/Documents/Thunderbird-Backup'.format(getpass.getuser())

    try:
        entries = os.listdir(documents)
        print(f"entries: {entries}")
        count = 1
        backup_list = []
        for entry in entries:
            if entry.startswith('t'):
                backup_list.append(f"-{count}- {entry}")
                count += 1

        backup_list.append("-q- Quit")

        print()
        print("----------------------------------------------------------")
        print("Select the backup you want to restore:")
        print()
        for item in backup_list:
            print(item)
        print("----------------------------------------------------------")

        while True:
            choice = input("Your choice: ")

            if choice == '1':
                restore_data(backup_list[0])
                break
            elif choice == '2':
                restore_data(backup_list[1])
                break
            elif choice == '3':
                restore_data(backup_list[2])
                break
            elif choice == '4':
                restore_data(backup_list[3])
                break
            elif choice == '5':
                restore_data(backup_list[4])
                break
            elif choice == 'q':
                quit_application()
            else:
                print("Unknown input! Try again.")
                continue

    except FileNotFoundError as e:
        print(f"Error message: {e}")
        sys.exit(
            "Could not find a folder named 'Thunderbird-Backup'!\n "
            "(The 'Profiles' folder must be located in a folder named 'Thunderbird-Backup'.)"
        )


def restore_data(backup_item: str):
    logging.debug("Restore data...")
    logging.debug(f"Backup: {backup_item}")

    # Get the path of the source folder
    documents = '/Users/{0}/Documents/Thunderbird-Backup/'.format(getpass.getuser())
    src = documents + backup_item[4:]
    logging.debug(f"Source folder: {src}")

    # Get the path of the destination folder (Thunderbird folder)
    _, dst, _ = check_default_profile()
    logging.debug(f"Destination folder: {dst}")

    # Copy data to destination folder
    try:
        copy_tree(src, dst)
    except OSError as e:
        print(f"Creation of the directory {dst} failed")
        print(f"Error message: {e}")
        sys.exit("Program terminated!")
    else:
        print("Successfully restored the backup!")
        print(f"You can find the backup data in {dst}")


def quit_application():
    print("Good bye!")
    sys.exit()


def user_input():
    """
    Check user input
    """
    print()
    print("----------------------------------------------------------")
    print("What do you want to do?")
    print()
    print("-1- Show the path of the default profile")
    print("-2- Backup the default profile")
    print("-3- Restore the default profile")
    print("-4- Show version")
    print("-5- Quit the application")
    print("----------------------------------------------------------")

    while True:
        choice = input("Your choice: ")

        if choice == '1':
            show_default_path()
            break
        elif choice == '2':
            backup()
            break
        elif choice == '3':
            restore_from_documents()
            break
        elif choice == '4':
            info.app_info()
            break
        elif choice == '5':
            quit_application()

        else:
            print("Unknown input! Try again.")
            continue


def main():
    """
    The entry point of this program.
    """
    user_input()


if __name__ == '__main__':
    main()
