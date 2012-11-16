/* Copyright 2012 by Douglas Sweetser, sweetser@alum.mit.edu
 * Licensed under the Apache License, Version 2.0
 */

package org.visualphysics.layout;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import org.junit.Before;

import org.visualphysics.layout.Size;

/** Class SizeTest
 *  junit tests
 *  @author sweetser@alum.mit.edu
 */
public class SizeTest {

    Size foo;

    @Before
    public void setUp(){
        this.foo = new Size(1);
    }

    @Test
    public void test_s() {
        assertEquals(this.foo.s, 1);
    }

    @Test
    public void test_simple_print() {
        String sp_string = "1";
        String sp = this.foo.simple_print();
        assertEquals(sp_string, sp);
    }

    @Test
    public void test_pretty_print() {
        String pp_string = "The size is: 1.";
        String pp = this.foo.pretty_print();
        assertEquals(pp_string, pp);
    }
}
