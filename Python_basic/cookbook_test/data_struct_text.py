# !/usr/bin/env python36
# -*- coding: utf-8 -*-

import logging
import numpy as np

logging.getLogger().setLevel(logging.INFO)


def unpackValue2obj():
    """
    现在有一个包含 N 个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给 N 个变量？
    解压序列赋值给多个变量
    """
    p = (4, 5)
    x, y = p
    logging.info(f'x = {x}, y = {y}')
    # INFO:root:x = 4, y = 5

    data = ['Simba', 165, 45, (2020, 5, 20)]
    name, height, width, birth = data
    print(name, height, width, birth)
    # Simba 165 45 (2020, 5, 20)

    year, month, day = birth
    print(year, month, day)
    # 2020 5 20

    _, height, weight, _ = data
    print(height, weight)
    # 165 45

    s = "HeyDuck"
    a, b, c, d, e, f, g = s
    print(a, b, c)
    # H e y


def unpackIterableObj2Values():
    """
    解压多个可迭代对象给变量
    """
    record = ('Simba', 'test@test.com', '123-456', '789-1011-121314')
    name, email, *phone = record
    print(name, email, phone)
    # Simba test@test.com ['123-456', '789-1011-121314']

    half_year_data = [i * 10 for i in range(6)]
    *last_5_month, current_month = half_year_data
    last_5_avg = sum(last_5_month) / len(last_5_month)
    print(last_5_avg, current_month)


def drop_first_last(score):
    first, *middle, last = score
    return np.average(middle)


if __name__ == '__main__':
    # unpackValue2obj()

    # score = [i * 10 for i in range(20)]
    # avg = drop_first_last(score)
    # print(avg)

    unpackIterableObj2Values()