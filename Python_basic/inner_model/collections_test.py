#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import namedtuple, deque, defaultdict, OrderedDict, ChainMap
import logging
import os, argparse

logging.getLogger().setLevel(logging.INFO)
PI = 3.14


def namedtuple_test():

    point = namedtuple('point', ['x', 'y'])
    p = point(1, 2)

    logging.info('\npoint is %s.\nx=%s\t y=%s ' % (p, p.x, p.y))
    logging.info(f'Is Point a subclass of tuple? {isinstance(p, point)}')
    logging.info(f'Is Point a subclass of tuple? {isinstance(p, tuple)}')

    Circle = namedtuple('Circle', ['x', 'y', 'r'])
    c = Circle(1, 2, 3)
    area = c.r * c.r * PI

    logging.info(f'Circle: x={c.x}\ty={c.y}\tr={c.r}\tarea={area}')


def deque_test():
    q = deque(['a', 'b', 'c'])
    q.append('x')
    q.appendleft('y')

    logging.info(f'deque is {q}')
    # INFO:root:deque is deque(['y', 'a', 'b', 'c', 'x'])


def defaultdict_test():
    """
    While U use dict if there is no key, it would be a KeyError err
    If U want returns a default value without err
    U can use defaultdict
    :return:
    """
    dd = defaultdict(lambda: 'N/A')  # key not in dict returns default value is 'N/A'
    dd['key'] = 'cat'

    logging.info(f'key in  {dd["key"]}')
    logging.info(f'keys not in {dd["key2"]}')
    # INFO:root:key in  cat
    # INFO:root:keys not in N/A


def ordereddict_test():
    """
    When U use dict, the key is unordered,
    while do iterator on a dict, we can't make sure what's its order of keys
    If keep the order of Key, U can use OrderedDict
    :return:
    """
    d = dict([('animal', 1), ('book', 2), ('cat', 3)])

    logging.info(f'dict d is : {d}')

    od = OrderedDict(d)
    od['a'], od['b'], od['c'] = 1, 2, 3

    logging.info(f'Oderded dict od is : {od}')

    # INFO:root:dict d is : {'animal': 1, 'book': 2, 'cat': 3}
    # INFO:root:Oderded dict od is : OrderedDict([('animal', 1), ('book', 2), ('cat', 3)])
    # INFO:root:Oderded dict od is : OrderedDict([('animal', 1), ('book', 2), ('cat', 3), ('a', 1), ('b', 2), ('c', 3)])


class FirstInFirstOutDict(OrderedDict):

    def __init__(self, capacity):
        super(FirstInFirstOutDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        """
        OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
        :param key:
        :param value:
        :return:
        """
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
        if containsKey:
            del self[key]
            logging.info(f'set: {(key, value)}')
        else:
            logging.info(f'add: {(key, value)}')

        OrderedDict.__setitem__(self, key, value)


def chainmap_test():
    """
    ChainMap can connect a group of dict make it be a logically dict
    ChainMap itself is a dict, but while searching, it can search in inner dict in ordered order
    :return:
    """
    defaults = {
        'animal': 'cat',
        'user': 'Simba'
    }

    # command line parameters
    parser = argparse.ArgumentParser()


if __name__ == '__main__':

    # namedtuple_test()

    # result:
    """
        INFO:root:
        point is point(x=1, y=2).
        x=1	 y=2 
        INFO:root:Is Point a subclass of tuple? True
        INFO:root:Is Point a subclass of tuple? True
        INFO:root:Circle: x=1	y=2	r=3	area=28.26
        
        Process finished with exit code 0

    """

    # deque_test()

    # defaultdict_test()

    # ordereddict_test()

    fifo = FirstInFirstOutDict(6)
