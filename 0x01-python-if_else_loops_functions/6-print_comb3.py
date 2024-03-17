#!/usr/bin/python3

for i in range(10):
    for j in range(10):
        if i < j:
            if i != 9 or (i == 9 and j != 10):
                # print(f'{i}{j}', end=" ")
                print("{:d}{:d}".format(i, j), end=", ")
                # print("{:02}".format(i*10 + j), end=" ")
            # else:
            #     print("{:d}{:d}".format(i, j))
print()