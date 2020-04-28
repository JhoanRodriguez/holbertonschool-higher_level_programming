#!/usr/bin/python3
for x in range(122, 96, -1):
    if(x % 2 != 0):
        upper = x - 32
    else:
        upper = x
    print("{:c}".format(upper), end="")
