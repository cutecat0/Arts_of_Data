#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

    def __getitem__(self, item):
        if isinstance(item, int):
            a, b, = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start, stop = item.start, item.stop
            if start is None:
                start = 0
            a, b, = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b, = b, a + b
            return L


if __name__ == '__main__':

    for n in Fib():
        print(n)

    brk = 1