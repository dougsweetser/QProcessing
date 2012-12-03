#!/usr/bin/env perl -w

use strict;
use FindBin qw($Bin);
use lib "$Bin/../..";
use Test::More tests=>4;
use Visualphysics::Layout::Grid;

my $g = new Visualphysics::Layout::Grid(1, 2);

ok($g->{x} == 1, "test x");
ok($g->{y} == 2, "test y");

my $sp_string = "1 2";
my $sp = $g->simple_print();
ok($sp_string eq $sp, "test simple_print()");

my $pp_string = "The grid point is (1, 2).";
my $pp = $g->pretty_print();
ok($pp_string eq $pp, "test pretty_print()");
