import os
from pathlib import Path

def create_pylista_dir(dir: str = ".pylista") -> None:
    """
    Create a directory to store lists on the user home dir
    """
    path = os.path.join(Path.home(), dir)
    try:
        os.mkdir(path)
    except FileExistsError:
        pass


def create_list_file(name: str) -> None:
    """
    """
    pass