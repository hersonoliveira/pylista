import os
from pathlib import Path

def create_pylista_dir(dir: str = ".pylista") -> None:
    path = os.path.join(Path.home(), dir)
    try:
        os.mkdir(path)
    except FileExistsError:
        pass
