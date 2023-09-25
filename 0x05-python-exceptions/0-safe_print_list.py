#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cnt = 0
    for i in my_list:
        try:
            if x == cnt:
                print()
                return cnt
            print("{}".format(i), end="")
            cnt += 1
        except IndexError:
            continue
    print()
    return cnt

