from src.utils import party_responses, create_json_file
from unittest.mock import Mock
from os import path
import json

def test_creates_json_file():
    create_json_file('test-data.json')
    assert path.isfile('test-data.json')

def test_party_responses_adds_a_person_to_json():
    party_responses('James', 'yes', 'test-data.json')
    with open('test-data.json') as t:
        test_responses = json.load(t)
    assert test_responses[0] == {
        'id' : '001',
        'name' : 'James',
        'response' : 'yes'
    }

def test_party_responses_capitalises_name():
    party_responses('emily', 'yes', 'test-data.json')
    with open('test-data.json') as t:
        test_responses = json.load(t)
    assert test_responses[1] == {
        'id' : '002',
        'name' : 'Emily',
        'response' : 'yes'
    }