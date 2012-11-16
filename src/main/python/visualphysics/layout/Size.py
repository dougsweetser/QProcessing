#!/usr/bin/env python3.3

# Copyright 2012 by Douglas Sweetser, sweetser@alum.mit.edu
# Licensed under the Apache License, Version 2.0.

import argparse

'''Class Size
Used for pixel sizes used in layouts.
Author: sweetser@alum.mit.edu'''
class Size:

    def __init__(self, s=0):
        self.s = s

    def simple_print(self):
        result = str(self.s)
        print(result)
        return result

    def pretty_print(self):
        result = "The size is: " + str(self.s) + "."
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
        foo_size = Size(s)
        if args.sprint:
            foo_size.simple_print()
        if args.pprint:
            foo_size.pretty_print()

