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

'''Class Icon
Creates Icons used in layouts.
Author: sweetser@alum.mit.edu'''
class Icon():

    def __init__(self, testing=False):
        self.testing = testing

    def home(self, scale=1):
        return ''

    def show_full_screen(self, x, y, scale=1, color=0):
        p = _show_full_screen_preable(self)
        s = _show_full_screen_setup(self, scale, color)
        d = _show_full_screen_draw(self, x, y)

    def _show_full_screen_preamble(self):
        ps = 'PShape ps_sfs;\n'
        return ps

    def _show_full_screen_setup(self, scale, color):
        sfs = var_is_func_string('ps_csg_sfs, 'createShape', 'GROUP')
        sfs += var_is_func_string('ps_cs_1', 'createShape')
        sfs += func_string(

        sfs = 'ps_csg_sfs = createShape(GROUP);\n'
        sfs += 'ps_cs_1 = createShape();\n'
        sfs += 'ps_cs_1.noFill();\n'
        sfs += 'ps_cs_1.stroke(color);\n'
        sfs +=  obj_func_ints_string('ps_cs_1', 'vertex', 0, scale * 2)
        sfs +=  obj_func_ints_string('ps_cs_1', 'vertex', scale * 2, scale * 2)
        sfs +=  obj_func_ints_string('ps_cs_1', 'vertex', scale * 2, 0)
        sfs += 'ps_cs_1.end();\n'
        sfs += 'ps_csg_sfs.addChild(ps_cs_1);\n'
        return sfs 

    def _show_full_screen_draw(self, x, y):
        t = 'translate(x, y);\n'
        t += 'shape(ps_sfs);\n'

    def hide_full_screen(self, scale=1):
        return ''

    def show_rotations(self, scale=1):
        return ''

    def hide_rotations(self, scale=1):
        return ''

    def show_boosts(self, scale=1):
        return ''

    def hide_boosts(self, scale=1):
        return ''

    def x_rotation(self, scale=1):
        return ''

    def y_rotation(self, scale=1):
        return ''

    def z_rotation(self, scale=1):
        return ''

    def xy_rotation(self, scale=1):
        return ''

    def xz_rotation(self, scale=1):
        return ''

    def yz_rotation(self, scale=1):
        return ''

    def x_boost(self, scale=1):
        return ''

    def y_boost(self, scale=1):
        return ''

    def z_boost(self, scale=1):
        return ''

    def setup(self):
        g = Gutter.Gutter(self.height, self.width, self.portrait)
        gb = g.icon_bottom()
        gl = g.left()
        gt = g.icon_top()
        frh = self.icon_height()
        frw = self.icon_width()
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

    def var_is_func_string(self, func, args=''):
        s = var + ' = ' + func + '( '
        if (arg):
            s += args
        s += ');\n'
        return s

    def obj_func_ints_string(self, func, ints):
        s = obj + '.' + func + '( '
        for int in ints:
            s += str(int) + ', '
        s = s[:-2]
        s += ');\n'
        return s

    def func_4_ints_string(self, obj, func, x1, y1, x2, y2):
        s = obj + '.' + func + '( '
        s += str(x1) + ', '
        s += str(y1) + ','
        s += str(x2) + ', '
        s += str(y2) + ')'
        return s

    def ints_2_rect(self, x1, y1, x2, y2):
        s = 'rect( '
        s += str(x1) + ', '
        s += str(y1) + ', '
        s += str(x2) + ', '
        s += str(y2) + ')'
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

    fr = Icon(args.width, args.height, args.portrait)

    if(args.pprint):
        fr.pprint()

    if(args.gui):
        fr.run()
