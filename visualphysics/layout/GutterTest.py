#!/usr/bin/env python3.3

import unittest
import re
import sys

import Gutter
sys.path.append('..')
import Layout

class GutterTest(unittest.TestCase):

    def setUp(self):
        self.verbose = False
        self.devices = \
            {'square':[500, 500, True], \
             'android_normal':[470, 320, True], \
             'android_large':[640, 480, False], \
             'android_xl':[960, 720, True], \
             'iPhone':[960, 640, False]}
        self.results = \
            {'square':{'button_table_top':1, 'button_table_bottom':1, 'frame_top':124, 'frame_bottom':125, 'left':0, 'center':0, 'right':0, 'frame_width':79}, \
            'android_normal':{'button_table_top':1,'button_table_bottom':1, 'frame_top':4, 'frame_bottom':5, 'left':0, 'center':0, 'right':0}, \
            'android_large':{'button_table_top':0, 'button_table_bottom':0, 'frame_top':40, 'frame_bottom':40, 'left':0, 'center':0, 'right':0}, \
            'android_xl':{'button_table_top':0, 'button_table_bottom':0, 'frame_top':60, 'frame_bottom':60, 'left':0, 'center':0, 'right':0}, \
            'iPhone':{'button_table_top':2, 'button_table_bottom':2, 'frame_top':0, 'frame_bottom':0, 'left':1, 'center':1, 'right':0}}
        self.layouts = {}
        self.guts = {}
        for k,v in self.devices.items():
            gut = Gutter.Gutter(v[0], v[1], portrait=v[2], testing=True)
            self.guts.update({k:gut})

    def test_button_table_top(self):
        self.method_test_loop('button_table_top')

    def test_button_table_bottom(self):
        self.method_test_loop('button_table_bottom')
 
    def test_left(self):
        self.method_test_loop('left')

    def test_center(self):
        self.method_test_loop('center')

    def test_right(self):
        self.method_test_loop('right')

    def test_set_size(self):
        for k, gut in self.guts.items():
            result = self.results.get(k)
            s = gut.set_sizes()
            for name, size in s.items():
                short_name = re.sub(r'gutter_', r'', name)
                test = result.get(short_name)
                self.assertEqual(size, test)

    def test_pprint(self):
        r = re.compile(r'gutter')
        for k, gut in self.guts.items():
            pp = gut.pprint()
            self.assertTrue(r.match(pp))

    def method_test_loop(self, name):
        for k, gut in self.guts.items():
            string_2_function = {'button_table_top':gut.button_table_top(), 'button_table_bottom':gut.button_table_bottom(), 'left':gut.left(), 'center':gut.center(), 'right':gut.right()}
            result = self.results.get(k)
            test = result.get(name)
            out = string_2_function.get(name)
            if self.verbose:
                print(k + " " + name + " test:" + str(test) + ", got=" + str(out))
            self.assertEqual(out, test)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(GutterTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
