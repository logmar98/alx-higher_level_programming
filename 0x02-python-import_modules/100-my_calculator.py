#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, div, mul
    count = len(argv) - 1
    if count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])
    match operator:
        case "+":
            print("{} {} {} = {}".format(a, operator, b, add(a, b)))
        case "-":
            print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
        case "*":
            print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
        case "/":
            print("{} {} {} = {}".format(a, operator, b, div(a, b)))
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
