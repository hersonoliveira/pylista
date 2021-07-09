import os
from pathlib import Path
from pylista.defaults import LISTS_DIR


def create_pylista_dir(dir: str) -> None:
    """
    Create a directory to store lists on the user home dir
    """
    if not os.path.exists(LISTS_DIR):
        os.makedirs(LISTS_DIR)


def create_list_file(name: str) -> None:
    """
    """
    pass

