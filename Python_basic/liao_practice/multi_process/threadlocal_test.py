#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
import logging

logging.getLogger().setLevel(logging.INFO)

# create global ThreadLocal obj
local_animal = threading.local()


def readme():
    """
    Under multi processing environment, each thread owns its own data_science
    One thread use its local value is better than use global value,
    because local value can be seen only by thread itself, which can
    not "trouble' other threads
    While global value must add lock
    But local variable can also has problem, which is while function calling
    transport would be so much trouble...
    :return:
    """
    pass


class Cat(object):

    def __init__(self, name):
        self._name = name


def process_cat(name):
    cat = Cat(name)
    # cat here is local variable but every function needs to use it, so must be passed in
    do_task_1(cat)
    do_task_2(cat)


def do_task_1(cat):
    do_subtask_1(cat)
    do_subtask_2(cat)


def do_task_2(cat):
    do_subtask_2(cat)
    do_subtask_2(cat)


def do_subtask_1(cat):
    pass


def do_subtask_2(cat):
    pass


# How can I always use one parameter to pass and pass!!!
# And how could U tolerate to do in such a slow way !!!

# What about  if use one global variable dict to put all Cat object,
# then make thread itself as key to get thread Cat object ???

global_dict = {}


def cat_thread(name):
    cat = Cat(name)
    # put cat variable into global variable global_dict
    global_dict[threading.current_thread()] = cat
    do_task_1()
    do_task_2()


def do_task_1():
    # without pass cat while according current thread to find
    cat = global_dict[threading.current_thread()]


def do_task_2():
    # any function can be able to find current cat variable
    cat = global_dict[threading.current_thread()]


# the above way is a little bit ...
# Here we comes to the ThreadLocal, which doesn't need to find dict, it can do it automatically
def process_new_cat():
    # get current thread locking cat
    cat = local_animal.cat
    logging.info('Hey, %s (in %s) ' % (cat, threading.current_thread().name))


def process_new_thread(name):
    # packing cat of ThreadLocal
    local_animal.cat = name
    process_new_cat()


if __name__ == '__main__':

    # cat_thread('Dolyn')

    t1 = threading.Thread(target=process_new_thread, args=('Tom', ), name='Thread-A')
    t2 = threading.Thread(target=process_new_thread, args=('Jerry', ), name='Thread-B')

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    # result:
    """
        INFO:root:Hey, Tom (in Thread-A) 
        INFO:root:Hey, Jerry (in Thread-B) 

    """