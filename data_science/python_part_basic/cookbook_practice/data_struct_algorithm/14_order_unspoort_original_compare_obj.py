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


class UserWithName(User):

    def __init__(self, first_name, last_name, user_id):
        super().__init__(user_id)
        self.first_name_ = first_name
        self.last_name_ = last_name

    def __repr__(self):
        return 'UserWithName({}, {}, {})'.format(self.user_id_, self.first_name_, self.last_name_)


def sort_not_compare():

    users = [User(99), User(12), User(100), User(3)]
    print(users)
    # [User(99), User(12), User(100), User(3)]

    print(sorted(users, key=lambda u: u.user_id_))
    # [User(3), User(12), User(99), User(100)]

    # way 2
    print(sorted(users, key=attrgetter('user_id_')))
    # [User(3), User(12), User(99), User(100)]

    # way 2 can run more quickly than way 1 & can pass more than one key
    # if user has last name and first name

    users = [UserWithName('Simba', 'Celina', 3),
             UserWithName('Cute', 'Cat', 93),
             UserWithName('Bruce', 'Win', 23),
             UserWithName('Jim', 'Gorden', 33)]
    print(users)
    # [UserWithName(3, Simba, Celina), UserWithName(93, Cute, Cat), UserWithName(23, Bruce, Win), UserWithName(33, Jim, Gorden)]
    print(sorted(users, key=attrgetter('first_name_')))
    # [UserWithName(23, Bruce, Win), UserWithName(93, Cute, Cat), UserWithName(33, Jim, Gorden), UserWithName(3, Simba, Celina)]
    print(sorted(users, key=attrgetter('last_name_')))
    # [UserWithName(93, Cute, Cat), UserWithName(3, Simba, Celina), UserWithName(33, Jim, Gorden), UserWithName(23, Bruce, Win)]


if __name__ == '__main__':
    sort_not_compare()