#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):

    # def __init__(self, name, score):
    #     self._name = name
    #     self._score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('Score must be an Integer!')
        if value < 0 or value > 100:
            raise ValueError('Score must between 0 ~ 100 !!')
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2021 - self._birth


class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height


class Animal(object):
    pass


class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class Runnable(object):
    def run(self):
        print('Running....')


class Flyable(object):
    def fly(self):
        print('Flying...')


class Dog(Mammal, Runnable):
    pass


class Bat(Mammal, Flyable):
    pass


class Parrot(Bird, Runnable):
    pass


class Pstrich(Bird, Flyable):
    pass


if __name__ == '__main__':
     # 测试:
    # s = Screen()
    # s.width = 1024
    # s.height = 768
    # print('resolution =', s.resolution)
    # if s.resolution == 786432:
    #     print('测试通过!')
    # else:
    #     print('测试失败!')
    #
    #     s = Screen()
    #
    # brk = 1


    pass
