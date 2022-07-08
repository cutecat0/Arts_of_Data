#!/usr/bin/env python3

def read_file():
    with open('../data/readme.md', 'r') as f:
        f.readline()


def binary_file():
    f = open('../data/hogwarts-legacy-desktop.jpg', 'rb')
    f.readline()

    brk = 1


def char_file():
    f = open('../data/test.txt', 'r', encoding='gbk', errors='ignore')
    f.readline()

    brk = 1


def write_file():
    f = open('../data/test.txt', 'w')
    f.write('Hey, there')
    f.close()
    """
        你可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件。
        当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。
        只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。
        忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。]所以，还是用with语句来得保险：
    """

    with open('../data/test.txt', 'a') as f:
        f.write('I am cat!!!')


if __name__ == '__main__':
    write_file()