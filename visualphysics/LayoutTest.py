#!/usr/bin/env python3.3

import unittest
import re

import Layout

class LayoutTest(unittest.TestCase):

    def setUp(self):
        self.devices = \
            {'square':[500, 500, True], \
             'android_normal':[470, 320, True], \
             'android_large':[640, 480, False], \
             'android_xl':[960, 720, True], \
             'iPhone':[960, 640, False]}
        self.layouts = {}
        for k,v in self.devices.items():
            self.layouts.update({k:Layout.Layout(v[0], v[1], portrait=v[2], testing=True)})

    def test_app_height(self):
        for k,layout in self.layouts.items():
            if (layout.portrait):
                h = self.devices[k][0]
            else:
                h = self.devices[k][1]
            lh = layout.height
            self.assertEqual(lh, h)

    def test_app_width(self):
        for k,layout in self.layouts.items():
            if (layout.portrait):
                w = self.devices[k][1]
            else:
                w = self.devices[k][0]
            lw = layout.width
            self.assertEqual(lw, w)

    def test_update(self):
        for k,layout in self.layouts.items():
            self.assertTrue(layout.update)

    def test_pprint(self):
        for k,layout in self.layouts.items():
            if (layout.portrait):
                h = self.devices[k][0]
                w = self.devices[k][1]
            else:
                h = self.devices[k][1]
                w = self.devices[k][0]
            result = "width is: " + str(w) + "\nheight is: " + str(h)
            pp = layout.pprint()
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
                self.assertTrue(r.match(line))

    def test_run(self):
        for k,layout in self.layouts.items():
            exit_code = layout.run()
            self.assertFalse(exit_code)
         
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LayoutTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
