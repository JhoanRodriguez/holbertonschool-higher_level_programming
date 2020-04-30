#!/usr/bin/python3.4
if __name__ == "__main__":
    from hidden_4 import *
    for x in dir():
        if x[:2] != "__":
            print("{}".format(x))
