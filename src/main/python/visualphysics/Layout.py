#!/usr/bin/env python3.3

# Copyright 2012 by Douglas Sweetser, sweetser@alum.mit.edu
# Licensed under the Apache License, Version 2.0.

import sys
import collections as co
import argparse as ap

import RunProcessing

'''Class Layout
Super class to organize where things go in the app.
Author: sweetser@alum.mit.edu'''
class Layout:

    global update
    update = True

    def __init__(self, width=480, height=640, testing=False):
        self.width = width
        self.height = height
        if (width > height):
            self.app_max = width
            self.app_min = height
            self.portrait = False
        else:
            self.app_min = height
            self.app_max = width
            self.portrait = True
        self.testing = testing

    def setup(self):
        if (self.portrait):
            result = "size( " + str(self.app_max) + ", " + str(self.app_min) +")"
        else:
            result = "size( " + str(self.app_min) + ", " + str(self.app_max) +")"
        return result

    def draw(self):
        result = "background(100)"
        return result

    def run(self):
        methods = co.OrderedDict()
        methods["def setup():"] = [self.setup()]
        methods["def draw():"] = [self.draw()]
        runner = RunProcessing.RunProcessing("Loyout", methods, self.testing)
        exit_code = runner.run()
        return exit_code

    def pprint(self):
        result = "app_max is: " + str(self.app_max) + "\napp_min is: " + str(self.app_min)
        print(result)
        return result


if __name__ == '__main__':
    args_parser = ap.ArgumentParser(description='Base class for layouts')
    args_parser.add_argument('-s', '--size', type=str, help="Acceptable sizes are: normal, large, xl, square, iphone, and ipad")
    args_parser.add_argument('-g', '--gui', action='store_true', default=False, help="See a box")
    args_parser.add_argument('--height', type=int, default=960)
    args_parser.add_argument('-w', '--width', type=int, default=720)
    args_parser.add_argument('-p', '--portrait', action='store_true', default=False)
    args_parser.add_argument('-l', '--landscape', action='store_true', default=False)
    args_parser.add_argument('--pprint', action='store_true', default=False)
    args = args_parser.parse_args()
    
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

    lay = Layout(args.width, args.height, args.portrait)

    if(args.pprint):
        lay.pprint()

    if(args.gui):
        lay.run()

