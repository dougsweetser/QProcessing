#!/usr/bin/env python3.3

# Copyright 2012 by Douglas Sweetser, sweetser@alum.mit.edu
# Licensed under the Apache License, Version 2.0.

from argparse import ArgumentParser
from os import getcwd 
from os.path import join
from subprocess import check_call

'''Class RunProcessing
Will run processing given setup and draw data.
Author: sweetser@alum.mit.edu'''
class RunProcessing:

    update = True

    def __init__(self, file_root, methods):
        self.file_name = join(getcwd(), file_root + ".processing.py")
        self.methods = methods
        self.path_to_processing_py_jar = join(getcwd(), "processing-py.jar")

    def construct_py(self):
        s = ''
        for method, array_of_strings in self.methods.items():
            s += method + "\n"
            for line in array_of_strings:
                s += "    " + line + "\n"
        return s

    def write_processing_py(self):
        f = open(self.file_name, 'w')
        s = self.construct_py()
        f.write(s)
        f.close()

    def run_processing_py(self):
        check_call(["java", "-jar", self.path_to_processing_py_jar, self.file_name])
        return 0

if __name__ == '__main__':
    args_parser = argparse.ArgumentParser(description='Way to run python classes in processing')
    args_parser.add_argument('-p', '--pprint', action='store_true', default=False)
    args_parser.add_argument('--height', type=int, default=960)
    args_parser.add_argument('-w', '--width', type=int, default=720)
    args = args_parser.parse_args()
    

