#!/usr/bin/env python3.3

# Copyright 2012 by Douglas Sweetser, sweetser@alum.mit.edu
# Licensed under the Apache License, Version 2.0.

import sys
import collections as co
import argparse as ap

sys.path.append("..")
import Layout
import ButtonTable
import Frame

'''Class Gutter
Calculates sizes of spaces between Frame and ButtonTable.
Author: sweetser@alum.mit.edu'''
class Gutter(Layout.Layout):

    def __init__(self, d1=640, d2=480, portrait=True, testing=False):
        super().__init__(d1, d2, portrait, testing)
        self.button_table = ButtonTable.ButtonTable(d1, d2, portrait, testing)
        self.frame = Frame.Frame(d1, d2, portrait, testing)
        self.sizes = co.OrderedDict() 
        self.testing = testing

    def button_table_top(self):
        btm = self.button_table.max()
        gt = round((self.app_min - btm)/2)
        self.sizes["gutter_button_table_top"] = gt
        return gt

    def button_table_bottom(self):
        btm = self.button_table.max()
        gt = round((self.app_min - btm)/2)
        gb = self.app_min - btm - gt
        self.sizes["gutter_button_table_bottom"] = gb
        return gb

    def frame_top(self):
        fh = self.frame.frame_height()
        ft = round((self.app_min - fh)/2)
        self.sizes["gutter_frame_top"] = ft
        return ft

    def frame_bottom(self):
        fh = self.frame.frame_height()
        ft = round((self.app_min - fh)/2)
        fb = self.app_min - fh - ft
        self.sizes["gutter_frame_bottom"] = fb
        return fb

    def open_space(self):
        #print("app_max: " + str(self.app_max))
        #print("frame_width: " + str(self.frame.frame_width()))
        #print("bt.min(): " + str(self.button_table.min()))
        os = self.app_max - self.frame.frame_width() - self.button_table.min()
        return os

    def left(self):
        gl = round(self.open_space() / 3)
        self.sizes["gutter_left"] = gl
        return gl

    def center(self):
        c = round(self.open_space() / 3)
        self.sizes["gutter_center"] = c
        return c

    def right(self):
        os = self.open_space()
        r = os - 2 * round(os / 3)
        self.sizes["gutter_right"] = r
        return r

    def set_sizes(self):
        self.button_table_top()
        self.button_table_bottom()
        self.frame_top()
        self.frame_bottom()
        self.left()
        self.center()
        self.right()
        return self.sizes

    def pprint(self):
        self.set_sizes()
        s = "gutter button_table top, bottom: " + str(self.sizes.get("gutter_button_table_top")) + ", " + str(self.sizes.get("gutter_button_table_bottom")) + "\n"
        s += "gutter frame top, bottom: " + str(self.sizes.get("gutter_frame_top")) + ", " + str(self.sizes.get("gutter_frame_bottom")) + "\n"
        s += "gutter left, center, right: " + str(self.sizes.get("gutter_left")) + ", " + str(self.sizes.get("gutter_center")) + ", " + str(self.sizes.get("gutter_right"))
        print(s)
        return s

if __name__ == '__main__':

    args_parser = ap.ArgumentParser(description='Button table calculations')
    args_parser.add_argument('-s', '--size', type=str, help="Acceptable sizes are: normal, large, xl, square, iphone, and ipad")
    args_parser.add_argument('--height', type=int, default=960)
    args_parser.add_argument('-w', '--width', type=int, default=720)
    args_parser.add_argument('-p', '--portrait', action='store_true', default=False)
    args_parser.add_argument('-l', '--landscape', action='store_true', default=False)
    args_parser.add_argument('--pprint', action='store_true', default=False)
    args = args_parser.parse_args()

    if(not args.pprint):
        print("You should set --pprint.\nExiting.")
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

    g = Gutter(args.width, args.height, args.portrait)

    if(args.pprint):
        g.pprint()
