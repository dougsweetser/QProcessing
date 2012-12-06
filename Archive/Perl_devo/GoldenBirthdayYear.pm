#!/usr/bin/perl -w
$|++;
use strict;
use English;

package GoldenBirthdayYear;

sub new {
    my $class = shift;
    my $self = {
        birth_year => shift
    };
    bless $self, $class;
    return $self;
}

sub calculate_golden_birthday_year {
    my ($self) = @_;
    my $birth_digits = $self->{birth_year} % 100;
    my $golden_year = $self->{birth_year} + $birth_digits;
    return $golden_year;
}

sub print_golden_birthday_year {
    my ($self, $pprint) = @_;
    my $gby = $self->calculate_golden_birthday_year();

    my $output;
    if ($pprint) {
        $output = "Since your birth year is $self->{birth_year}, your golden birthday is $gby";
    }
    else{
        $output = $gby;
    }
    print("$output\n");
    return $output;
}

main() unless caller;

my $pprint;
my @birth_years;

sub main {
    __get_opt();

    while (my $birth_year = shift @birth_years) {
        my $gby = new GoldenBirthdayYear($birth_year);
        $gby->print_golden_birthday_year($pprint);
    }
}

sub __get_opt {

    use Getopt::Long;
        $Getopt::Long::autoabbrev = 1;
        $Getopt::Long::ignorecase = 0;

    # Get options.
    my $help;
    my $get = GetOptions(
           "pprint!" => \$pprint,
           "help!"   => \$help);

    my $help_string = qq(usage: GoldenBirthdayYear.pm [-h] [-p]\n\nCalculates the golden birth, which is the birth year added to the birth digits, so someone born in 2004 would have their golden birthday in 2004 + 4 = 2008.

optional arguments:
  -h, --help    show this help message and exit
  -p, --pprint

Happy birthday, whenever! You have only one of these.
);

    die ("Check options please.\nProgram exiting.\n") unless $get;

    if ($help) {
        print $help_string;
        exit(1);
    }

    foreach my $arg (@ARGV) {
        if ($arg =~ /^\d{4}$/) {
            push @birth_years, $arg;
        }
        else {
            die "Please provide 4 digit years.\nProgram exiting.\n";
        }
    }
}

1
