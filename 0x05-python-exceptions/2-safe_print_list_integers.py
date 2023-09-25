#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    cnt = 0
    for i in my_list:
        try:
            if x == cnt:
                print()
                return cnt
            print("{:d}".format(i), end="")
            cnt += 1
        except (TypeError, ValueError, IndexError):
            continue
    print()
    return cnt

