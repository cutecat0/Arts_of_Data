#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta, timezone
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

    tz_utc_8 = timezone(timedelta(hours=8))
    strong2utc = now.replace(tzinfo=tz_utc_8)

    utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
    bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
    tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
    bj2tokyo_dt = bj_dt.astimezone(timezone(timedelta(hours=9)))

    logging.info('The pointed time is: %s ' % dt)
    logging.info('Timestamp is: %s ' % dt_timestamp)
    logging.info('Timestamp %s to local Peking datetime is %s ' % (tsp, tsp2dt))
    logging.info('Timestamp %s to UTC datetime is %s ' % (tsp, tsp2utc))
    logging.info('String to datetime is %s ' % str2dtm)
    logging.info('Datetime now %s to string is %s ' % (now, dtm2str))

    logging.info('Now %s add 10 hours is %s ' % (now, addtm))
    logging.info('Now %s sub 1 day is %s ' % (now, subtm))
    logging.info('Now %s add 1 day and 12 hours is %s ' % (now, addtmday))
    logging.info('Now %s strong to UTC time is %s ' % (now, strong2utc))
    logging.info('Now %s to UTC time is %s ' % (now, utc_dt))
    logging.info('UTC time  %s to Beijing time is %s ' % (utc_dt, bj_dt))
    logging.info('UTC time  %s to Tokyo time is %s ' % (utc_dt, tokyo_dt))
    logging.info('Beijing time  %s to Tokyo time is %s ' % (bj_dt, bj2tokyo_dt))


def to_timestamp(dt_str, tz_str):
    """
    Suppose you get user's input date and time such as 2022-01-18 11:49:22
    and a timezone info such as UTC+5:00
    all are string
    please write one function change them to timestamp
    :param dt_str:
    :param tz_str:
    :return:
    """
    # 1. string to datetime
    # 2. UTC timezone
    # 3. datetime to timestamp

    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    utc_tz = timezone(timedelta(hours=int(tz_str[3:-3])))

    dtm = dt.replace(tzinfo=utc_tz)

    tsp_dt = dtm.timestamp()

    logging.info('Return: %s ' % tsp_dt)

    return tsp_dt


if __name__ == '__main__':

    # test()
    # result:
    """
        INFO:root:Now is: 2022-01-18 11:45:33.236359 
        INFO:root:Type of now is <class 'datetime.datetime'> 
        INFO:root:The pointed time is: 2022-01-14 11:39:00 
        INFO:root:Timestamp is: 1642131540.0 
        INFO:root:Timestamp 1666666666.0 to local Peking datetime is 2022-10-25 10:57:46 
        INFO:root:Timestamp 1666666666.0 to UTC datetime is 2022-10-25 02:57:46 
        INFO:root:String to datetime is 2022-01-14 18:08:18 
        INFO:root:Datetime now 2022-01-18 11:45:33.236359 to string is Tue, Jan 18 11:45 
        INFO:root:Now 2022-01-18 11:45:33.236359 add 10 hours is 2022-01-18 21:45:33.236359 
        INFO:root:Now 2022-01-18 11:45:33.236359 sub 1 day is 2022-01-17 11:45:33.236359 
        INFO:root:Now 2022-01-18 11:45:33.236359 add 1 day and 12 hours is 2022-01-20 23:45:33.236359 
        INFO:root:Now 2022-01-18 11:45:33.236359 strong to UTC time is 2022-01-18 11:45:33.236359+08:00 
        INFO:root:Now 2022-01-18 11:45:33.236359 to UTC time is 2022-01-18 03:45:33.238334+00:00 
        INFO:root:UTC time  2022-01-18 03:45:33.238334+00:00 to Beijing time is 2022-01-18 11:45:33.238334+08:00 
        INFO:root:UTC time  2022-01-18 03:45:33.238334+00:00 to Tokyo time is 2022-01-18 12:45:33.238334+09:00 
        INFO:root:Beijing time  2022-01-18 11:45:33.238334+08:00 to Tokyo time is 2022-01-18 12:45:33.238334+09:00 
        
        Process finished with exit code 0
        
        datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。

        如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。



    """

    # test:
    t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
    assert t1 == 1433121030.0, t1

    t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
    assert t2 == 1433121030.0, t2

    print('ok')
