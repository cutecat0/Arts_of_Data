#! usr/bin/env python
# -*- coding:utf-8 -*-

from operator import attrgetter

"""
    Q: You want to order same type object while they don't support original compare
    A: Way 1: use sorted() function with it's parameter 'key'
       Way 2: use operator.attrgetter() instead of lambda 
"""


class User:

    def __init__(self, user_id):
        self.user_id_ = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id_)


def sort_not_compare():

    users = [User(99), User(12), User(100), User(3)]
    print(users)
    # [User(99), User(12), User(100), User(3)]

    print(sorted(users, key=lambda u: u.user_id_))
    # [User(3), User(12), User(99), User(100)]

    # way 2
    print(sorted(users, key=attrgetter('user_id_')))
    # [User(3), User(12), User(99), User(100)]


if __name__ == '__main__':
    sort_not_compare()