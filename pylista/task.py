import os
import json
import click
from sqlalchemy.sql.operators import op

from pylista.defaults import LISTS_DIR


def create_json_file(list_name: str) -> None:
    """Create a json file if it does not exist"""
    if not os.path.exists(LISTS_DIR):
        os.makedirs(LISTS_DIR)

    path = os.path.join(LISTS_DIR, list_name)
    data = {
        "notes": []
        }
    with open(f"{path}.json", "w+") as f:
        json.dump(data, f)
    click.secho(f"List created: {path}")


def add_note_to_list(note: str, list_path: str):
    """
    Add note to list
    """
    with open(list_path, "r+") as json_file:
        data = json.load(json_file)
        data["notes"].append(note)
        json_file.seek(0)
        json.dump(data, json_file)


def get_list_file(list_path: str) -> list:
    """
    Get and returns a python list containing notes from a list file
    """
    with open(list_path, "r") as json_file:
        data = json.load(json_file)
    return data["notes"]


def print_notes(l: list) -> None:
    """
    Format a python list of notes to print
    """
    pass
