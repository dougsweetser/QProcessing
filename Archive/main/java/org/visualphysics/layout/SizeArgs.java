package org.visualphysics.layout;

import java.util.ArrayList;
import java.util.List;
import com.beust.jcommander.Parameter;
        
public class SizeArgs 
{
    @Parameter(names={"-s", "--sprint"}, required=false, description = "simple print")
    public boolean sprint = false;

    @Parameter(names={"-p", "--pprint"}, required=false, description = "pretty print")
    public boolean pprint = false;

    @Parameter(names={"-h", "--help"}, required=false, description = "help info")
    public boolean help = false;

    @Parameter()
    public List<Integer> argv = new ArrayList<Integer>();
}
