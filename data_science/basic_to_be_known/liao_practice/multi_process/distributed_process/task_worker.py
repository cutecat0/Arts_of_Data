#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import time
import sys
import queue
from multiprocessing.managers import BaseManager


logging.getLogger().setLevel(logging.INFO)


class QueueManager(BaseManager):
    pass


# cause this QueueManager is just get queue from net, only offer name while registering
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')


# connect to server, which is the machine that runs task_master.py
server_addr = '127.0.0.1'
logging.info('Connect to server %s... ' % server_addr)

# attention to the port and checknum is the same as task_master.py totally
m = QueueManager(address=(server_addr, 5000), authkey=b'cat')

# connect to the net
m.connect()

# get Queue object
task = m.get_task_queue()
result = m.get_result_queue()

# get task from task queue and write the result into result queue
for i in range(10):
    try:
        n = task.get(timeout=1)
        logging.info('run task %d * %d... ' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        logging.info('task queue is empty')

# end
logging.info('worker exit.')


"""
    results:
    INFO:root:Connect to server 127.0.0.1... 
    INFO:root:run task 5000 * 5000... 
    INFO:root:run task 5295 * 5295... 
    INFO:root:run task 1338 * 1338... 
    INFO:root:run task 739 * 739... 
    INFO:root:run task 3572 * 3572... 
    INFO:root:run task 8184 * 8184... 
    INFO:root:run task 8158 * 8158... 
    INFO:root:run task 842 * 842... 
    INFO:root:run task 9586 * 9586... 
    INFO:root:run task 6877 * 6877... 
    INFO:root:worker exit.
    
    Process finished with exit code 0
    
"""