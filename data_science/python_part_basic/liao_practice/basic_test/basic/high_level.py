# !/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections.abc import Iterator
from functools import reduce


def create_list():
    """
    create a List which contains above numberrs:
    1, 3, 5, 7, 9, 11, ..., 99
    :return:
    """
    L = []
    n = 1
    while n <= 99:
        L.append(n)
        n += 2

    return L


def trim(s):
    """
    利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
    :return:
    """
    if s == '':
        return s
    else:
        if s[0] == ' ' or s[-1] == ' ':  # 首或尾有空格
            if s[0] == ' ':  # 首有空格
                s = s[1:]
                if s[-1] == ' ':  # 尾也有空格
                    s = s[:-1]
            else:  # 仅尾有空格
                s = s[:-1]
            return trim(s)  # 使用递归，预防首尾有多个空格的情况
        else:
            return s


def iteration():
    d1 = {'Gwendolyn': 20, 'Lete': 18}

    for k, v in d1.items():
        print(k, v)


def findMinAndMax(L):
    """
    请使用迭代查找一个list中最小和最大值，并返回一个tuple：
    """
    if len(L) == 0:
        return (None, None)
    if len(L) == 1:
        return (L[0], L[0])
    else:
        min_number, max_number = L[0], L[0]
        for number in L:
            if min_number > number:
                min_number = number
            elif max_number < number:
                max_number = number
            elif min_number == number and max_number == number:
                min_number, max_number = number, number

    return (min_number, max_number)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n += 1
    return 'done'


