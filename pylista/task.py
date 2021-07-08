import os

import click

from pylista.defaults import LISTS_DIR


def create_json_file(list_name: str) -> None:
    """Create a json file if it does not exist"""
    if not os.path.exists(LISTS_DIR):
        os.makedirs(LISTS_DIR)

    path = os.path.join(LISTS_DIR, list_name)
    with open(f"{path}.json", "w+") as f:
        click.secho(f"List created: {path}")


def add_note_to_list(note: str, list: str):
    """
    Add note to list
    """
    pass