#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cp_list = my_list[:]
    if idx < 0:
        return (cp_list)

    length = len(cp_list)

    if idx > length - 1:
        return (cp_list)
    cp_list[idx] = element
    return (cp_list)
    