import json
import os

from pylista.defaults import LISTS_DIR
from pylista.lists import create_json_file


def test_create_json_file():
    create_json_file("test_list")
    result_file = os.path.join(LISTS_DIR, "test_list.json")

    assert os.path.exists(result_file)
    with open(result_file, "r") as json_file:
        data = json.load(json_file)
        assert data == {"notes": []}
