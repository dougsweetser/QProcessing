package org.visualphysics;

import com.beust.jcommander.Parameter;
import java.util.ArrayList;
import java.util.List;

public class GoldenBirthdayYearArgs{

    @Parameter(names={"-p", "--pprint"}, required=false, description = "pretty print")
    public boolean pprint = false;

    @Parameter(names={"-h", "--help"}, required=false, description = "help info")
    public boolean help = false;

    @Parameter()
    public List<Integer> argv = new ArrayList<Integer>();
}
