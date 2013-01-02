#!/usr/bin/env python3.3

# Copyright 2012 by Douglas Sweetser, sweetser@alum.mit.edu
# Licensed under the Apache License, Version 2.0.

import sys
import collections as co
import argparse as ap

sys.path.append("..")
import Layout
import RunProcessing

'''Class ButtonTable
Calculates sizes needed for a Button Table.
Author: sweetser@alum.mit.edu'''
class ButtonTable(Layout.Layout):

    def __init__(self, d1=480, d2=640, portrait=True, testing=False):
        super().__init__(d1, d2, portrait, testing)
        self.rows = 6
        self.columns = 3
        self.spacer = 2
        self.on = True
        self.sizes = co.OrderedDict() 
        self.testing = testing

    def show(self):
        self.on = True
        return self.on

    def hide(self):
        self.on = False
        return self.on

    def max(self):
        app_min = min(self.width, self.height)
        m = app_min - app_min % self.rows
        self.sizes["button_table_max"] = m
        return m

    def min(self):
        m = self.max() / self.rows * self.columns
        self.sizes["button_table_min"] = m
        return m

    def active_height(self):
        ah = self.max() / self.rows
        self.sizes["button_table_active_height"] = ah
        return ah

    def active_width(self):
        aw = self.min() / self.columns
        self.sizes["button_table_active_width"] = aw
        return aw

    def frame_height(self):
        fh = self.max() / self.rows - 2 * self.spacer
        self.sizes["button_table_frame_height"] = fh
        return fh

    def frame_width(self):
        fw = self.min() / self.columns - 2 * self.spacer
        self.sizes["button_table_frame_width"] = fw
        return fw

    def set_sizes(self):
        self.max()
        self.min()
        self.active_height()
        self.active_width()
        self.frame_height()
        self.frame_width()
        return self.sizes

    def setup(self):
        app_min = min(self.width, self.height)
        app_max = max(self.width, self.height)
        s = []
        s.append("rectMode(CORNERS)")
        s.append("fill(204, 102, 0)")
        d1 = app_max - self.min()
        gutter = int((app_min - self.max()) / 2)
        gmax = gutter + self.max()
        d2 = app_max

        if (self.portrait):
            rect = "rect(" + str(gutter) + "," + str(d1)  + "," + str(gmax)  + "," + str(d2) + ")"
        else:
            rect = "rect(" + str(d1) + "," + str(gutter)  + "," + str(d2)  + "," + str(gmax) + ")"
        s.append(rect)
        return s

    def run(self):
        methods = co.OrderedDict()
        s = super().setup()
        s += self.setup()
        methods["def setup():"] = s
        d = self.draw()
        methods["def draw():"] = d
        runner = RunProcessing.RunProcessing("ButtonTable", methods, self.testing)
        exit_code = runner.run()
        return exit_code

    def pprint(self):
        self.set_sizes()
        s = "rows, columns, spacer: " + str(self.rows) + ", " + str(self.columns) + ", " + str(self.spacer) + "\n"
        s += "active height, width: " + str(self.sizes.get("button_table_active_height")) + ", " + str(self.sizes.get("button_table_active_width")) + "\n"
        s += "frame height, width: " + str(self.sizes.get("button_table_frame_height")) + ", " + str(self.sizes.get("button_table_frame_width"))
        print(s)
        return s

if __name__ == '__main__':

    args_parser = ap.ArgumentParser(description='Button table calculations')
    args_parser.add_argument('-s', '--size', type=str, help="Acceptable sizes are: normal, large, xl, square, iphone, and ipad")
    args_parser.add_argument('-g', '--gui', action='store_true', default=False, help="See a box")
    args_parser.add_argument('--height', type=int, default=960)
    args_parser.add_argument('-w', '--width', type=int, default=720)
    args_parser.add_argument('-p', '--portrait', action='store_true', default=False)
    args_parser.add_argument('-l', '--landscape', action='store_true', default=False)
    args_parser.add_argument('--pprint', action='store_true', default=False)
    args = args_parser.parse_args()

    if(not args.gui and not args.pprint):
        print("You should set -g/--gui or --pprint.\nExiting.")
        sys.exit(1)

    sizes = {'square':[500, 500], \
             'normal':[470, 320], \
             'large':[640, 480], \
             'xl':[960, 720], \
             'iphone':[960, 640], \
             'ipad':[2048, 1536]}

    if(args.size):
         if (args.size in sizes):
             lxw = sizes[args.size]
             args.height = lxw[0]
             args.width = lxw[1]
         else:
             print("Did not find that size. Know these: ")
             for k in sizes.keys():
                 print(k + " ")
             sys.exit(1)

    if (args.landscape and args.portrait):
        print("Choose either -portrait or -lanscape, not both.\nProgram exiting.\n")
        sys.exit()
    elif (not args.landscape and not args.portrait):
        args.portrait = True

    bt = ButtonTable(args.width, args.height, args.portrait)

    if(args.pprint):
        bt.pprint()

    if(args.gui):
        bt.run()
