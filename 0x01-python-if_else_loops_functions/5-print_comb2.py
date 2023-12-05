#!/usr/bin/python3

for i in range(0, 100):
    coma = end = ", "
    if i == (100 - 1):
        print("{}".format(str(i).zfill(2)))
    else:
        print("{}{}".format(str(i).zfill(2), coma), end=" ")
