from src.utils import party_responses, create_json_file
from unittest.mock import Mock
from os import path

def test_creates_list_of_dicts():
    create_json_file('test-data.json')
    assert path.isfile('test-data.json')

