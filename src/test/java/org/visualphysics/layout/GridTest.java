/* Copyright 2012 by Douglas Sweetser, sweetser@alum.mit.edu
 * Licensed under the Apache License, Version 2.0
 */

package org.visualphysics.layout;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import org.junit.Before;

import org.visualphysics.layout.Grid;

/** Class GridTest
 *  junit tests
 *  @author sweetser@alum.mit.edu
 */
public class GridTest {

    Grid g;

    @Before
    public void setUp(){
        this.g = new Grid(1, 2);
    }

    @Test
    public void test_x() {
        assertEquals(this.g.x, 1);
    }

    @Test
    public void test_y() {
        assertEquals(this.g.y, 2);
    }

    @Test
    public void test_simple_print() {
        String sp_string = "1 2";
        String sp = this.g.simple_print();
        assertEquals(sp_string, sp);
    }

    @Test
    public void test_pretty_print() {
        String pp_string = "The grid point is (1, 2).";
        String pp = this.g.pretty_print();
        assertEquals(pp_string, pp);
    }
}
