#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    sign = {"+": add, "-": sub, "/": div, "*": mul}
    if argv[2] not in sign:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = argv[1]
    b = argv[3]
    print("{} {} {} = {:d}"
          .format(argv[1], argv[2], argv[3], sign[argv[2]](x, y)))
