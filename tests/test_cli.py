#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
import re

from subprocess import getstatusoutput

from profiles_backup import cli

prg = "../profiles_backup/cli.py"


@pytest.fixture()
def create_parser():
    """Create a parser"""
    parser = cli.create_parser()
    yield parser


def test_help_option():
    """Test -h, --help option"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


def test_evaluate_arguments(create_parser):
    """
    Test if the given arguments will be parsed.

    Args:
        create_parser: The created parser
    """
    args_version = create_parser.parse_args(["--version"])
    args_path = create_parser.parse_args(["--path"])
    args_backup = create_parser.parse_args(["--backup"])
    args_restore = create_parser.parse_args(["--restore"])

    assert args_version.version is True
    assert args_path.path is True
    assert args_backup.backup is True
    assert args_restore.restore is True
