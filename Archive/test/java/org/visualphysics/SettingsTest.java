package org.visualphysics;

import  org.visualphysics.Settings;
import  org.junit.Test;
import  static org.junit.Assert.*;

public class SettingsTest {

    private Settings s = new Settings();
    
    @Test
    public void testValue() {
        assertEquals(s.testValue, 3);
    }
}

