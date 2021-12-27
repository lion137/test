import unittest
import sys
import pdb
from decimalrunner import DecimalRunner
from helpers import FIXTURES_PATH, get_json_from_file

data_dict = get_json_from_file(FIXTURES_PATH)

class testTest(DecimalRunner):
    def test_dummy_numbers(self):
        # expected numbers
        PV01 = data_dict["PV01" + self._testMethodName]
        DV01 = data_dict["DV01" + self._testMethodName]
        # actual numbers
        PV01value = 0.02137
        DV01value = 0.02137
        self.assertAlmostEqual(PV01, PV01value, places=3)
        self.assertAlmostEqual(DV01, DV01value, places=3)
    def test_dummy_numbers2(self):
        # expected numbers
        PV01 = data_dict["PV01" + self._testMethodName]
        DV01 = data_dict["DV01" + self._testMethodName]
        PV01copy = data_dict["PV01copy" + self._testMethodName]
        # actual numbers
        PV01value = 0.2147
        DV01value = 0.2157
        PV01_copy_value = 0.2167
        self.assertAlmostEqual(PV01, PV01value, places=3)
        # pdb.set_trace() #debug
        self.assertAlmostEqual(DV01, DV01value, places=3)
        self.assertAlmostEqual(PV01copy, PV01_copy_value, places=3)
    def test_dummy_numbers_equal(self):
        # expected numbers
        expected_sum = data_dict["expected_sum" + self._testMethodName]
    
        # actual numbers
        expected_sum_value = 0.22137
        self.assertEqual(expected_sum, expected_sum_value)
