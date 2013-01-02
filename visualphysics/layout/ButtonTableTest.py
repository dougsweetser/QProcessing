#!/usr/bin/env python3.3

import unittest
import re

import ButtonTable

class ButtonTableTest(unittest.TestCase):

    def setUp(self):
        self.verbose = True
        self.devices = \
            {'square':[500, 500, True], \
             'android_normal':[470, 320, True], \
             'android_large':[640, 480, False], \
             'android_xl':[960, 720, True], \
             'iPhone':[960, 640, False]}
        self.results = \
            {'square':{'max':498, 'min':249, 'active_height':83, 'active_width':83, 'frame_height':79, 'frame_width':79, 'draw':''}, \
            'android_normal':{'max':318,'min':159, 'active_height':53, 'active_width':53, 'frame_height':49, 'frame_width':49, 'draw':''}, \
            'android_large':{'max':480, 'min':240, 'active_height':80, 'active_width':80, 'frame_height':76, 'frame_width':76, 'draw':''}, \
            'android_xl':{'max':720, 'min':360, 'active_height':120, 'active_width':120, 'frame_height':116, 'frame_width':116, 'draw':''}, \
            'iPhone':{'max':636, 'min':318, 'active_height':106, 'active_width':106, 'frame_height':102, 'frame_width':102, 'draw':''}}
        self.bts = {}
        for k, v in self.devices.items():
            bt = ButtonTable.ButtonTable(v[0], v[1], portrait=v[2], testing=True)
            self.bts.update({k:bt})

    def test_rows(self):
        self.attribute_loop('rows', 6)

    def test_columns(self):
        self.attribute_loop('columns', 3)

    def test_spacer(self):
        self.attribute_loop('spacer', 2)

    def test_show(self):
        for k, bt in self.bts.items():
            show = bt.show()
            self.assertTrue(show)

    def test_hide(self):
        for k, bt in self.bts.items():
            hide = bt.hide()
            self.assertFalse(hide)

    def test_max(self):
        self.method_test_loop('max')

    def test_min(self):
        self.method_test_loop('min')

    def test_active_height(self):
        self.method_test_loop('active_height')

    def test_active_width(self):
        self.method_test_loop('active_width')
 
    def test_frame_height(self):
        self.method_test_loop('frame_height')

    def test_frame_width(self):
        self.method_test_loop('frame_width')

    def test_set_size(self):
        for k, bt in self.bts.items():
            result = self.results.get(k)
            s = bt.set_sizes()
            for name, size in s.items():
                short_name = re.sub(r'button_table_', r'', name)
                test = result.get(short_name)
                self.assertEqual(size, test)

    def test_setup(self):
        r = re.compile(r"rect|fill")
        for k,bt in self.bts.items():
            s = bt.setup()
            for line in s:
                self.assertTrue(r.match(line))
                if (self.verbose):
                    print(line)

    def test_run(self):
        for k,bt in self.bts.items():
            exit_code = bt.run()
            self.assertFalse(exit_code)

    def test_pprint(self):
        r = re.compile(r'row|max|height')
        for k, bt in self.bts.items():
            pp = bt.pprint()
            self.assertTrue(r.match(pp))

    def attribute_loop(self, name, value):
        for k,bt in self.bts.items():
            string_2_attribute = {'rows': bt.rows, 'columns':bt.columns, 'spacer':bt.spacer, 'on':bt.on}
            self.assertEqual(string_2_attribute.get(name), value)

    def method_test_loop(self, name):
        for k,bt in self.bts.items():
            string_2_function = {'max':bt.max(), 'min':bt.min(), 'active_height':bt.active_height(), 'active_width':bt.active_width(), 'frame_height':bt.frame_height(), 'frame_width':bt.frame_width()}
            result = self.results.get(k)
            test = result.get(name)
            out = string_2_function.get(name)
            if self.verbose:
                print(k + " " + name + " test:" + str(test) + ", got=" + str(out))
            self.assertEqual(out, test)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ButtonTableTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
