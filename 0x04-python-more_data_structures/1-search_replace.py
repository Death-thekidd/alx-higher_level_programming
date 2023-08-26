#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_matrix = my_list.copy()

    mod_matrix = [replace if el == search else el for el in new_matrix]
    return mod_matrix
