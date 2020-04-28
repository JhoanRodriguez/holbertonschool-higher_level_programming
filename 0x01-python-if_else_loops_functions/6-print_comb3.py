#!/usr/bin/python3
for x in range(0, 90):
    if (x != 89):
        if (x/10 == x % 10):
            pass
        elif(x / 10 < x % 10):
            print("{:0>2d}".format(x), end=", ")
    else:
        print("{:0>2d}".format(x))
