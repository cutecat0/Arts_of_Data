#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Q: You have a data list, want to get some need value or reduce the length through some rules
    A: Way 1: Simplest way is by the list to get it such as [n for n in data_list if n>0]
       Way 2: Use iterator expression
       Way 3: while rules is too much complex, you can write a special rule function and then put this
              rule function in python inner build filter() function
"""


def get_list_elements():
    # way 1
    lists = [i + 2 for i in range(20)]
    print(lists)
    # [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
    filtered_list = [n for n in lists if n > 6 and n % 3 == 0]
    print(filtered_list)
    # [9, 12, 15, 18, 21]
    """
        ! way 1 disadvantage: if the input data is very large the output would be large either, 
        which will takes too much storage 
        solution: if you're senstive to storage, I suggest you use iterator strongly! 
    """

    # way 2
    pos = (n for n in lists if n > 6 and n % 3 == 0)
    print(pos)  # <generator object get_list_elements.<locals>.<genexpr> at 0x7fbfe98851d0>
    for i in pos:
        print(i, end='\t')
    # 9	12	15	18	21

    # way 3
    data_list = [0, 1, 6, 8, -6, 'N/A', 'NULL', 's-1', 'None']
    need_list = list(filter(rules, data_list))
    print(need_list)
    # [0, 1, 6, 8, -6, '-1']


def rules(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    get_list_elements()

