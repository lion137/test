import os
import json
from unittest import TestCase
import pdb
from helpers import FIXTURES_PATH, get_json_from_file
from runtests import DecimalRunnerBase


class DecimalRunner(DecimalRunnerBase, TestCase):
    def assertAlmostEqual(self, left, right, places=7, msg=None, delta=None):
        if self.rebaseAll:
            self._update_fixture(TestCase.assertAlmostEqual, left, right, places=places, msg=msg, delta=delta)
        else:
            return TestCase.assertAlmostEqual(self, left, right, places=places, msg=msg, delta=delta)
    def assertEqual(self, left, right, msg=None):
        if self.rebaseAll:
            self._update_fixture(TestCase.assertEqual, left, right, msg=msg)
        else:
            return TestCase.assertEqual(self, left, right, msg=msg)
    def _update_fixture(self, assertion, left, right, places=7, msg=None, delta=None):
        try:
            if assertion == TestCase.assertAlmostEqual:
                assertion(self, left, right, places=places, msg=msg, delta=delta)
            else:
                assertion(self, left, right, msg=msg)
        except AssertionError:
            data_dict = get_json_from_file(FIXTURES_PATH)
            # pdb.set_trace() #debug
            data_dict[self._extract_update_key(self._testMethodName, left, data_dict)] = right
            with open(FIXTURES_PATH, 'w') as outfile:
                json.dump(data_dict, outfile, indent=2)
    def _extract_update_key(self, test_name, value, data):
        def is_exact_match(name, key):
            index = key.find("test_")
            return name == key[index:]
        def get_key(value, data):
            for k, v in data.items():
                if v == value:
                    return k
        test_items = {k: v for k, v in data.items() if test_name in k and is_exact_match(test_name, k)}
        return get_key(value, test_items)
    
