from operator import itemgetter

"""
    Q: How to order a dict by a key word given?
    A: Use itemgetter() function from operator model
"""


def order_dict_by_key_word():

    users = [
        {'name': 'Jerry', 'addr': 'Moon', 'uid': 10010},
        {'name': 'Tom', 'addr': 'Earth', 'uid': 10012},
        {'name': 'Simba', 'addr': 'Mars', 'uid': 10039},
        {'name': 'Anna', 'addr': 'Moon', 'uid': 10004},
        {'name': 'Lee', 'addr': 'Earth', 'uid': 10050},
    ]

    users_by_name = sorted(users, key=itemgetter('name'))
    # print(users_by_name)
    # [{'name': 'Anna', 'addr': 'Moon', 'uid': 10004},
    #  {'name': 'Jerry', 'addr': 'Moon', 'uid': 10010},
    #  {'name': 'Lee', 'addr': 'Earth', 'uid': 10050},
    #  {'name': 'Simba', 'addr': 'Mars', 'uid': 10039},
    #  {'name': 'Tom', 'addr': 'Earth', 'uid': 10012}]

    users_by_uid = sorted(users, key=itemgetter('uid'))
    # print(users_by_uid)
    # [{'name': 'Anna', 'addr': 'Moon', 'uid': 10004},
    #  {'name': 'Jerry', 'addr': 'Moon', 'uid': 10010},
    #  {'name': 'Tom', 'addr': 'Earth', 'uid': 10012},
    #  {'name': 'Simba', 'addr': 'Mars', 'uid': 10039},
    #  {'name': 'Lee', 'addr': 'Earth', 'uid': 10050}]

    users_by_name_addr = sorted(users, key=itemgetter('name', 'addr'))
    # print(users_by_name_addr)
    # [{'name': 'Anna', 'addr': 'Moon', 'uid': 10004},
    #  {'name': 'Jerry', 'addr': 'Moon', 'uid': 10010},
    #  {'name': 'Lee', 'addr': 'Earth', 'uid': 10050},
    #  {'name': 'Simba', 'addr': 'Mars', 'uid': 10039},
    #  {'name': 'Tom', 'addr': 'Earth', 'uid': 10012}]

    # itemgetter can also use lambda, but it slowly, itemgetter is much quick
    users_by_name_uid = sorted(users, key=lambda u: (u['name'], u['uid']))
    print(users_by_name_uid)
    # [{'name': 'Anna', 'addr': 'Moon', 'uid': 10004},
    #  {'name': 'Jerry', 'addr': 'Moon', 'uid': 10010},
    #  {'name': 'Lee', 'addr': 'Earth', 'uid': 10050},
    #  {'name': 'Simba', 'addr': 'Mars', 'uid': 10039},
    #  {'name': 'Tom', 'addr': 'Earth', 'uid': 10012}]

    max_users_by_uid = max(users, key=itemgetter('uid'))
    print(max_users_by_uid)
    # {'name': 'Lee', 'addr': 'Earth', 'uid': 10050}


if __name__ == '__main__':

    order_dict_by_key_word()