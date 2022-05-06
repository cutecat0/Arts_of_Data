"""
    Q: How to find the same point between two dicts, such as same key or value?
    A: Operating set operation on key or items
"""


def dict_same_point():
    a = {
        'x': 1,
        'y': 2,
        'z': 3,
        'w': 6
    }
    b = {
        'x': 6,
        'y': 2,
        'e': 0
    }

    keys_in_common = a.keys() & b.keys()
    print(keys_in_common)  # {'x', 'y'}

    keys_in_a_not_in_b = a.keys() - b.keys()
    print(keys_in_a_not_in_b)  # {'z'}

    key_value_in_common = a.items() & b.items()
    print(key_value_in_common)  # {('y', 2)}

    c = {key: a[key] for key in a.keys() - {'z', 'w'}}
    print(c)  # {'x': 1, 'y': 2}


if __name__ == '__main__':
    dict_same_point()
