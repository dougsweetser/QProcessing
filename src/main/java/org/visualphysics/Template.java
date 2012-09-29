/* Copyright 2012 by Douglas Sweetser, sweetser@alum.mit.edu
 * Licensed under the Apache License, Version 2.0.
 */

package org.visualphysics;

import org.visualphysics.Settings;

/** Description for Javadoc
 *  @author doug  sweetser@alum.mit.edu
 */
public class Template {

    // Class and instance variables.
    protected int value = 3;

    // Methods
    // Note: store data in Settings for centralization.
    protected void setValue(int value) {
        Settings.testValue = value; 
    }

    protected int valueSquared() {
        return this.value * this.value;
    }
}
