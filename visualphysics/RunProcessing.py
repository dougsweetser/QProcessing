#!/usr/bin/env python3.3

# Copyright 2012 by Douglas Sweetser, sweetser@alum.mit.edu
# Licensed under the Apache License, Version 2.0.

import sys
import os
import re
import subprocess as sp
import collections as co
import argparse as ap

'''Class RunProcessing
Will run processing given setup and draw data.
Author: sweetser@alum.mit.edu'''
class RunProcessing:

    def __init__(self, file_root, methods, testing=False):
        dir = os.path.join(os.getcwd(), 'pde', file_root)
        if not os.path.exists(dir):
            os.makedirs(dir)
        self.file_name_pde = os.path.join(dir, file_root + ".pde")
        self.file_name_py = os.path.join(os.getcwd(), 'pde', file_root + ".processing.py")
        self.methods = methods
        self.testing = testing
        cwd_jar = os.path.join(os.getcwd(), "processing-py.jar")
        par_jar = os.path.join(os.pardir, "processing-py.jar")
        if (os.path.isfile(cwd_jar)):
            self.path_to_processing_py_jar = cwd_jar
        elif (os.path.isfile(par_jar)):
            self.path_to_processing_py_jar = par_jar
        else:
            print("Unable to find needed processing-py.jar.\nExiting.")
            sys.exit(1)

    def construct_processing_py(self):
        s = ''
        for method, array_of_strings in self.methods.items():
            mpy = re.sub(r'(^void_)|(^int_)|(^String_)', r'def ', method)
            s += mpy + "\n"
            for line in array_of_strings:
                s += "    " + line + "\n"
        return s

    def construct_processing_pde(self):
        s = ''
        for method, array_of_strings in self.methods.items():
            mj = re.sub(r'_', r' ', method)
            s += re.sub(r':', r'{\n', mj)
            for line in array_of_strings:
                s += "    " + line + ";\n"
            s += "}\n"
        return s

    def write_processing_py(self):
        f = open(self.file_name_py, 'w')
        s = self.construct_processing_py()
        f.write(s)
        f.close()
        return 1

    def write_processing_pde(self):
        f = open(self.file_name_pde, 'w')
        s = self.construct_processing_pde()
        f.write(s)
        f.close()
        return 1

    def run_processing_py(self):
        try:
            if (self.testing):
                error_code = sp.check_call(["java", "-jar", self.path_to_processing_py_jar, self.file_name_py], timeout=10)
            else:
                error_code = sp.check_call(["java", "-jar", self.path_to_processing_py_jar, self.file_name_py])
        except sp.TimeoutExpired as te:
            error_code = 0
        return error_code

    def run(self):
        self.construct_processing_pde()
        self.write_processing_pde()
        self.construct_processing_py()
        self.write_processing_py()
        error_code = self.run_processing_py()
        return error_code


if __name__ == '__main__':
    args_parser = ap.ArgumentParser(description='Way to run python classes in processing')
    args_parser.add_argument('--height', type=int, default=640)
    args_parser.add_argument('-w', '--width', type=int, default=480)
    args_parser.add_argument('-s', '--setup', type=str, nargs='*', help="Add one -s 'line_in_setup():' as needed")
    args_parser.add_argument('-d', '--draw', type=str, nargs='*', help="Add one -d 'line_in_draw():' as needed")
    args = args_parser.parse_args()

    if (not args.setup):
        args.setup = []
        args.setup.append("size( " + str(args.width) + ", " + str(args.height) + ")")

    if (not args.draw):
        args.draw = []
        args.draw.append("background(100)")

    methods = co.OrderedDict()
    methods["void_setup():"] = args.setup
    methods["void_draw():"] = args.draw

    runner = RunProcessing("RunProcessing", methods)
    runner.run()
