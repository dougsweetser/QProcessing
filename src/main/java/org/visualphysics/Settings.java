/* Copyright 2012 by Douglas Sweetser, sweetser@alum.mit.edu
 * Licensed under the Apache License, Version 2.0 (the "License");
 */

package org.visualphysics;

import org.visualphysics.Settings;

/** Central storage for data.
 *  @author doug  sweetser@alum.mit.edu
 */
public class Settings implements java.io.Serializable {

    // Variables: public, protected static...
    protected static int testValue = 3;

    Settings() {

    }

    Settings(int data) {
        this.testValue = data;
    }
}
