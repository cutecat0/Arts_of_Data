#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import logging
import itertools

logging.getLogger().setLevel(logging.INFO)


def itertools_test():
    """
    unlimited iterators
    :return:
    """
    naturals = itertools.count(1)

    for n in naturals:
        logging.info(f'number {n}')
        if n == 6:
            break
    # INFO:root:number 1
    # INFO:root:number 2
    # INFO:root:number 3
    # INFO:root:number 4
    # INFO:root:number 5
    # ...
    # INFO:root:number 100

    cyc = itertools.cycle('Simba')
    for c in cyc:
        logging.info(f'cycle string {c}')
        if c == 'a':
            break
    # loop can't stop
    # cycle string m
    # INFO:root:cycle string b
    # INFO:root:cycle string a
    # INFO:root:cycle string S
    # INFO:root:cycle string i
    # INFO:root:cycle string m
    # INFO:root:cycle string b
    # INFO:root:cycle string a
    # INFO:root:cycle string S
    # INFO:root:cycle string i
    # INFO:root:cycle string m

    unlimited_repeat = itertools.repeat('Cat', 6)
    for n in unlimited_repeat:
        logging.info(f'repeat {n}')

    # here use n to point repeat times
    # INFO:root:repeat Cat
    # INFO:root:repeat Cat
    # INFO:root:repeat Cat
    # INFO:root:repeat Cat
    # INFO:root:repeat Cat
    # INFO:root:repeat Cat

    count = itertools.count(1)
    nc = itertools.takewhile(lambda x: x <= 6, count)
    logging.info(f'nc is : {list(nc)}')
    # INFO:root:nc is : [1, 2, 3, 4, 5, 6]

    for c in itertools.chain('Simba', 'Cat'):
        logging.info(f'use chain {c}')
    # INFO:root:use chain S
    # INFO:root:use chain i
    # INFO:root:use chain m
    # INFO:root:use chain b
    # INFO:root:use chain a
    # INFO:root:use chain C
    # INFO:root:use chain a
    # INFO:root:use chain t

    for key, group in itertools.groupby('XXXYYZZZzZAA'):
        logging.info(f'use group by: {key} \t {list(group)}')
    # INFO:root:use group by: X 	 ['X', 'X', 'X']
    # INFO:root:use group by: Y 	 ['Y', 'Y']
    # INFO:root:use group by: Z 	 ['Z', 'Z', 'Z']
    # INFO:root:use group by: z 	 ['z']
    # INFO:root:use group by: Z 	 ['Z']
    # INFO:root:use group by: A 	 ['A', 'A']

    for key, group in itertools.groupby('XxXXxxYYyZZzz', lambda c: c.upper()):
        logging.info(f'use group by ignore upper: {key}\t{list(group)}')
    # INFO:root:use group by ignore upper: X	['X', 'x', 'X', 'X', 'x', 'x']
    # INFO:root:use group by ignore upper: Y	['Y', 'Y', 'y']
    # INFO:root:use group by ignore upper: Z	['Z', 'Z', 'z', 'z']


def pi(N):
    """
    'calculate PI sum N '
    # step 1: create one odd list: 1, 3, 5, 7, 9, ...
    # step 2: take N from step 1 list: 1, 3, 5, 7, 9, ..., 2*N-1.
    # step 3: add + - & use 4 /: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    # step 4: sum :
    return 3.14
    :param N:
    :return:
    """
    # way 1
    result = 0
    for idx, number in enumerate(itertools.takewhile(lambda x: x <= 2*N-1, itertools.count(1, 2))):
        result += (-1)**idx * 4 / number

    return result


if __name__ == '__main__':

    # itertools_test()

    # test
    print(pi(10))
    print(pi(100))
    print(pi(1000))
    print(pi(10000))
    assert 3.04 < pi(10) < 3.05
    assert 3.13 < pi(100) < 3.14
    assert 3.140 < pi(1000) < 3.141
    assert 3.1414 < pi(10000) < 3.1415
    print('ok')