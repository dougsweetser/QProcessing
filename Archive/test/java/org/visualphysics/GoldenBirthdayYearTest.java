package org.visualphysics;

import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.assertEquals;
import org.visualphysics.GoldenBirthdayYear;

public class GoldenBirthdayYearTest {

    GoldenBirthdayYear gby;

    @Before
    public void setUp() {
        int the_year = 2008;
        this.gby = new GoldenBirthdayYear(the_year);
    }

    @Test
    public void test_calculate_golden_birthday_year() {
        int the_gby = 2016;
        int gby_year = this.gby.calculate_golden_birthday_year();
        assertEquals(the_gby, gby_year);
    }

    @Test
    public void test_print_golden_birthday_year() {
        String the_gby_string  = "2016";
        boolean pprint = false;
        String gby_year = this.gby.print_golden_birthday_year(pprint);
        assertEquals(the_gby_string, gby_year);
    }

    @Test
    public void test_pprint_print_golden_birthday_year() {
        String the_pp_gby  = "Since your birth year is 2008, your golden birthday is 2016";
        boolean pprint = true;
        String gby_year = this.gby.print_golden_birthday_year(pprint);
        assertEquals(the_pp_gby, gby_year);
    }
}

