#!/usr/bin/env python3

import re
import sys


# 用于查找最高温度的map函数
def f_map():

    for line in sys.stdin:
        val = line.strip()
        year, temp, q = val[15:19], val[87:92], val[92:93]
        if temp != '9999' and re.match('[01459]', q):
            print('%s\t%s' % (year, temp))


# 用于查找最高温度的reduce函数
def f_reduce():

    last_key, max_val = None, -sys.maxint
    for line in sys.stdin:
        key, val = line.strip().split('\t')
        if last_key and last_key != key:
            print('%s\t%s' % (last_key, max_val))
            last_key, max_val = key, int(val)
        else:
            last_key, max_val = key, max(max_val, int(val))
    if last_key:
        print('%s\t%s' % (last_key, max_val))


if __name__ == '__main__':

    f_map()

    f_reduce()

