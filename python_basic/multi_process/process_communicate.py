#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Process, Queue
import os
import time
import random
import logging

logging.getLogger().setLevel(logging.INFO)

"""
    Between Process the communication is one important part
"""


def write(q):

    logging.info('Process to write: %s ' % os.getpid())
    for value in ['A', 'B', 'C']:
        logging.info('Put %s to queue ... ' % value)
        q.put(value)
        time.sleep(random.random())


def read(q):

    logging.info('Process to read: %s ' % os.getpid())

    while True:
        value = q.get(True)

        logging.info('Get %s from queue.' % value)


if __name__ == '__main__':

    # Parent Process create Queue and pass to each subprocess
    q = Queue()
    pw = Process(target=write, args=(q, ))
    pr = Process(target=read, args=(q, ))

    # start subprocess pw to write in
    pw.start()

    # start subprocess pr to read in
    pr.start()

    # wait pw end
    pw.join()

    # pr process is dead loop, can not wait it to end, kill it
    pr.terminate()

    # result:
    """ 
        INFO:root:Process to write: 37944
        INFO:root:Put A to queue ...
        INFO:root:Process to read: 37945
        INFO:root:Get A from queue.
        INFO:root:Put B to queue ...
        INFO:root:Get B from queue.
        INFO:root:Put C to queue ...
        INFO:root:Get C from queue.
        
        Process finished with exit code 0

    """


