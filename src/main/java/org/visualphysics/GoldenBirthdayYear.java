/* Copyright 2012 by Douglas Sweetser, sweetser@alum.mit.edu
 * Licensed under the Apache License, Version 2.0.
 */

package org.visualphysics;

import com.beust.jcommander.JCommander;
import java.util.ArrayList;
import java.util.List;

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

    public static void main(String[] args) {
        GoldenBirthdayYearArgs params = new GoldenBirthdayYearArgs();
        JCommander cmd = new JCommander(params, args);

        if(params.help) {
            System.out.println("Calculates the golden birth, which is the birth year added to the birth digits, so someone born in 2004 would have their golden birthday in 2004 + 4 = 2008.\n -p --pprint   pretty print\n -h --help     print help \nHappy birthday, whenever! You have only one of these.");
        }
        for (int i = 0; i < params.argv.size(); i++) {
            GoldenBirthdayYear gby = new GoldenBirthdayYear(params.argv.get(i));
            gby.print_golden_birthday_year(params.pprint);
        }
    }
}


