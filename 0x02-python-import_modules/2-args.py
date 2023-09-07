#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 0:
        chr = "."
    else:
        chr = ":"
    print("{} argument{}".format(int(len(argv)) , chr), )
    for i in range(1, int(len(argv))):
        print("{}: {}".format(i, argv[i]))
