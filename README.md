# pylista 📃

A simple python package CLI tool to manage lists

## Getting Started

Install the app with

```bash
pip install pylista
```

To check the options

```bash
pylista --help

Usage: pylista [OPTIONS] COMMAND [ARGS]...

  A simple CLI tool to manage lists

Options:
  --help  Show this message and exit.

Commands:
  add    Add a note to list
  ls     List notes
  newls  Create a new list
  rm     Remove a note from list
```

To create your first list

```
pylista newls movies

List created: /home/user/.pylista/movies
```

## Improvements

* Add env variable to set the folder path of the lists
