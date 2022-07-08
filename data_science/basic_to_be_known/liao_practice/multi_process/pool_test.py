#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os
import random
import time
from multiprocessing import Pool

logging.getLogger().setLevel(logging.INFO)   # logging.info can't display add this sentence


def long_time_task(name):

    logging.info('Run task %s (%s) ... ' % (name, os.getpid()))

    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()

    logging.info('Task %s runs %0.2f seconds. ' % (name, (end - start)))


def process_pool():
    """
        if want to start multi sub processes
    cau use process pool way to create sub processes in batches （mass production）
    :return:
    """

    logging.info('Parent process %s. ' % os.getpid())

    p = Pool(4)

    for i in range(5):
        p.apply_async(long_time_task, args=(i, ))

    logging.info('Waiting for all subprocesses done...')

    p.close()
    """
        use join() function will wait all sub processes run done, 
    but before call join() function, must call close() at first.
    after call close() can't add new Process any more.
    """
    p.join()

    logging.info('All subprocesses done. ')


if __name__ == '__main__':

    process_pool()

    #  the result is:
    """
    INFO:root:Parent process 34679. 
    INFO:root:Waiting for all subprocesses done...
    INFO:root:Run task 0 (34680) ... 
    INFO:root:Run task 1 (34681) ... 
    INFO:root:Run task 2 (34682) ... 
    INFO:root:Run task 3 (34683) ... 
    INFO:root:Task 0 runs 0.33 seconds. [!!!: here after 4 tasks, Task 4 begin to run : we set pool number is 4 ]
    INFO:root:Run task 4 (34680) ... 
    INFO:root:Task 4 runs 0.28 seconds. 
    INFO:root:Task 2 runs 0.81 seconds. 
    INFO:root:Task 1 runs 0.98 seconds. 
    INFO:root:Task 3 runs 1.38 seconds. 
    INFO:root:All subprocesses done.
    """

    """ Hahahahahahahhhahahahaha~~~~~
        Due to the default size of Pool is the core number of your own CPU 
        Unfortunately, if your CPU is 8 cores, then at lease you should submit 9 subprocess can see the above wait result
    """