#!/usr/bin/env perl -w
$|++;

# Copyright 2012 by Douglas Sweetser, sweetser@alum.mit.edu
# Licensed under the Apache License, Version 2.0.

package Visualphysics::Layout::Grid;

sub new {
    my $class = shift;
    my $self = {
        x => shift,
        y => shift
    };
    bless $self, $class;
    return $self;
}

sub simple_print {
    my ($self) = shift @_;

    my $result = "$self->{x} $self->{y}";
    print ("$result\n");
    return $result;
}

sub pretty_print {
    my ($self) = shift @_;

    $result = "The grid point is ($self->{x}, $self->{y}).";
    print("$result\n");
    return $result;
}

main() unless caller;

my $sprint;
my $pprint;

sub main {
    __get_opt();

    while(@ARGV) {
        $x = shift @ARGV;
        $y = shift @ARGV;

        $g = new Visualphysics::Layout::Grid($x, $y);

        if ($sprint) {
            $g->simple_print();
        }
        if ($pprint) {
            $g->pretty_print();
        }
    }
}

sub __get_opt {

    use Getopt::Long;
    $Getopt::Long::autoabbrev = 1;
    $Getopt::Long::ignorecase = 0;

    my $help;
    my $get = GetOptions(
              "sprint!" => \$sprint,
              "pprint!" => \$pprint,
              "help!" => \$help);

    die("Please check the options.\nProgram exiting.\n")
        unless $get;

    my $help_string = qq(

usage: Grid.py [-h] [-s] [-p]

Prints a point given two bits of data

optional arguments:
  -h, --help    show this help message and exit
  -s, --sprint  Simple print
  -p, --pprint  Pretty print, more verbose

);

    $sprint = 1 unless ($pprint);

    if (scalar(@ARGV) % 2) {
        push @ARGV, "0";
    }
}

=head1 NAME
 
VisualPhysics::Layout::Grid - Way to keep grid x and y
 
=head1 SYNOPSIS
 
use $g = new VisualPhysics::Layout::Grid(1, 2);
    $g->simple_print();
    $g->pretty_print();
 
=head1 DESCRIPTION

The way a pair of values are stored for layouts.

=head2 Instance variables

=head3 x

=head3 y

=head2 Functions
 
=head3 simple_print()

Returns the two integers separated by a space:
1 2

=head3 pretty_print()

Returns a more verbose form:
The grid point is (1, 2).

=head1 AUTHOR

sweetser@alum.mit.edu

=head1 LICENSE

Apache 2.0

=cut

1
