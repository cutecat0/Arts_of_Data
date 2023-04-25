#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Q: U want to creat a dict which is the subset of another dict?
    A: The simplest way is to use dict push to another dict

"""


def get_subset_dict():
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }

    # Make a dictionary of all prices over 200
    p1 = {key: value for key, value in prices.items() if value > 200}
    print(p1)
    # {'AAPL': 612.78, 'IBM': 205.55}

    names = ['IBM', 'HPQ', 'FB']
    p2 = {key: value for key, value in prices.items() if key in names}
    print(p2)
    # {'IBM': 205.55, 'HPQ': 37.2, 'FB': 10.75}


if __name__ == '__main__':
    get_subset_dict()