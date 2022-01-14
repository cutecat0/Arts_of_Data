#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import logging


logging.getLogger().setLevel(logging.INFO)


def test():
    """
    timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
    对应的北京时间是：
    timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00
    :return:
    """
    now = datetime.now()

    logging.info('Now is: %s ' % now)
    logging.info('Type of now is %s ' % type(now))

    dt = datetime(2022, 1, 14, 11, 39)
    dt_timestamp = dt.timestamp()

    tsp = 1666666666.0
    tsp2dt = datetime.fromtimestamp(tsp)  # local time
    tsp2utc = datetime.utcfromtimestamp(tsp)  # UTC time

    logging.info('The pointed time is: %s ' % dt)
    logging.info('Timestamp is: %s ' % dt_timestamp)
    logging.info('Timestamp %s to local Peking datetime is %s ' % (tsp, tsp2dt))
    logging.info('Timestamp %s to UTC datetime is %s ' % (tsp, tsp2utc))


if __name__ == '__main__':

    test()
    # result:
    """
        INFO:root:Now is: 2022-01-14 11:37:59.570007 
        INFO:root:Type of now is <class 'datetime.datetime'> 
        INFO:root:The pointed time is: 2022-01-14 11:39:00 
        INFO:root:Timestamp is: 1642131540.0 
        INFO:root:Timestamp 1666666666.0 to datetime is 2022-10-25 10:57:46 
        INFO:root:Timestamp 1666666666.0 to UTC datetime is 2022-10-25 02:57:46 

    """