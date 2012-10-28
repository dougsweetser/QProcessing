#!/usr/local/bin/python3

import argparse

class GoldenBirthdayYear:

    def __init__(self, birth_year):
        self.birth_year = birth_year

    def calculate_golden_birthday_year(self):
        birth_digits = self.birth_year % 100
        golden_year_int = self.birth_year + birth_digits
        return golden_year_int

    def print_golden_birthday_year(self, pprint):
        gby = self.calculate_golden_birthday_year()
        if pprint:
            output = "Since your birth year is " + str(self.birth_year) + ", your golden birthday is " + str(gby)
        else:
            output = gby
        print(output)
        return output

if __name__ == '__main__':
    args_parser = argparse.ArgumentParser(description='Calculates the golden birth, which is the birth year added to the birth digits, so someone born in 2004 would have their golden birthday in 2004 + 4 = 2008.',epilog='Happy birthday, whenever! You have only one of these.')
    args_parser.add_argument('-p', '--pprint', action='store_true', default=False)
    args_stuff = args_parser.parse_known_args()
    args = args_stuff[0]
    birthdays = args_stuff[1]
    
    for birthday in birthdays:
        gby = GoldenBirthdayYear(int(birthday))
        gby.print_golden_birthday_year(args.pprint)

