#!/usr/bin/env python3.3

# Copyright 2012 by Douglas Sweetser, sweetser@alum.mit.edu
# Licensed under the Apache License, Version 2.0.

import collections as co
import argparse

'''Class ButtonTable
Button Table layout calculations
Author: sweetser@alum.mit.edu'''
class ButtonTable:

    def __init__(self, layout):
        self.layout = layout;
        self.rows = 6
        self.columns = 3
        self.spacer = 2
        self.on = True
        self.sizes = co.OrderedDict() 

    def show(self):
        self.on = True
        return self.on

    def hide(self):
        self.on = False
        return self.on

    def max(self):
        m = self.layout.app_min - self.layout.app_min % self.rows
        self.sizes["max"] = m
        return m

    def min(self):
        m = self.max() / self.rows * self.columns
        self.sizes["min"] = m
        return m

    def active_height(self):
        ah = self.max() / self.rows
        self.sizes["active_height"] = ah
        return ah

    def active_width(self):
        aw = self.min() / self.columns
        self.sizes["active_width"] = aw
        return aw

    def frame_height(self):
        fh = self.max() / self.rows - 2 * self.spacer
        self.sizes["frame_height"] = fh
        return fh

    def frame_width(self):
        fw = self.min() / self.columns - 2 * self.spacer
        self.sizes["frame_width"] = fw
        return fw

    def set_size(self):
        max = self.max()
        ah = self.active_height()
        aw = self.active_width()
        fh = self.frame_height()
        fw = self.frame_width()
        min = self.min()

    def setup(self):
        s = "rectMode(CORNERS);\n"
        s + "fill(204, 102, 0);\n"
        d1 = self.layout.app_max - self.min
        gutter = int((self.layout.app_min - self.max) / 2)
        gmax = gutter + self.max
        d2 = self.layout.app_max

        if (self.layout.portrait):
            s + "rect(" + str(gutter) + "," + str(d1)  + "," + str(gmax)  + "," + str(d2) + ")"
        else:
            s + "rect(" + str(d1) + "," + str(gutter)  + "," + str(d2)  + "," + str(gmax) + ")"
        return s

    def draw(self):
        return ""

    def run(self):
        void

    def pretty_print(self):
        result = "void"
        print(result)
        return result

if __name__ == '__main__':
    args_parser = argparse.ArgumentParser(description='Prints a point given two bits of data')
    args_parser.add_argument('-s', '--sprint', action='store_true', default=False, help="Simple print")
    args_parser.add_argument('-p', '--pprint', action='store_true', default=False, help="Pretty print, more verbose")
    args_stuff = args_parser.parse_known_args()
    args = args_stuff[0]
    argv = args_stuff[1]
 
    if (not args.pprint):
        args.sprint = True

    while argv:
        s = argv.pop(0)
        foo_size = Size.Size(s)
        if args.sprint:
            foo_size.simple_print()
        if args.pprint:
            foo_size.pretty_print()

