#!/usr/bin/env python3.3

import os
import collections as co
import unittest

import RunProcessing

class RunProcessingTest(unittest.TestCase):

    def setUp(self):
        methods = co.OrderedDict()
        methods["def setup():"] = ["size(200, 400)"]
        methods["def draw():"] = ["background(200)"]
        self.runner = RunProcessing.RunProcessing("RunProcessingTest", methods, testing=True)

    def test_path_to_processing_py_jar(self):
        self.assertTrue(os.path.isfile(self.runner.path_to_processing_py_jar))

    def test_contruct_processing_py(self):
        r = "def setup():\n    size(200, 400)\ndef draw():\n    background(200)\n"
        s = self.runner.construct_processing_py()
        self.assertEqual(r, s)

    def test_write_processing_py(self):
        self.runner.write_processing_py()
        self.assertTrue(os.path.isfile(self.runner.file_name))

    def test_run_processing_py(self):
        exit_code = self.runner.run_processing_py()
        self.assertFalse(exit_code)
         
    def test_run(self):
        exit_code = self.runner.run()
        self.assertFalse(exit_code)
         
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(RunProcessingTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
