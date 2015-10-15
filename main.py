#!/usr/bin/env python

# Command line script to convert a single number to and from several units

import argparse

from src.convert import kilometers_to_miles, miles_to_kilometers, years_to_minutes, minutes_to_years

#Parse command line args
parser = argparse.ArgumentParser()
parser.add_argument('value', type=float, help="The number to be converted")
args = parser.parse_args()

#Perform conversions
# km to mi
to_miles = kilometers_to_miles(args.value)
print("{0} kilometers is {1} miles".format(args.value, to_miles))

# mi to km
to_km = miles_to_kilometers(args.value)
print("{0} miles is {1} kilometers".format(args.value, to_km))

# years to minutes
to_minutes = years_to_minutes(args.value)
print("{0} years is {1} minutes".format(args.value, to_minutes))

# minutes to years
to_years = minutes_to_years(args.value)
print("{0} minutes is {1} years".format(args.value, to_years))


