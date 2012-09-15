/* Copyright 2012 by Douglas Sweetser, sweetser@alum.mit.edu
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at

 *     http://www.apache.org/licenses/LICENSE-2.0

 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or impled.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
// Syntax help: http://en.wikipedia.org/wiki/Java_syntax

package org.visualphysics;

// Imports

/** One line description for Javadoc
 *  @author doug  sweetser@alum.mit.edu
 */
public class Template {

    // Variables: public, protected static...
    protected int value = 3;

    // Constructors
    /** Empty contructor */
    Template() {
        this.value = value;
    }
    /** Constructor with int
      * @param int
      */
    Template(int data) {
        this.value = data;
    }

    // Public methods
    public int getValue() {
        return this.value;
    }

    public void setValue(int value) {
        this.value = value; 
    }

    // Private methods
    public int valueSquared() {
        return this.value * this.value;
    }
}
