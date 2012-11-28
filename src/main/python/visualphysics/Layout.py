#!/usr/bin/env python3.3

# Copyright 2012 by Douglas Sweetser, sweetser@alum.mit.edu
# Licensed under the Apache License, Version 2.0.

import argparse

'''Class Layout
Super class to organize where things go in the app.
Author: sweetser@alum.mit.edu'''
class Layout:

    update = True

    def __init__(self, dimension_1, dimension_2):
        if (dimension_1 > dimension_2):
            self.app_max = dimension_1
            self.app_min = dimension_2
        else:
            self.app_min = dimension_1
            self.app_max = dimension_2

    def pprint(self):
        result = "app_max is: " + str(self.app_max) + "\napp_min is: " + str(self.app_min)
        print(result)
        return result

    def setup(self):
        result = "size( " + str(self.app_max) + ", " + str(self.app_min) +")"
        return result

if __name__ == '__main__':
    args_parser = argparse.ArgumentParser(description='Base class for layouts')
    args_parser.add_argument('-p', '--pprint', action='store_true', default=False)
    args_parser.add_argument('--height', type=int, default=960)
    args_parser.add_argument('-w', '--width', type=int, default=720)
    args = args_parser.parse_args()
    
    lay = Layout(args.height, args.width)

    lay.pprint()

