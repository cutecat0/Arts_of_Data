#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import math

PIE = 3.14


def circle_area(r):
    area = PIE * r * r

    return area


def f_abs(x):

    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


def f_move(x, y, step, angle=0):

    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)

    return nx, ny


def nop():
    pass


def quadratic(a, b, c):

    delt = (b**2) - (4 * a * c)
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError('Bad operand type')
    if a == 0 or b == 0:
        print('a and b can not be zero!!!')
    if delt == 0:
        return -b / (2 * a)
    if delt < 0:
        return None
    if delt > 0:
        x1 = (-b + math.sqrt(delt)) / (2 * a)
        x2 = (-b - math.sqrt(delt)) / (2 * a)
        return x1, x2


def pr(x):

    return x*x


def npr(x, n):

    s = 1
    while n > 0:
        s *= x
        n -= 1

    return s


def npr2(x, n=2):

    s = 1
    while n > 0:
        s *= x
        n -= 1

    return s


def add_end(L = []):
    L.append('END')
    return L


def add_end2(L=None):

    if L is None:
        L = []

    L.append('END')

    return L


def sumall(numbers):

    s = 0
    for n in numbers:
        s += n ** 2

    return s


def sumall2(*numbers):

    s = 0
    for n in numbers:
        s += n * n

    return s


def kwpara(name, age, **kw):
    print('name: ', name, '\tage: ', age, '\tother: ', kw)


def kwpara2(name, age, **kw):

    if 'pet' in kw:
        pass
    if 'job' in kw:
        pass

    print('name: ', name, '\tage: ', age, '\tother: ', kw)


def kwpara3(name, age, *, pet, job):
    print(name, age, pet, job)


def kwpara4(name, age, *args, pet, job):
    print(name, age, args, pet, job)


def kwpara4(name, age, *, pet='cat', job):
    print(name, age, pet, job)


def kwpara5(name, age, pet, job):
    pass


if __name__ == '__main__':

    # r = 4
    # print(circle_area(r))
    #
    # n1 = 255
    # n2 = 1000
    #
    # hex(n1)

    # print(f_abs(-99))

    # nop()

    # r = f_move(100, 100, 60, math.pi / 6)
    # print(r)

    # 测试:
    # print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
    # print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
    #
    # if quadratic(2, 3, 1) != (-0.5, -1.0):
    #     print('测试失败')
    # elif quadratic(1, 3, -4) != (1.0, -4.0):
    #     print('测试失败')
    # else:
    #     print('测试成功')

    # print(npr2(5))

    # print(add_end2(['x', 'y', 'z']))
    #
    # print(add_end2())
    #
    # print(add_end2())
    #
    # print(add_end2())

    # print(sumall([1, 3, 5, 7]))
    # print(sumall2(1, 2, 3, 5))

    # kwpara('Gwendolyn', 20)
    # kwpara('Harry', 11, city='UK')
    # kwpara('Ron', 12, gender='boy', pet='cat')

    # extra = {'city': 'UK', 'pet': 'cat', 'job': 'Wizard', 'love': 'Magic'}
    # kwpara('Harry', 11, **extra)
    args = ('cat', 'Wizard')
    kwpara4('Harry', 12, )

    pass
