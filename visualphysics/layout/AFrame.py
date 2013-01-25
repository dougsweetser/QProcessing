#!/usr/bin/env python3.3

# Copyright 2012 by Douglas Sweetser, sweetser@alum.mit.edu
# Licensed under the Apache License, Version 2.0.

import sys
import collections as co
import argparse as ap

sys.path.append("..")
import Layout
import RunProcessing
import ButtonTable
import Gutter

'''Class AFrame
Calculates sizes needed for Animation Frame used for animation.
Author: sweetser@alum.mit.edu'''
class AFrame(Layout.Layout):

    def __init__(self, d1=640, d2=480, portrait=True, testing=False):
        super().__init__(d1, d2, portrait, testing)
        self.on = True
        self.sizes = co.OrderedDict() 
        self.testing = testing

    def aframe_height(self):
        bt = ButtonTable.ButtonTable(self.height, self.width, self.portrait)
        fh = min(self.app_min, self.app_max - bt.min())
        self.sizes["aframe_height"] = fh
        return fh

    def aframe_width(self):
        bt = ButtonTable.ButtonTable(self.height, self.width, self.portrait)
        fw = min(self.app_min, self.app_max - bt.min())
        self.sizes["aframe_width"] = fw
        return fw

    def sky_height(self):
        fh = self.aframe_height()
        sh = round(fh * 0.6) 
        self.sizes["sky_height"] = sh
        return sh

    def ground_height(self):
        fh = self.aframe_height()
        gh = fh - round(fh * 0.6)
        self.sizes["ground_height"] = gh
        return gh

    def set_sizes(self):
        self.aframe_height()
        self.aframe_width()
        self.sky_height()
        self.ground_height()
        return self.sizes

    def setup(self):
        g = Gutter.Gutter(self.height, self.width, self.portrait)
        gb = g.aframe_bottom()
        gl = g.left()
        gt = g.aframe_top()
        frh = self.aframe_height()
        frw = self.aframe_width()
        sh = self.sky_height()

        s = []
        s.append('rectMode(CORNERS)')
        s.append('fill(100, 200, 100)')
        if (self.portrait):
            r1 = self.ints_2_rect(gb, gl, gb + frw, gl + frh)
            s.append(r1)
            s.append('fill(100, 200, 200)')
            r2 = self.ints_2_rect(gb, gl, gb + frw, gl + sh)
            s.append(r2)
        else:
            r1 = self.ints_2_rect(gl, gt, gl + frw, gt + frh)
            s.append(r1)
            s.append('fill(100, 200, 200)')
            r2 = self.ints_2_rect(gl, gt, gl + frw, gt + sh)
            s.append(r2)
        return s

    def ints_2_rect(self, x1, y1, x2, y2):
        s = 'rect( '
        s += str(x1) + ', '
        s += str(y1) + ', '
        s += str(x2) + ', '
        s += str(y2) + ')'
        return s

    def run(self):
        methods = co.OrderedDict()
        s = super().setup()
        s += self.setup()
        bt = ButtonTable.ButtonTable(self.height, self.width, self.portrait)
        s += bt.setup()
        methods["void_setup():"] = s
        d = self.draw()
        methods["void_draw():"] = d
        runner = RunProcessing.RunProcessing("AFrame", methods, self.testing)
        exit_code = runner.run()
        return exit_code

    def pprint(self):
        self.set_sizes()
        s = "aframe height, width: " + str(self.sizes.get("aframe_height")) + ", " + str(self.sizes.get("aframe_width")) + "\n"
        s += "sky, ground height: " + str(self.sizes.get("sky_height")) + ", " + str(self.sizes.get("ground_height"))
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
             'xl':[480, 800], \
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

    fr = AFrame(args.width, args.height, args.portrait)

    if(args.pprint):
        fr.pprint()

    if(args.gui):
        fr.run()
