#!/usr/bin/python3
def safe_print_integer(value):
    try:
        i = int(value)
    except ValueError:
        return False
    print("{:d}".format(i))
    return True

