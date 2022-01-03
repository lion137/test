# test file

import unittest

class TestTest(unittest.TestCase):
    def test_test(self):
        exvar = 2.21372137
        self.assertAlmostEqual(exvar, 2.21372137)
    def test_test2(self):
        exvar = 2.21372137
        self.assertAlmostEqual(exvar, 2.21372)