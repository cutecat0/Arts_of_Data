"""
    Q: How to keep order while U delete elements?
    A: If allof the values are hashable, U can use set or generator to solve the problem.
"""


def delete_same(items):
    """
    This way can only useful while the items can hashable.
    e.g for a list[]
    But when items is a dict{}, it doesn't work.
    """
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def delete_same_v2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


if __name__ == '__main__':
    # a = [1, 2, 6, 3, 9, 1, 10, 0, 1]
    # print(list(delete_same(a)))
    # [1, 2, 6, 3, 9, 10, 0]

    a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
    print(list(delete_same_v2(a, key=lambda d: (d['x'], d['y']))))
    # [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]

    print(list(delete_same_v2(a, key=lambda d: d['x'])))
    # [{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]

    a = [
        {'x': 1, 'y': 2, 'z': 3},
        {'x': 1, 'y': 4, 'z': 6},
        {'x': 1, 'y': 2, 'z': 3},
        {'x': 2, 'y': 2, 'z': 3},
    ]

    b = delete_same_v2(a, key=lambda d: (d['x'], d['y'], d['z']))
    print(list(b))
    # [{'x': 1, 'y': 2, 'z': 3}, {'x': 1, 'y': 4, 'z': 6}, {'x': 2, 'y': 2, 'z': 3}]

    c = delete_same_v2(a, key=lambda d: d['x'])
    print(list(c))
    # [{'x': 1, 'y': 2, 'z': 3}, {'x': 2, 'y': 2, 'z': 3}]

