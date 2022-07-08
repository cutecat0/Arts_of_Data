#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import logging
import hmac
import random

logging.getLogger().setLevel(logging.INFO)


def hmac_test():
    """
    Hmac algorithm: Keyed-Hashing for Message Authentication
    It offers a standard algorithm while calculate hash,
    mix key in the processing of calculating.
    :return:
    """
    message = b'Hey, lovely & cute cat!'
    key = b'simba'
    h = hmac.new(key, message, digestmod='MD5')
    # if message is too much long, can use h.update(msg) by more than one time
    logging.info(f'Hmac res: {h.hexdigest()}')


def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()


class User(object):

    def __init__(self, username, pwd):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.pwd = hmac_md5(self.key, pwd)


db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}


def login(username, pwd):
    user = db[username]

    return user.pwd == hmac_md5(user.key, pwd)


if __name__ == '__main__':

    # hmac_test()
    # INFO:root:Hmac res: eb62495424e180ccbcb816db29a98bd8

    assert login('michael', '123456')
    assert login('bob', 'abc999')
    assert login('alice', 'alice2008')
    assert not login('michael', '1234567')
    assert not login('bob', '123456')
    assert not login('alice', 'Alice2008')
    print('ok')

