#!/usr/local/bin/python3

import sys
import argparse
import fileinput

class DemoType:
    def __init__(self, cmd):
        self.cmd = cmd

    def type_cmd(self):
        r = "echo '" + self.cmd + "' | pv -qL 10"
        return r

    def run_cmd(self):
        r = self.cmd
        return r

    def run_demo(self):
        s1 = self.type_cmd()
        s2 = self.run_cmd()
        return s1 + "\n" + s2

if __name__ == '__main__':
    
    args_parser = argparse.ArgumentParser(description='Demo typist when given a file of commands.',epilog='pipe to a shell to run.')
    args_parser.add_argument('-s', '--sleep', dest='sleep', action='store', metavar='N', type=int, default=2, help='time between keystrokes')
    args_parser.add_argument('-f', '--file', dest='file', action='store', metavar='cmds',  default='file', help='file name with commands')
    args = args_parser.parse_args()

    for line in fileinput.input(args.file):
        cmd = line.rstrip()
        dt  = DemoType(cmd)
        out = dt.run_demo()
        print(out)
        s = "sleep " + str(args.sleep)
        print(s)

