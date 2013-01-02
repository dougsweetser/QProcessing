#!/usr/bin/env python3.3

import sys
import unittest

import LayoutTest
import RunProcessingTest

sys.path.append('layout')
import ButtonTableTest
import FrameTest
import GridTest
import GutterTest

if __name__ == '__main__':
    tests = []
    tests.append(unittest.TestLoader().loadTestsFromTestCase(LayoutTest.LayoutTest))
    tests.append(unittest.TestLoader().loadTestsFromTestCase(RunProcessingTest.RunProcessingTest))
    tests.append(unittest.TestLoader().loadTestsFromTestCase(ButtonTableTest.ButtonTableTest))
    tests.append(unittest.TestLoader().loadTestsFromTestCase(FrameTest.FrameTest))
    tests.append(unittest.TestLoader().loadTestsFromTestCase(GridTest.GridTest))
    tests.append(unittest.TestLoader().loadTestsFromTestCase(GutterTest.GutterTest))
    all_tests = unittest.TestSuite(tests)
    unittest.TextTestRunner(verbosity=2).run(all_tests)

