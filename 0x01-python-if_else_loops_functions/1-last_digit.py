#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastnumber = int(str(number)[-1])
if number < 0:
    lastnumber = -lastnumber
if lastnumber > 5:
    n = "and is greater than 5"
elif lastnumber == 0:
    n = "and is 0"
elif lastnumber < 6:
    n = "and is less than 6 and not 0"
print(f"Last digit of {number} is {lastnumber} {n}")

