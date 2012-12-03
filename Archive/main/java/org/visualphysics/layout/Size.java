/* Copyright 2012 by Douglas Sweetser, sweetser@alum.mit.edu
 * Licensed under the Apache License, Version 2.0
 */

package org.visualphysics.layout;

import java.util.ArrayList;
import java.util.List;
import com.beust.jcommander.JCommander;

/** Class Size
 *  Used for x and y values used in layouts.
 *  @author sweetser@alum.mit.edu
 */
public class Size 
{
    int s;

    public Size(int s) 
    {
        this.s = s;
    }

    public String simple_print() 
    {
        String result = Integer.toString(this.s);
        System.out.println(result);
        return result;
    }

    public String pretty_print() 
    {
        String result = "The size is: " + Integer.toString(this.s) + ".";
        System.out.println(result);
        return result;
    }
    
    public static void main(String[] args) 
    {
        SizeArgs params = new SizeArgs();
        JCommander cmd = new JCommander(params, args);

        if(params.help) 
        {
            System.out.println("usage: Size.java [-h] [-s] [-p]\n\nPrints a size.\n\noptional arguments:\n  -h, --help    show this help message and exit\n  -s, --sprint  Simple print\n  -p, --pprint  Pretty print, more verbose");
        }

        if(params.pprint) 
        {
        }
        else 
        {
            params.sprint = true;
        } 
   
        while (!params.argv.isEmpty()) 
        {
            int s = params.argv.remove(0);
            Size foo = new Size(s);
            if (params.sprint) 
            {
                foo.simple_print();
            }
            if (params.pprint) 
            {
                foo.pretty_print();
            }
        }        
    }
}
