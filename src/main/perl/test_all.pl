#!/usr/bin/env perl -w

use Test::Harness;
use File::Find;
use FindBin qw($Bin);

my @test_files;

find(sub{push @test_files, $File::Find::name if ($File::Find::name =~ /\.t$/)}, $Bin);
$Test::Harness::verbose = 1;
runtests(@test_files);
