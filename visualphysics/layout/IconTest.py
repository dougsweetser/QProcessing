#!/usr/bin/env python3.3

import sys
import unittest
import re

import Icon
import Layout

class IconTest(unittest.TestCase):

    def setUp(self):
        self.verbose = True

    def test_home(self):
        self.assertTrue(1)

    def test_show_full_screen(self):
        self.assertTrue(1)
 
    def test_hide_full_screen(self):
        self.assertTrue(1)

    def test_show_rotations(self):
        self.assertTrue(1)

    def test_hide_rotations(self):
        self.assertTrue(1)
    
    def test_show_boosts(self):
        self.assertTrue(1)

    def test_hide_boosts(self):
        self.assertTrue(1)
    
    def test_x_rotation(self):
        self.assertTrue(1)

    def test_y_rotation(self):
        self.assertTrue(1)

    def test_z_rotation(self):
        self.assertTrue(1)

    def test_xy_rotation(self):
        self.assertTrue(1)

    def test_xz_rotation(self):
        self.assertTrue(1)

    def test_yz_rotation(self):
        self.assertTrue(1)

    def test_x_boost(self):
        self.assertTrue(1)

    def test_y_boost(self):
        self.assertTrue(1)
        
    def test_z_boost(self):
        self.assertTrue(1)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(IconTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
