#!/usr/bin/python3
for i in range(97, 123):
    letter = chr(i)
    if letter not in "qe":
        print("{}".format(letter), end='')
