#!/usr/local/bin/python3

import argparse

class Template:

    def __init__(self, datum):
        self.datum = datum

    def calc(self, pprint):
        if pprint:
            result = "One arg is: " + self.datum
        else:
            result = self.datum
        print(result)
        return result

if __name__ == '__main__':
    args_parser = argparse.ArgumentParser(description='Repeats command line args',epilog='Nothing else.')
    args_parser.add_argument('-p', '--pprint', action='store_true', default=False)
    args_stuff = args_parser.parse_known_args()
    args = args_stuff[0]
    data = args_stuff[1]
    
    for datum in data:
        t = Template(datum)
        t.calc(args.pprint)

