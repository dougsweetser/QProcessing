#!/usr/bin/env python3.3

import sys
import unittest
import re

import AFrame
import Layout

class AFrameTest(unittest.TestCase):

    def setUp(self):
        self.verbose = True
        self.devices = \
            {'square':[500, 500, True], \
             'android_normal':[470, 320, True], \
             'android_large':[640, 480, False], \
             'android_xl':[960, 720, True], \
             'iPhone':[960, 640, False]}
        self.results = \
            {'square':{'aframe_height':251, 'aframe_width':251, 'sky_height':151, 'ground_height':100}, \
            'android_normal':{'aframe_height':311, 'aframe_width':311, 'sky_height':187, 'ground_height':124}, \
            'android_large':{'aframe_height':400, 'aframe_width':400, 'sky_height':240, 'ground_height':160}, \
            'android_xl':{'aframe_height':600, 'aframe_width':600, 'sky_height':360, 'ground_height':240}, \
            'iPhone':{'aframe_height':640, 'aframe_width':640, 'sky_height':384, 'ground_height':256}}
        self.layouts = {}
        self.frs = {}
        for k, v in self.devices.items():
            fr = AFrame.AFrame(v[0], v[1], portrait=v[2], testing=True)
            self.frs.update({k:fr})

    def test_aframe_height(self):
        self.method_test_loop('aframe_height')

    def test_aframe_width(self):
        self.method_test_loop('aframe_width')
 
    def test_sky_height(self):
        self.method_test_loop('sky_height')

    def test_ground_height(self):
        self.method_test_loop('ground_height')

    def test_set_size(self):
        for k, fr in self.frs.items():
            result = self.results.get(k)
            s = fr.set_sizes()
            for name, size in s.items():
                test = result.get(name)
                self.assertEqual(size, test)

    def test_setup(self):
        r = re.compile(r'rect|fill')
        for k, fr in self.frs.items():
            s = fr.setup()
            for line in s:
                self.assertTrue(r.match(line))
                if (self.verbose):
                    print(line)

    def test_run(self):
        for k, fr in self.frs.items():
            exit_code = fr.run()
            self.assertFalse(exit_code)

    def test_pprint(self):
        r = re.compile(r'height')
        for k, fr in self.frs.items():
            pp = fr.pprint()
            print("pp is: " + pp)
            self.assertTrue(r.search(pp))

    def method_test_loop(self, name):
        for k, fr in self.frs.items():
            string_2_function = {'aframe_height':fr.aframe_height(), 'aframe_width':fr.aframe_width(), 'sky_height':fr.sky_height(), 'ground_height':fr.ground_height()}
            result = self.results.get(k)
            test = result.get(name)
            out = string_2_function.get(name)
            if self.verbose:
                print(k + " " + name + " test:" + str(test) + ", got=" + str(out))
            self.assertEqual(out, test)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AFrameTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
