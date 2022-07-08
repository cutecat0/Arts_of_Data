#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import threading
import logging

logging.getLogger().setLevel(logging.INFO)


def loop():
    """
    new thread exacute code
    process is combined by threads
    one process has one thread at least
    :return:
    """

    logging.info('thread %s is running...' % threading.current_thread().name)

    n = 0

    while n < 5:
        n += 1

        logging.info('thread %s >>> %s' % (threading.current_thread().name, n))

        time.sleep(1)

    logging.info('thread %s ended.' % threading.current_thread().name)


if __name__ == '__main__':

    logging.info('thread %s is running...' % threading.current_thread().name)

    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()

    logging.info('Thread %s ended.' % threading.current_thread().name)

    # result:
    """
        INFO:root:thread MainThread is running...
        INFO:root:thread LoopThread is running...
        INFO:root:thread LoopThread >>> 1
        INFO:root:thread LoopThread >>> 2
        INFO:root:thread LoopThread >>> 3
        INFO:root:thread LoopThread >>> 4
        INFO:root:thread LoopThread >>> 5
        INFO:root:thread LoopThread ended.
        INFO:root:Thread MainThread ended.
        
        Process finished with exit code 0
    """
