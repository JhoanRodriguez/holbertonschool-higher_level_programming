#!/usr/bin/python3
for x in range(0, 100):
    if (x != 99):
        print("{:0>2d}".format(x), end=", ")
    else:
        print("{:0>2d}".format(x))
