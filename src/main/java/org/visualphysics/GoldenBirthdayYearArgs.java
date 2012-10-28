package org.visualphysics;

import com.beust.jcommander.Parameter;

public class GoldenBirthdayYearArgs{

    @Parameter(names="-p", required=false, description = "pretty print")
    public boolean pprint = false;
}
