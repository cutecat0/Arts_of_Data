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

manager.shutdown()
logging.info('Master closed!!!')