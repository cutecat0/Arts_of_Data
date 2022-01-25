#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import hashlib
import random

logging.getLogger().setLevel(logging.INFO)
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

db2 = {}


def hashlib_test():
    """
    Digest : MD5, SHA1
    摘要算法： also called 哈希算法、散列算法
    through a function change any length data into a length fixed data circle (数据串)
    digest function is a singel direction function
    it's easy to calculate f(data) while hard to through digest push out data
    MD5 is the most 'viewed' digest algorithm, high speed, result is fixed 128 bit,
    normally expressed by using one 32bits 16hex string
    the result of SHA1 is 160bit, usually  expressed by using one 40bits 16hex string
    SHA256 and SHA512 is much safer than SHA1, but the safer it is, the slower algorithm is.
    And length of digest would be much longer.
    crash: two different digest algorithms make two different sentences have the same digest.
    :return:
    """

    md5 = hashlib.md5()
    md5.update('I love my cat so much!'.encode('utf-8'))
    logging.info(f"md5 result is: {md5.hexdigest()}")

    md5.update('I like my cat so much!'.encode('utf-8'))
    logging.info(f"md5 result is: {md5.hexdigest()}")

    sha1 = hashlib.sha1()
    sha1.update('My cat is now using SHA1 in python'.encode('utf-8'))
    logging.info(f'Using SHA1: {sha1.hexdigest()}')
    sha1.update('Do u know my cat is so cute?'.encode('utf-8'))
    logging.info(f'Using SHA1: {sha1.hexdigest()}')


def calc_md5(pwd):
    """
    according to user's input
    calculate MD5 stored in db
    :param pwd:
    :return:
    """
    md5 = hashlib.md5()
    md5.update(str(pwd).encode('utf-8'))

    return md5.hexdigest()


def login(user, pwd):
    """
    check user login, through user input
    check whether input is right
    :param user:
    :param pwd:
    :return: True or False
    """
    pwd = calc_md5(pwd)

    if db[user] == pwd:
        return True
    else:
        return False


def calc_md5_v2(pwd):
    """
    normal pwd such as 123456 can has a compare table like {md5:123456}
    to make normal user much safer, add another complex string
    which is called "add salt"
    :param pwd:
    :return:
    """
    return get_md5(pwd + 'the-Salt')


def register(username, pwd):
    db2[username] = get_md5(pwd + username + 'the-Salt')


def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


class User(object):
    def __init__(self, username, pwd):
        self.username = username
        self.salt = ' '.join([chr(random.randint(48, 122)) for i in range(20)])
        self.pwd = get_md5(pwd + self.salt)


db2 = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}


def login2(username, pwd):
    user = db2[username]
    return user.pwd == get_md5(pwd + db2[username].salt)


if __name__ == '__main__':
    # hashlib_test()
    # INFO:root:md5 result is: 62b856beee489fecdecdce81fb2a83dc
    # INFO:root:md5 result is: d78d8850160880262c57492fd3d25d8a
    # INFO:root:Using SHA1: 576dc2b5a2fbef4aaf0dc59c808cad7c3cd5cfb0
    # INFO:root:Using SHA1: 0cf73a6877adbc628087f111afbae91148e4cdcd

    # assert login('michael', '123456')
    # assert login('bob', 'abc999')
    # assert login('alice', 'alice2008')
    # assert not login('michael', '1234567')
    # assert not login('bob', '123456')
    # assert not login('alice', 'Alice2008')
    # print('ok')

    assert login2('michael', '123456')
    assert login2('bob', 'abc999')
    assert login2('alice', 'alice2008')
    assert not login2('michael', '1234567')
    assert not login2('bob', '123456')
    assert not login2('alice', 'Alice2008')
    print('ok')
