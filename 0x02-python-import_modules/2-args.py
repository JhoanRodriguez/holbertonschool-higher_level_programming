#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("{:d} argument:".format(len(sys.argv) - 1))
        print("{:d}: {}".format(1, sys.argv[1]))
    else:
        print("{:d} arguments:".format(len(sys.argv) - 1))
        for x in range(1, len(sys.argv)):
            print("{:d}: {}".format(x, sys.argv[x]))
