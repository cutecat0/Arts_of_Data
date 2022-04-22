#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools
import time


def log(func):
    def wrapper(*args, **kw):
        print('call %s(): ' % func.__name__)
        return func(*args, **kw)
    return wrapper


def log_v2(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s(): ' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log
def now():
    """
    use @log here is a decorator
    which means now = log(now) here
    :return:
    """
    print('2021-12-17')


@log_v2('excute')
def now_2():
    print('Today is 2021-12-17, Have a nice day')


def log_v3(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s(): ' % func.__name__)
        return func(*args, **kw)
    return wrapper()


def log_v4(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s(): ' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


def metric(fn):
    """
    请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
    :param fn:
    :return:
    """
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        print('%s executed in %s ms' % (fn.__name__, 10.24))
        return fn(*args, **kw)
    return wrapper


@log
def f():
    """
    请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
    再思考一下能否写出一个@log的decorator，使它既支持：
    @log
    def f():
        pass
    又支持：
    @log('execute')
    def f():
        pass
"""
    pass


@log('execute')
def f():
    pass


if __name__ == '__main__':

    # f = now_2
    # print(f.__name__)
    # f()

    # 测试
    # @metric
    # def fast(x, y):
    #     time.sleep(0.0012)
    #     return x + y;
    #
    # @metric
    # def slow(x, y, z):
    #     time.sleep(0.1234)
    #     return x * y * z;
    #
    # f = fast(11, 22)
    # s = slow(11, 22, 33)
    # if f != 33:
    #     print('测试失败!')
    # elif s != 7986:
    #     print('测试失败!')
    pass
