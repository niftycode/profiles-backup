# profiles-backup

**This program is under development. Most features are not implemented yet. So, use this program on your own risk.**

## About

Use this program to backup or restore your Thunderbird's default profile folder. This is the folder with the '.default-release' suffix located in

    ~/Library/Thunderbird/Profiles

Note: Only **macOS** is currently supported.

Run the program with

	$ python3 profiles-backup.py

## Requirements

* Python >= 3.7
* psutil >= 5.7.2

## Changelog

* May 1st, 2020: First commit, Version 0.0.1
* August 28th, 2020: Check if Thunderbird is running
* February 19th, 2021: Rename project to "profiles-backup"
