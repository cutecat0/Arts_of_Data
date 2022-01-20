#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import namedtuple
import logging

logging.getLogger().setLevel(logging.INFO)


def namedtuple_test():

    point = namedtuple('point', ['x', 'y'])
    p = point(1, 2)

    logging.info('\npoint is %s.\nx=%s\t y=%s ' % (p, p.x, p.y))


if __name__ == '__main__':

    namedtuple_test()