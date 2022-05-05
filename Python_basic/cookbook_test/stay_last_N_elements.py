#!/usr/bin/env python36
# -*- coding: utf-8 -*-

from collections import deque


def search(lines, pattern, history=5):
    previous_line = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_line
            previous_line.append(line)


if __name__ == '__main__':
    with open(r'readme.md') as f:
        for line, previous_line in search(f, 'python', 5):
            for pline in previous_line:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)

