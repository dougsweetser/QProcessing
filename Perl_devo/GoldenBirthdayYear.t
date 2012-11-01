#!/usr/bin/perl -w

use strict;
use Test::More tests => 3;
use GoldenBirthdayYear;
use FindBin qw($Bin);
use lib "$Bin";

my $the_year = "2008";
my $the_gby  = "2016";
my $gby = new GoldenBirthdayYear($the_year);
my $gby_year = $gby->calculate_golden_birthday_year();
ok($the_gby == $gby_year);

my $pprint = '';
$gby_year = $gby->print_golden_birthday_year($pprint);
ok($the_gby == $gby_year);

my $the_pp_gby  = "Since your birth year is 2008, your golden birthday is 2016";
$pprint = 1;
$gby_year = $gby->print_golden_birthday_year($pprint);
ok($the_pp_gby eq $gby_year);


