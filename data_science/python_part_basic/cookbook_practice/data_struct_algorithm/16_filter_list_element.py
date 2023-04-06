#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Q: You have a data list, want to get some need value or reduce the length through some rules
    A: Simplest way is by the list to get it: way 1
"""


def get_list_elements():
    lists = [i + 2 for i in range(20)]
    print(lists)
    # [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
    filtered_list = [n for n in lists if n > 6 and n % 3 == 0]
    print(filtered_list)
    # [9, 12, 15, 18, 21]


if __name__ == '__main__':
    get_list_elements()

