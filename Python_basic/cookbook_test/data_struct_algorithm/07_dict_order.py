from collections import OrderedDict
import json

"""
    Q: How to keep the order of the elements of a dict when you create it?
    A: Use collections.OrderedDict class can make sure the insert order of the dict.
"""


def ordered_dict():
    """
    !!! OrderedDict inner build a ordered by key double-link-table(双向链表)
    each time insert in the tail of this link-table
    So, the size of OrderedDict is two times of the normal dict.
    """

    d = OrderedDict()
    d['cat'] = 8
    d['dog'] = 2
    d['duck'] = 3
    d['dragon'] = 4
    d['cat'] = 1

    for key in d:
        print(key, d[key])

    json_dict = json.dumps(d)
    print(json_dict)
    # {"cat": 1, "dog": 2, "duck": 3, "dragon": 4}


if __name__ == '__main__':

    ordered_dict()
    """
    cat 1
    dog 2
    duck 3
    dragon 4
    {"cat": 1, "dog": 2, "duck": 3, "dragon": 4}
    
    Process finished with exit code 0

    """
