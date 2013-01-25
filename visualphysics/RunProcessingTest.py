#!/usr/bin/env python3.3

import os
import collections as co
import re
import unittest

import RunProcessing

class RunProcessingTest(unittest.TestCase):

    def setUp(self):
        methods = co.OrderedDict()
        methods["void_setup():"] = ["size(200, 400)"]
        methods["void_draw():"] = ["background(200)"]
        self.runner = RunProcessing.RunProcessing("RunProcessingTest", methods, testing=True)

    def test_path_to_processing_py_jar(self):
        self.assertTrue(os.path.isfile(self.runner.path_to_processing_py_jar))

    def test_contruct_processing_py(self):
        r = "def setup():\n    size(200, 400)\ndef draw():\n    background(200)\n"
        s = self.runner.construct_processing_py()
        self.assertEqual(r, s)

    def test_contruct_processing_pde(self):
        r = re.compile(r'void')
        s = self.runner.construct_processing_pde()
        self.assertTrue(r.match(s))

    def test_write_processing_py(self):
        self.runner.write_processing_py()
        self.assertTrue(os.path.isfile(self.runner.file_name_py))

    def test_write_processing_pde(self):
        self.runner.write_processing_pde()
        self.assertTrue(os.path.isfile(self.runner.file_name_pde))

    def test_run_processing_py(self):
        exit_code = self.runner.run_processing_py()
        self.assertFalse(exit_code)
         
    def test_run(self):
        exit_code = self.runner.run()
        self.assertFalse(exit_code)
         
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(RunProcessingTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
