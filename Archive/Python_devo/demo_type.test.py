#!/usr/local/bin/python3 

import unittest
import demo_type
import re

class DemoTypeTests(unittest.TestCase):

    def setUp(self):
        self.cmd = 'q_one'
        self.dt = demo_type.DemoType(self.cmd)

    def test_init(self):
        self.assertEqual(self.cmd, self.dt.cmd)

    def test_type_cmd(self):
        dt_cmd = self.dt.type_cmd()
        self.assertEqual("echo 'q_one' | pv -qL 10", dt_cmd)

    def test_run_cmd(self):
        dt_cmd = self.dt.run_cmd()
        self.assertEqual("q_one", dt_cmd, "test 3")

    def test_run_demo(self):
        regexp_cmd = re.compile(r'q_one | pv')
        regexp_run = re.compile(r'q_one')
        dt = demo_type.DemoType(self.cmd)
        dt_cmd = self.dt.run_demo()
        self.assertTrue(regexp_cmd.search(dt_cmd))
        self.assertTrue(regexp_run.search(dt_cmd))

if __name__ == '__main__':
    unittest.main()
