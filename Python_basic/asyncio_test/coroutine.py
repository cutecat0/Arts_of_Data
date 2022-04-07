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
        cons.send(None)
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

