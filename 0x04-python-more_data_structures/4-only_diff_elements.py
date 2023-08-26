#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    common = set(filter(lambda x: x not in set_2, set_1))

    for el in set_2:
        if el not in set_1:
            common.add(el)

    return common
