import os
import json
from unittest import TestCase
FIXTURES_PATH = os.path.normpath("/home/tmadry/Projects/Python/tests/decimal_recording/fixtures/numbers.json")

def get_json_from_file(file_name):
    with open(file_name, 'r') as f:
        return json.load(f)

