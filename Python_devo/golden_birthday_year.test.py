#!/usr/local/bin/python3

import unittest
import golden_birthday_year

class TestStuff(unittest.TestCase):

    def test_num(self):
        gby = golden_birthday_year.GBY(2008)
        n_string = '11'
        gby_num = gby.num(n_string)
        self.assertEqual(gby_num, 11)

    def test_calculate_golden_birthday_year(self):
        the_year = "2008"
        the_gby  = "2016"
        gby = golden_birthday_year.GBY(2008)
        gby_year = gby.calculate_golden_birthday_year(the_year)
        self.assertEqual(the_gby, gby_year)

    def test_print_golden_birthday_year(self):
        the_year = "2008"
        the_gby  = "2016"
        pprint = False
        gby = golden_birthday_year.GBY(the_year)
        gby_year = gby.print_golden_birthday_year(pprint)
        self.assertEqual(the_gby, gby_year)

    def test_pretty_print_golden_birthday_year(self):
        the_year = "2008"
        the_pp_gby  = "Since your birth year is 2008, your golden birthday is 2016"
        pprint = True
        gby = golden_birthday_year.GBY(the_year)
        gby_year = gby.print_golden_birthday_year(pprint)        
        self.assertEqual(the_pp_gby, gby_year)

if __name__ == '__main__':
    unittest.main()
