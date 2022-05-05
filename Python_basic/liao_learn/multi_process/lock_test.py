#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import threading
import logging

logging.getLogger().setLevel(logging.INFO)

balance = 0
lock = threading.Lock


def change_it(n):

    # save at first, then take off, res should be 0
    global balance
    balance += n
    balance -= n


def run_thread(n):

    for i in range(2000000):
        change_it(n)


# above will make balance can't be 0
# the solution is add lock

def run_thread_lock(n):
    """
    use lock
    :param n:
    :return:
    """

    for i in range(100000):
        # get lock at first
        lock.acquire()
        try:
            # change it whatever u want
            change_it(n)
        finally:
            # after change must release lock
            lock.release()


if __name__ == '__main__':

    t1 = threading.Thread(target=run_thread_lock, args=(5,))
    t2 = threading.Thread(target=run_thread_lock, args=(8,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    logging.info(balance)
