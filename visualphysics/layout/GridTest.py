#!/usr/bin/env python3.3

import unittest
import Grid

class GridTest(unittest.TestCase):

    def setUp(self):
        self.g = Grid.Grid(1, 2)

    def test_x(self):
        self.assertEqual(self.g.x, 1)

    def test_y(self):
        self.assertEqual(self.g.y, 2)

    def test_simple_print(self):
        sp_string = "1 2"
        sp = self.g.simple_print()
        self.assertEqual(sp_string, sp)

    def test_pretty_print(self):
        pp_string = "The grid point is (1, 2)."
        pp = self.g.pretty_print()
        self.assertEqual(pp_string, pp)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(GridTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
