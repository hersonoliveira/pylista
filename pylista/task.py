import json
import os
import click
from .defaults import LISTS_DIR


def add_task(task_name, list_name):
    """Add a task to a json file"""
    pass

def remove_task(task_id, list_name):
    """Remove a task from a list"""
    pass

def list_all_tasks(list_name):
    """Print all tasks on a list"""
    pass

def create_json_file(list_name):
    """Create a json file if it does not exist"""
    if not os.path.exists(LISTS_DIR):
        os.makedirs(LISTS_DIR)

    #TODO Maybe ask if would like to overwrite existing list
    path = os.path.join(LISTS_DIR, list_name)
    with open(f"{path}.json", "w+") as f:
        click.secho(f"List created: {path}")
