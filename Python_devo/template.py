#!/usr/bin/env python33

import argparse

class Template:

    def __init__(self, arg):
        self.arg = arg

    def calc(self, pprint):
        if pprint:
            result = "One arg is: " + self.arg
        else:
            result = self.arg
        print(result)
        return result

if __name__ == '__main__':
    args_parser = argparse.ArgumentParser(description='Repeats command line args',epilog='Nothing else.')
    args_parser.add_argument('-p', '--pprint', action='store_true', default=False)
    args_stuff = args_parser.parse_known_args()
    args = args_stuff[0]
    argv = args_stuff[1]
    
    for arg in argv:
        t = Template(arg)
        t.calc(args.pprint)

