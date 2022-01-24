#!/usr/bin/env python3

import logging
import base64

logging.getLogger().setLevel(logging.INFO)


def base64_test():
    """
    Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。

    由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，
    所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：

    由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉：
    去掉=后怎么解码呢？因为Base64是把3个字节变为4个字节，
    所以，Base64编码的长度永远是4的倍数，因此，需要加上=把Base64字符串的长度变为4的倍数，就可以正常解码了。

    :return:
    """

    res = base64.b64encode(b'binary\x00string')

    logging.info(f'result is: {res}')
    # INFO:root:result is: b'YmluYXJ5AHN0cmluZw=='

    check = base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
    logging.info(f'check is: {check}')
    # INFO:root:check is: b'binary\x00string'

    url_ = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
    logging.info(f'url _ {url_}')
    # INFO:root:url _ b'abcd++//'

    url_safe = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
    logging.info(f'url safe {url_safe}')
    # INFO:root:url safe b'abcd--__'

    url_safe_ = base64.urlsafe_b64decode('abcd--__')
    logging.info(f'url safe _ {url_safe}')
    # INFO:root:url safe _ b'abcd--__'


def safe_base64_decode(s):
    """
    decode remove =
    :param s:
    :return:
    """
    return base64.b64decode(s + '=' * (len(s) % 4) if len(s) % 4 else s )


if __name__ == '__main__':

    # base64_test()

    assert b'abcd' == safe_base64_decode('YWJjZA=='), safe_base64_decode('YWJjZA==')
    assert b'abcd' == safe_base64_decode('YWJjZA'), safe_base64_decode('YWJjZA')
    print('ok')