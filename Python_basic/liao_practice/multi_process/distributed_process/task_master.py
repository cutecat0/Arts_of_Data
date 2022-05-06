#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import time
import queue
from multiprocessing.managers import BaseManager
import logging


logging.getLogger().setLevel(logging.INFO)

# the queue of send task
task_queue = queue.Queue()

# the queue of recive task
result_queue = queue.Queue()


# from BaseManager implements QueueManager
class QueueManager(BaseManager):
    pass


# register two queues on the net, callable parameter links to Queue Obj
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)

# band port 5000, set check number as 'cat'
manager = QueueManager(address=('', 5000), authkey=b'cat')
# start Queue
manager.start()
# get through net Queue obj
task = manager.get_task_queue()
result = manager.get_result_queue()

# put some tasks into
for i in range(10):
    n = random.randint(0, 10000)
    logging.info('Put task %d...' % n)
    task.put(n)

# read result from result queue
logging.info('Try to get results...')
for i in range(10):
    r = result.get(timeout=10)
    logging.info('Result: %s' % r)

#  close
manager.shutdown()
logging.info('Master closed!!!')


"""
    results:
    INFO:root:Put task 5000...
    INFO:root:Put task 5295...
    INFO:root:Put task 1338...
    INFO:root:Put task 739...
    INFO:root:Put task 3572...
    INFO:root:Put task 8184...
    INFO:root:Put task 8158...
    INFO:root:Put task 842...
    INFO:root:Put task 9586...
    INFO:root:Put task 6877...
    INFO:root:Try to get results...
    INFO:root:Result: 5000 * 5000 = 25000000
    INFO:root:Result: 5295 * 5295 = 28037025
    INFO:root:Result: 1338 * 1338 = 1790244
    INFO:root:Result: 739 * 739 = 546121
    INFO:root:Result: 3572 * 3572 = 12759184
    INFO:root:Result: 8184 * 8184 = 66977856
    INFO:root:Result: 8158 * 8158 = 66552964
    INFO:root:Result: 842 * 842 = 708964
    INFO:root:Result: 9586 * 9586 = 91891396
    INFO:root:Result: 6877 * 6877 = 47293129
    INFO:root:Master closed!!!
    
    Process finished with exit code 0
"""