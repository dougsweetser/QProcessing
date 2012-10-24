#!/usr/local/bin/python3

import unittest
import template

class TestStuff(unittest.TestCase):

    def setUp(self):
        self.input = 'foo'
        self.t = template.Template(self.input)

    def test_calc(self):
        d = self.t.calc(False)
        self.assertEqual(self.input, d)

    def test_calc_pretty(self):
        pretty = 'One arg is: ' + self.input
        d = self.t.calc(True)
        self.assertEqual(pretty, d)

if __name__ == '__main__':
    unittest.main()
