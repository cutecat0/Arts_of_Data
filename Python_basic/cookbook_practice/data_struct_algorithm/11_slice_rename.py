"""
    Q: There's a lot of slices in your code, U need to clear it. Such as hard decode and so on.
    A: Use slice
"""


def use_slice():
    items = [0, 1, 3, 'cat', 'lovely', 'kitty']
    print(items[2:4])  # [3, 'cat']

    a = slice(2, 4)
    print(items[a])  # [3, 'cat']

    items[a] = ['I', 'am']
    print(items)  # [0, 1, 'I', 'am', 'lovely', 'kitty']

    del items[a]
    print(items)  # [0, 1, 'lovely', 'kitty']

    a = slice(5, 20, 2)
    print(a.start)  # 5
    print(a.stop)  # 20
    print(a.step)  # 2

    s = 'IamLovelyCat'
    b = a.indices(len(s))
    print(b)  # (5, 12, 2)

    for i in range(*b):
        print(s[i])
    # v
    # l
    # C
    # t


if __name__ == '__main__':
    use_slice()

    pass
