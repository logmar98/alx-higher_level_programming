#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) - 1 == 0:
        chr = "."
    elif len(argv) - 1 == 1:
        chr = ":"
    else:
        chr = "s :"
    print("{} argument{}".format(int(len(argv)) - 1, chr), )
    for i in range(1, int(len(argv))):
        print("{}: {}".format(i, argv[i]))
