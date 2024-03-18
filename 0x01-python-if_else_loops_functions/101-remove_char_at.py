#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    my_copy = ""
    for c in str:
        if i != n:
            my_copy += c
        i += 1
    return my_copy
