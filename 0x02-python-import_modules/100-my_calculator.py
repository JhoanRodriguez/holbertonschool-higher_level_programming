#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    sign = {"+": add, "-": sub, "/": div, "*": mul}
    if sys.argv[2] not in sign:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = sys.argv[1]
    b = sys.argv[3]
    print("{} {} {} = {:d}"
          .format(sys.argv[1], sys.argv[2], sys.argv[3], sign[sys.argv[2]](int(a), int(b))))
