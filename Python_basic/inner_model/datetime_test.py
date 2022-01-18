#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
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
    str2dtm = datetime.strptime('2022-01-14 18:08:18', '%Y-%m-%d %H:%M:%S')
    dtm2str = now.strftime('%a, %b %d %H:%M')  # '%a, %b %d %H:%M'

    addtm = now + timedelta(hours=10)
    subtm = now - timedelta(days=1)
    addtmday = now + timedelta(days=2, hours=12)

    logging.info('The pointed time is: %s ' % dt)
    logging.info('Timestamp is: %s ' % dt_timestamp)
    logging.info('Timestamp %s to local Peking datetime is %s ' % (tsp, tsp2dt))
    logging.info('Timestamp %s to UTC datetime is %s ' % (tsp, tsp2utc))
    logging.info('String to datetime is %s ' % str2dtm)
    logging.info('Datetime now %s to string is %s ' % (now, dtm2str))

    logging.info('Now %s add 10 hours is %s ' % (now, addtm))
    logging.info('Now %s sub 1 day is %s ' % (now, subtm))
    logging.info('Now %s add 1 day and 12 hours is %s ' % (now, addtmday))


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
        INFO:root:String to datetime is 2022-01-14 18:08:18 
        INFO:root:Datetime now 2022-01-14 18:06:23.704516 to string is Fri, Jan 14 18:06 
        INFO:root:Now 2022-01-18 11:01:56.574294 add 10 hours is 2022-01-18 21:01:56.574294 
        INFO:root:Now 2022-01-18 11:01:56.574294 sub 1 day is 2022-01-17 11:01:56.574294 
        INFO:root:Now 2022-01-18 11:01:56.574294 add 1 day and 12 hours is 2022-01-20 23:01:56.574294 

        Process finished with exit code 0
    """