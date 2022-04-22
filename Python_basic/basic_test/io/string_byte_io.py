#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from io import StringIO
from io import BytesIO


def string_io():
    """
    StringIO
    很多时候，数据读写不一定是文件，也可以在内存中读写。
    StringIO顾名思义就是在内存中读写str。
    要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可
    :return:
    """
    f = StringIO()
    f.write('Hey Duck')
    print(f.getvalue())


def read_io():
    f = StringIO('Hey\nHai\nBye!')
    while True:
        s = f.readline()
        if s == '':
            break
        print(s.strip())


def byte_io():
    f = BytesIO()
    f.write('喵喵'.encode('utf-8'))
    print(f.getvalue())


if __name__ == '__main__':

    # string_io()

    # read_io()

    byte_io()