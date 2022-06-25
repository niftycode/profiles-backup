
import pytest

from profiles_backup.cli import user_input
from profiles_backup.cli import show_default_path
from profiles_backup import cli


def test_input(mocker):
    test_a = mocker.patch("cli.show_default_path()", return_value="hello")
    # with mocker.patch('builtins.input', return_value='1'):
    #     assert user_input() == "hello"
