#!/usr/bin/env python3.3

import unittest
import re

import Layout

class LayoutTest(unittest.TestCase):

    def setUp(self):
        self.devices = \
            {'square':[500, 500], \
             'android_normal':[470, 320], \
             'android_large':[640, 480], \
             'android_xl':[960, 720], \
             'iPhone':[960, 640], \
             'iPad':[2048, 1536]}
        self.layouts = {}
        for k,v in self.devices.items():
            self.layouts.update({k:Layout.Layout(v[0], v[1], testing=True)})

    def test_app_height(self):
        for k,layout in self.layouts.items():
            m = layout.app_max
            dmax = self.devices[k][0]
            self.assertEqual(m, dmax)

    def test_app_width(self):
        for k,layout in self.layouts.items():
            m = layout.app_min
            dmin = self.devices[k][1]
            self.assertEqual(m, dmin)

    def test_update(self):
        for k,layout in self.layouts.items():
            self.assertTrue(layout.update)

    def test_pprint(self):
        for k,layout in self.layouts.items():
            pp = layout.pprint()
            dmax = self.devices[k][0]
            dmin = self.devices[k][1]
            result = "app_max is: " + str(dmax) + "\napp_min is: " + str(dmin)
            self.assertEqual(pp, result)

    def test_setup(self):
        r = re.compile(r"fill|size|rect")
        for k, layout in self.layouts.items():
            s = layout.setup()
            for line in s: 
                self.assertTrue(r.match(line))

    def test_draw(self):
        r = re.compile(r"noLoop")
        for k, layout in self.layouts.items():
            s = layout.draw()
            for line in s: 
                print("line\n" + line)
                self.assertTrue(r.match(line))

    def test_run(self):
        for k,layout in self.layouts.items():
            exit_code = layout.run()
            self.assertFalse(exit_code)
         
if __name__ == '__main__':
    unittest.main()
