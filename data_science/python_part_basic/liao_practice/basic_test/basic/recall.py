# !/usr/bin/env python3
# -*- coding: utf-8 -*-


def fact(n):
    if n == 1:
        return 1

    return n * fact(n - 1)


def fact2(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


'''
请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，
然后打印出把所有盘子从A借助B移动到C的方法，例如：
'''


def hanoi(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        hanoi(n-1, a, c, b)
        hanoi(1, a, b, c)
        hanoi(n-1, b, a, c)


if __name__ == '__main__':

    hanoi(3, 'A', 'B', 'C')
