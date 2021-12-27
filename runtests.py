import os
import sys
import unittest
import pdb  #debug
# pdb.set_trace() #debug
global rebase_all
if len(sys.argv) > 1:
    rebase_all = True
else:
    rebase_all = False

class DecimalRunnerBase():
    global rebase_all
    rebaseAll = rebase_all


os.chdir(os.path.dirname(os.path.abspath(__file__)))

loader = unittest.TestLoader()

suite = loader.discover('.')

runner = unittest.TextTestRunner()
result = runner.run(suite)
# print(result.failures)  #debug
if not result.wasSuccessful():
    sys.exit(True)