/* Copyright 2012 by Douglas Sweetser, sweetser@alum.mit.edu
 * Licensed under the Apache License, Version 2.0.
 */

package org.visualphysics;

import org.visualphysics.Settings;

/** Description for Javadoc
 *  @author doug  sweetser@alum.mit.edu
 */
public class GoldenBirthdayYear {

    String birthyear;

    public GoldenBirthdayYear(String by) {
        birthyear = by;
    }

    public String calculate_golden_birthday_year() {
        String birth_digits = this.birthyear.substring(2);
        int golden_year_int = Integer.valueOf(birth_digits) + Integer.valueOf(this.birthyear);
        return Integer.toString(golden_year_int);
    }

    public String print_golden_birthday_year(boolean pprint){
        String gby = this.calculate_golden_birthday_year();
        String output;
        if(pprint) {
            output = "Since your birth year is " + this.birthyear + ", your golden birthday is " + gby;
        }
        else {
            output = gby;
        }
        System.out.println(output);
        return output;
    }
}
