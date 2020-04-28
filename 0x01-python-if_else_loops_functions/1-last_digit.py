#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if (number < 0):
    last = last * -1
if (last > 5):
    msg = "is greater than 5"
elif (last == 0):
    msg = "is 0"
else:
    msg = "is less than 6 and not 0"
print("Last digit of {:d} is {:d} and {}".format(number, last, msg))
