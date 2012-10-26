package org.visualphysics;

import  org.visualphysics.Template;

import  org.junit.Before;
import  org.junit.Test;
import  org.junit.After;
import  static org.junit.Assert.*;

public class TemplateTest {

    private Template tplate = new Template();
    
    @Test
    public void testValue() {
        assertEquals(tplate.value, 3);
    }
}

