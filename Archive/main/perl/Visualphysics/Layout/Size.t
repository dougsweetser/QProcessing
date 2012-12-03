#!/usr/bin/env perl -w

use strict;
use FindBin qw($Bin);
use lib "$Bin/../..";
use Test::More tests=>3;
use Visualphysics::Layout::Size;

my $foo = new Visualphysics::Layout::Size(1, 2);

ok($foo->{s} == 1, "test s");

my $sp_string = "1";
my $sp = $foo->simple_print();
ok($sp_string eq $sp, "test simple_print()");

my $pp_string = "The size is: 1.";
my $pp = $foo->pretty_print();
ok($pp_string eq $pp, "test pretty_print()");
