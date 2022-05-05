from collections import defaultdict


"""
    Q: Dict key maps to different many values?
    A: Put values into other "containers"
"""


def dict_key_to_values():

    dict_0 = {
        'animal': ['cat', 'dog', 'rabbit'],  # use list [] to keep order insert
        'vegetable': [1, 2]
    }

    dict_1 = {
        'animal': {1, 6, 7},  # use set {} to remove repeat elements and don't care about inser order
        'vegetable': {1, 2}
    }

    d = defaultdict(list)
    d['a'].append(1)
    d['a'].append(3)
    d['b'].append(2)
    d['a'].append(3)

    print(d)

    d = defaultdict(set)
    d['a'].add(1)
    d['a'].add(3)
    d['b'].add(2)
    d['a'].add(3)
    print(d)


if __name__ == '__main__':

    dict_key_to_values()
    # defaultdict(<class 'list'>, {'a': [1, 3, 3], 'b': [2]})
    # defaultdict(<class 'set'>, {'a': {1, 3}, 'b': {2}})
