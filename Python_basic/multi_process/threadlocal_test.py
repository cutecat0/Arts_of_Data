#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def readme():
    """
    Under multi processing environment, each thread owns its own data
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
