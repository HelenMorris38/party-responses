from src.utils import party_responses, write_to_json, update_response
from unittest.mock import Mock
from os import path
import json

def test_writes_to_json_file():
    write_to_json('test-data.json', [])
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

def test_updates_response():
    update_response('001', 'no', 'test-data.json')
    with open('test-data.json') as t:
        test_responses = json.load(t)
    assert test_responses[0] == {
        'id' : '001',
        'name' : 'James',
        'response' : 'no'
    } 