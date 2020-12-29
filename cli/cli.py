import click
from . import task


@click.group()
def cli():
    """A simple cli list app"""
    pass


@cli.command()
@click.argument("task")
def add(task):
    """Add a new task"""
    pass


@cli.command()
def done():
    """Complete a task"""
    pass


@cli.command()
def list():
    """List tasks"""
    pass


@cli.command()
@click.argument("list_name")
def new_list(list_name):
    """Create a new list"""
    task.create_json_file(list_name)
 