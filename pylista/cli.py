import click
from pylista.task import create_json_file, add_note_to_list, get_list_file
from pylista.utils import create_pylista_dir
import os
from pylista.defaults import LISTS_DIR


@click.group()
def cli():
    """A simple cli list app"""
    pass


@cli.command()
@click.argument("list")
@click.argument("note")
def add(list, note):
    """Add a new task"""
    list_path = os.path.join(LISTS_DIR, f"{list}.json")
    if not os.path.exists(list_path):
        click.secho("List doesn't exist!")
    else:
        add_note_to_list(note, list_path)
        click.secho(f"Note added to list {list}")


@cli.command()
def remove():
    """Remove a note"""
    pass


@cli.command()
@click.argument("list")
def list(list):
    """List notes"""
    list_path = _make_path_to_list(list)
    print(get_list_file(list_path))


@cli.command()
@click.argument("list")
def new_list(list):
    """
    Create a new list
    """
    new_list = os.path.join(LISTS_DIR, f"{list}.json")

    if os.path.exists(new_list):
        click.secho("List is already present!")
    else:
        # create list
        create_json_file(list)


def _make_path_to_list(list: str) -> str:
    return os.path.join(LISTS_DIR, f"{list}.json")
