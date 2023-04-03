#!usr/bin/env python3
# -*- coding:utf-8 -*-

import logging

logging.getLogger().setLevel(logging.INFO)


class CoroutineTest(object):

    def __init__(self, name):
        """
        协程，又称微线程，纤程。
        英文名Coroutine。
        https://www.liaoxuefeng.com/wiki/1016959663602400/1017968846697824
        the whole process has no lock, excuted by only one thread
        producer and consume worked together, cooperation, which is called Coroutine,
        not the Threads with multi tasks in the way of "knock"
            整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。
            最后套用Donald Knuth的一句话总结协程的特点：“子程序就是协程的一种特例。”
        """
        self._name = name

    def consumer(self):
        r = ''
        while True:
            n = yield r
            if not n:
                return
            logging.info(f'[CONSUMER] Consuming {n}')
            r = '200 ok'

    def produce(self, cons):
        cons.send(None)  # start generator
        n = 0
        while n < 5:
            n += 1
            logging.info(f'[PRODUCER] Producing {n}')
            r = cons.send(n)
            logging.info(f'[PRODUCER] Consumer return {r}')
        cons.close()


if __name__ == '__main__':
    cor = CoroutineTest('Coroutine Test')
    cons = cor.consumer()
    cor.produce(cons)

    """ result is:
    INFO:root:[PRODUCER] Producing 1
    INFO:root:[CONSUMER] Consuming 1
    INFO:root:[PRODUCER] Consumer return 200 ok
    INFO:root:[PRODUCER] Producing 2
    INFO:root:[CONSUMER] Consuming 2
    INFO:root:[PRODUCER] Consumer return 200 ok
    INFO:root:[PRODUCER] Producing 3
    INFO:root:[CONSUMER] Consuming 3
    INFO:root:[PRODUCER] Consumer return 200 ok
    INFO:root:[PRODUCER] Producing 4
    INFO:root:[CONSUMER] Consuming 4
    INFO:root:[PRODUCER] Consumer return 200 ok
    INFO:root:[PRODUCER] Producing 5
    INFO:root:[CONSUMER] Consuming 5
    INFO:root:[PRODUCER] Consumer return 200 ok
    
    Process finished with exit code 0
    
    """

