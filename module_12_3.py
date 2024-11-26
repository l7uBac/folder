import module_12_1
import module_12_2

import unittest

testcase = unittest.TestSuite()
testcase.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2.TournamentTest))
testcase.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(testcase)