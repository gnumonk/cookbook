#!/usr/bin/python

data = ['ACME', 50, 91.1, (2012, 12, 21)]

name, shares, price, date = data
print('%s %d %f %s') % (name, shares, price, date)
