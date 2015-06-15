#!/usr/bin/python

# Problem
# You have an N-element tuple or sequence that you would like to unpack into a collection of N variables.

data = ['ACME', 50, 91.1, (2012, 12, 21)]

name, shares, price, date = data
print('%s %d %f %s') % (name, shares, price, date)
