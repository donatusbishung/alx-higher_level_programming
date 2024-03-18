#!/usr/bin/python3
def uppercase(str):
    for character in range(len(str)):
        if ord(str[character]) >= 97 and ord(str[character]) <= 122:
            number = 32
        else:
            number = 0
        print("{:c}".format(ord(str[character]) - number), end="")
    print()
