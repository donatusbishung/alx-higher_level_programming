#!/usr/bin/python3

for i in range(9):
    for j in range(10):
        if i < j:
            if i != 8 or (i == 8 and j != 9):
                # print(f'{i}{j}', end=" ")
                print("{:d}{:d}".format(i, j), end=", ")
                # print("{:02}".format(i*10 + j), end=" ")
            else:
                print("{:d}{:d}".format(i, j))