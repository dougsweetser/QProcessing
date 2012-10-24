#!/usr/local/bin/python3

import argparse

class GBY:

    def __init__(self, birth_year):
        self.birth_year = birth_year

    def calculate_golden_birthday_year(self, birth_year):
        birth_digits = birth_year[2:]
        return str(self.num(birth_year) + self.num(birth_digits))

    def print_golden_birthday_year(self, pprint):
        gby = self.calculate_golden_birthday_year(self.birth_year)
        if pprint:
            output = "Since your birth year is " + self.birth_year + ", your golden birthday is " + gby
        else:
            output = gby
        print(output)
        return output

    def num(self, s):
        try:
            return int(s)
        except exceptions.ValueError:
            return float(s)

if __name__ == '__main__':
    args_parser = argparse.ArgumentParser(description='Calculates the golden birth, which is the birth year added to the birth digits, so someone born in 2004 would have their golden birthday in 2004 + 4 = 2008.',epilog='Happy birthday, whenever! You have only one of these.')
    args_parser.add_argument('-p', '--pprint', action='store_true', default=False)
    args_stuff = args_parser.parse_known_args()
    args = args_stuff[0]
    birthdays = args_stuff[1]
    
    for birthday in birthdays:
        gby = GBY(birthday)
        gby.print_golden_birthday_year(args.pprint)

