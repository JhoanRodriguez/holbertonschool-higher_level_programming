#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("0 argument.")
    else:
        print("{:d} arguments:".format(len(sys.argv) - 1))
        for x in range (1, len(sys.argv)):
            print("{:d}: {}".format(x, sys.argv[x]))

