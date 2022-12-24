#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    k = []
    for item in a_dictionary:
        k.append(item)

    k.sort()
    for item in k:
        print("{}: {}".format(item, a_dictionary[item]))
