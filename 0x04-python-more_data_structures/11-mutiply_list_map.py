#!/usr/bin/python3
def mutiply_list_map(my_list=None, number=0):
    if my_list is None:
        my_list = []
    return (list(map(lambda i: i * number, my_list)))
