#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    mul_val = [val * 2 for val in a_dictionary.values()]

    i = 0
    arr = [list(tu) for tu in a_dictionary.items()]
    for a in arr:
        a[1] = mul_val[i]
        i = i + 1
    new_dict.update(arr)

    return new_dict
