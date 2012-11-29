#!/usr/bin/env python3.3

import unittest
import RunProcessing
from os.path import isfile
from collections import OrderedDict

class RunProcessingTest(unittest.TestCase):

    def setUp(self):
        methods = OrderedDict()
        methods["def setup():"] = ["size(200, 400)"]
        methods["def draw():"] = ["background(200)"]
        self.runner = RunProcessing.RunProcessing("RunProcessingTest", methods)

    def test_path_to_processing_py_jar(self):
        self.assertTrue(isfile(self.runner.path_to_processing_py_jar))

    def test_contruct_py(self):
        r = "def setup():\n    size(200, 400)\ndef draw():\n    background(200)\n"
        s = self.runner.construct_py()
        self.assertEqual(r, s)

    def test_write_processing_py(self):
        self.runner.write_processing_py()
        self.assertTrue(isfile(self.runner.file_name))

    def test_run_processing_py(self):
        exit_code = self.runner.run_processing_py()
        self.assertFalse(exit_code)
         
if __name__ == '__main__':
    unittest.main()
