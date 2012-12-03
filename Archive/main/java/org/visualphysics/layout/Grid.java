/* Copyright 2012 by Douglas Sweetser, sweetser@alum.mit.edu
 * Licensed under the Apache License, Version 2.0
 */

package org.visualphysics.layout;

import com.beust.jcommander.JCommander;
import java.util.ArrayList;
import java.util.List;

/** Class Grid
 *  Used for x and y values used in layouts.
 *  @author sweetser@alum.mit.edu
 */
public class Grid {

    int x;
    int y;

    public Grid(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public String simple_print() {
        String result = Integer.toString(this.x) + " " + Integer.toString(this.y);
        System.out.println(result);
        return result;
    }

    public String pretty_print() {
        String result = "The grid point is (" + Integer.toString(this.x) + ", " + Integer.toString(this.y) + ").";
        System.out.println(result);
        return result;
    }
    
    public static void main(String[] args) {
        GridArgs params = new GridArgs();
        JCommander cmd = new JCommander(params, args);

        if(params.help) {
            System.out.println("usage: Grid.py [-h] [-s] [-p]\n\nPrints a point given two bits of data\n\noptional arguments:\n  -h, --help    show this help message and exit\n  -s, --sprint  Simple print\n  -p, --pprint  Pretty print, more verbose");
        }

        if(params.pprint) {
        }
        else {
            params.sprint = true;
        } 
   
        int dl = params.argv.size();

        if (dl % 2 == 1) {
            params.argv.add(0);
        }

        while (!params.argv.isEmpty()) {
            int x = params.argv.remove(0);
            int y = params.argv.remove(0);
            Grid g = new Grid(x, y);
            if (params.sprint) {
                g.simple_print();
            }
            if (params.pprint) {
                g.pretty_print();
            }
        }        
    }
}
