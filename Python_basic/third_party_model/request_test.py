#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import requests

logging.getLogger().setLevel(logging.INFO)


def test(url):
    """
    third party library requests is more 'useful' than inner model urllib
    :param url:
    :return:
    """
    req = requests.get(url)
    logging.info(f'Status: {req.status_code}')
    logging.info(f'Text : {req.text}')

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Mobile Safari/537.36'
}


def test1():
    req = requests.get('https://www.liaoxuefeng.com/wiki/1016959663602400/1183249464292448', params={'q': 'python', 'cat': '1001'})
    logging.info(f'real url is : {req.url}')

    logging.info(f'requests encoding: {req.encoding}')

    content = req.content
    logging.info(f'request content is: {content}')


if __name__ == '__main__':
    url = 'https://www.liaoxuefeng.com/wiki/1016959663602400/1183249464292448'
    url = 'https://github.com/cutecat0'
    # test(url)
    """
    INFO:root:Status: 200
    INFO:root:Text : 
    
    <!DOCTYPE html>
    ...
    ...
    """

    test1()
    # INFO:root:real url is : https://www.douban.com/search?q=python&cat=1001
    # INFO:root:requests encoding: None

