#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):
    # count = 0
    # __slots__ = ('name', 'age')    # limit only name, age parameters, add other can not

    def __init__(self, name, score=99, gender='Female'):
        self.__name = name
        self.__score = score
        self.__gender = gender

    def __str__(self):
        return 'Student object (name: %s)' % self.__name

    def __getattr__(self, item):
        if item == 'age':
            return lambda: 23
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % item)

    def __call__(self):
        print('My name is %s. ' % self.__name)

    def print_score(self):
        print("%s %s " % (self.__name, self.__score))
    __repr__ = __str__

    def grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score!!!')

    def set_gender(self, gender):
        self.__gender = gender

    def get_gender(self):
        return self.__gender


class Animal(object):

    def run(self):
        print('Animal is running...')


class Dog(Animal):

    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


class Cat(Animal):

    def run(self):
        print('Cat is running...')


class Tortoise(Animal):

    def run(self):
        print('Tortoise is running slowly...')


def run_twice(animal):
    animal.run()
    animal.run()


if __name__ == '__main__':

    # jerry = Student('Jerry', 90)
    # jerry.print_score()
    # print(jerry.grade())
    #
    # tom = Student('Tom', 88)
    # tom.print_score()
    # print(tom.grade())

    # dog = Dog()
    # dog.run()
    #
    # cat = Cat()
    # cat.run()

    # run_twice(Animal())
    #
    # run_twice(Dog())
    #
    # run_twice(Cat())

    # run_twice(Tortoise())
    print(Student('Jerry'))

    pass