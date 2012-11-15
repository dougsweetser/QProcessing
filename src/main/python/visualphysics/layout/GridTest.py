#!/usr/bin/env python3.3

import unittest
import Grid

class GridTest(unittest.TestCase):

    def setUp(self):
        self.p = Grid.Grid(1, 2)

    def test_x(self):
        self.assertEqual(self.p.x, 1)

    def test_y(self):
        self.assertEqual(self.p.y, 2)

    def test_simple_print(self):
        sp_string = "1 2"
        sp = self.p.simple_print()
        self.assertEqual(sp_string, sp)

    def test_pretty_print(self):
        pp_string = "The grid point is (1, 2)."
        pp = self.p.pretty_print()
        self.assertEqual(pp_string, pp)

if __name__ == '__main__':
    unittest.main()
