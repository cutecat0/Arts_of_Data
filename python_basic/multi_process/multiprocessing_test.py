#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, time, random
from multiprocessing import Pool, Process


def unix_process():
    print('Process (%s) start...' % os.getpid())

    pid = os.fork()
    if pid == 0:
        print(' child process (%s) and parent process is %s. ' % (os.getpid(), os.getpid()))
    else:
        print('(%s) created a child process (%s).' % (os.getpid(), pid))


def windows_process(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':

    # unix_process(

    # windows

    print('Parent process %s.' % os.getpid())
    p = Process(target=windows_process, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

    pass