def fib_generator(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'


def triangles_other():
    L = [1]
    M = [1]
    while True:
        yield L
        M = [L[k - 1] + L[k] if k != 0 else L[k] for k in range(len(M))]
        M.append(1)
        L = M.copy()


def triangles():
    left, middle = [1], [1]
    while True:
        yield left
        middle = [left[k - 1] + left[k] if k != 0 else left[k] for k in range(len(left))]
        middle.append(1)
        left = middle.copy()


def add(x, y, f):
    return f(x) + f(y)


def f(x):
    return x * x


def add2(x, y):
    return x + y


def fn(x, y):
    return x * 10 + y


DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return DIGITS[s]

    return reduce(fn, map(char2num, s))


def str2int2(s):
    def char2num(s):
        return DIGITS[s]

    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


def normalize(name):
    """
    利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
    输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
    """

    return name[0].upper() + name[1:].lower()


def prod(L):
    """Python提供的sum()函数可以接受一个list并求和，
    请编写一个prod()函数，可以接受一个list并利用reduce()求积："""

    def fx(x, y):
        return x * y

    return reduce(fx, L)


def str2float(s):
    """
    # 利用map和reduce编写一个str2float函数
    ，把字符串'123.456'转换成浮点数123.456：
    """

    def str2num(s):
        return DIGITS[s]

    index = s.find('.')

    return reduce(lambda x, y: x * 10 + y, map(str2num, s[:index])) + reduce(lambda x, y: x * 10 + y,
                                                                             map(str2num, s[index + 1:])) / 10 ** index


def isodd(x):
    if x % 2 == 1:
        return x


def not_empty(s):
    return s and s.strip()


# 1. define an odd number start from 3
def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n


# 2. define an filter function
def _not_divisible(n):
    return lambda x: x % n > 0


# 3. as last dedine an iterator to product prime forever
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        filter(_not_divisible(n), it)


def is_palindrome(n):
    """
    回数是指从左向右读和从右向左读都是一样的数，
    例如12321，909。请利用filter()筛选出回数：
    :param n:
    :return:
    """
    return str(n)[::] == str(n)[::-1]


def by_name(t):
    """
    假设我们用一组tuple表示学生名字和成绩：
    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    请用sorted()对上述列表分别按名字排序：
    # -*- coding: utf-8 -*-
    :return:
    """
    return t[1]



    pass


def calsum(*args):
    s = 0
    for n in args:
        s += n
    return s


def lazysum(*args):
    def sum():
        s = 0
        for n in args:
            s += n
        return s
    return sum


if __name__ == '__main__':
    # if trim('hello  ') != 'hello':
    #     print('测试失败!')
    # elif trim('  hello') != 'hello':
    #     print('测试失败!')
    # elif trim('  hello  ') != 'hello':
    #     print('测试失败!')
    # elif trim('  hello  world  ') != 'hello  world':
    #     print('测试失败!')
    # elif trim('') != '':
    #     print('测试失败!')
    # elif trim('    ') != '':
    #     print('测试失败!')
    # else:
    #     print('测试成功!')

    # iteration()

    # isinstance('abc', Iterable)
    # 测试
    # if findMinAndMax([]) != (None, None):
    #     print('测试失败!')
    # elif findMinAndMax([7]) != (7, 7):
    #     print('测试失败!')
    # elif findMinAndMax([7, 1]) != (1, 7):
    #     print('测试失败!')
    # elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    #     print('测试失败!')
    # else:
    #     print('测试成功!')

    # f = fib_generator(10)
    # for n in f:
    #     print(n)

    # 期待输出:
    # [1]
    # [1, 1]
    # [1, 2, 1]
    # [1, 3, 3, 1]
    # [1, 4, 6, 4, 1]
    # [1, 5, 10, 10, 5, 1]
    # [1, 6, 15, 20, 15, 6, 1]
    # [1, 7, 21, 35, 35, 21, 7, 1]
    # [1, 8, 28, 56, 70, 56, 28, 8, 1]
    # [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
    # n = 0
    # results = []
    # for t in triangles():
    #     results.append(t)
    #     n = n + 1
    #     if n == 10:
    #         break
    #
    # for t in results:
    #     print(t)
    #
    # if results == [
    #     [1],
    #     [1, 1],
    #     [1, 2, 1],
    #     [1, 3, 3, 1],
    #     [1, 4, 6, 4, 1],
    #     [1, 5, 10, 10, 5, 1],
    #     [1, 6, 15, 20, 15, 6, 1],
    #     [1, 7, 21, 35, 35, 21, 7, 1],
    #     [1, 8, 28, 56, 70, 56, 28, 8, 1],
    #     [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
    # ]:
    #     print('测试通过!')
    # else:
    #     print('测试失败!')
    # isinstance([], Iterator)
    #
    # isinstance((x for x in range(10)), Iterator)
    #
    # isinstance(iter([]), Iterator)
    #
    # isinstance('abc', Iterator)

    # x, y = 5, -6
    # f = abs
    # res = add(x, y, f)
    # print(res)

    # r = map(f, [x for x in range(10)])
    # print(r)
    # print(list(r))

    # print(list(map(str, [x for x in range(10)])))

    # print(reduce(add2, [x if x % 2 != 0 else 0 for x in range(10)]))

    # print(str2int('32455454'))
    # print(str2int2('135790'))

    # 测试:
    # L1 = ['adam', 'LISA', 'barT']
    # L2 = list(map(normalize, L1))
    # print(L2)

    # print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
    # if prod([3, 5, 7, 9]) == 945:
    #     print('测试成功!')
    # else:
    #     print('测试失败!')

    # print('str2float(\'123.456\') =', str2float('123.456'))
    # if abs(str2float('123.456') - 123.456) < 0.00001:
    #     print('测试成功!')
    # else:
    #     print('测试失败!')

    # print(list(filter(isodd, [x for x in range(10)])))
    # print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

    # for n in primes():
    #     if n < 1000:
    #         print(n)
    #     else:
    #         break
    # 测试:
    # output = filter(is_palindrome, range(1, 1000))
    # print('1~1000:', list(output))
    # if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    #     print('测试成功!')
    # else:
    #     print('测试失败!')

    # 测试:
    # output = filter(is_palindrome, range(1, 1000))
    # print('1~1000:', list(output))
    # if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    #     print('测试成功!')
    # else:
    #     print('测试失败!')
    # print(list(filter(is_palindrome, range(1, 100))))

    # L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    # L2 = sorted(L, key=by_name)
    # print(L2)
    # f = lazysum(1, 3, 5, 7, 9)
    # print(f)
    # print(f())

    pass





















