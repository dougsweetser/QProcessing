#!/usr/bin/env python3

import unittest
import golden_birthday_year

class GoldenBirthdayYear(unittest.TestCase):

    def setUp(self):
        the_year = 2008
        self.gby = golden_birthday_year.GoldenBirthdayYear(the_year)

    def test_calculate_golden_birthday_year(self):
        the_gby = 2016
        gby_year = self.gby.calculate_golden_birthday_year()
        self.assertEqual(the_gby, gby_year)

    def test_print_golden_birthday_year(self):
        the_gby_string = "2016"
        pprint = False
        gby_year = self.gby.print_golden_birthday_year(pprint)
        self.assertEqual(the_gby_string, gby_year)

    def test_pretty_print_golden_birthday_year(self):
        the_pp_gby  = "Since your birth year is 2008, your golden birthday is 2016"
        pprint = True
        gby_year = self.gby.print_golden_birthday_year(pprint)        
        self.assertEqual(the_pp_gby, gby_year)

if __name__ == '__main__':
    unittest.main()
