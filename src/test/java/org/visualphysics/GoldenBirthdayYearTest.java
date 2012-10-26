package org.visualphysics;

import  org.visualphysics.GoldenBirthdayYear;

import  org.junit.Before;
import  org.junit.Test;
import  org.junit.After;
import  static org.junit.Assert.*;

public class GoldenBirthdayYearTest {

    @Test
    public void test_calculate_golden_birthday_year() {

        String the_year = "2008";
        String the_gby = "2016";
        GoldenBirthdayYear gby = new GoldenBirthdayYear(the_year);
        String gby_year = gby.calculate_golden_birthday_year();
        assertEquals(the_gby, gby_year);
    }

    @Test
    public void test_print_golden_birthday_year() {
        String the_year = "2008";
        String the_gby  = "2016";
        boolean pprint = false;
        GoldenBirthdayYear gby = new GoldenBirthdayYear(the_year);
        String gby_year = gby.print_golden_birthday_year(pprint);
        assertEquals(the_gby, gby_year);
    }

    @Test
    public void test_pprint_print_golden_birthday_year() {
        String the_year = "2008";
        String the_pp_gby  = "Since your birth year is 2008, your golden birthday is 2016";
        boolean pprint = true;
        GoldenBirthdayYear gby = new GoldenBirthdayYear(the_year);
        String gby_year = gby.print_golden_birthday_year(pprint);
        assertEquals(the_pp_gby, gby_year);
    }
}

