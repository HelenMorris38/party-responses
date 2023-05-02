from src.utils import party_responses, create_json_file
from unittest.mock import Mock
from os import path
import json

def test_creates_json_file():
    create_json_file('test-data.json')
    assert path.isfile('test-data.json')

def test_party_responses_adds_a_person_to_json():
    party_responses('James', 'yes', 'test-data.json')
    try:
        json.load('test-data.json')
        assert True
    except:
        print('Not valid JSON object')
        assert False