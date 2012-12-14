#!/usr/bin/env python3.3

# Copyright 2012 by Douglas Sweetser, sweetser@alum.mit.edu
# Licensed under the Apache License, Version 2.0.

import argparse

'''Class Grid
Used for x and y values used in layouts.
Author: sweetser@alum.mit.edu'''
class Grid:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def simple_print(self):
        result = str(self.x) + " " + str(self.y)
        print(result)
        return result

    def pretty_print(self):
        result = "The grid point is (" + str(self.x) + ", " + str(self.y) + ")."
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

    dl = len(argv)
    if dl % 2 == 1:
        argv.append(0)
    while argv:
        x = argv.pop(0)
        y = argv.pop(0)
        g = Grid(x, y)
        if args.sprint:
            g.simple_print()
        if args.pprint:
            g.pretty_print()

