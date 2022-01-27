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


if __name__ == '__main__':
    url = 'https://www.liaoxuefeng.com/wiki/1016959663602400/1183249464292448'
    url = 'https://github.com/cutecat0'
    test(url)
    """
    INFO:root:Status: 200
    INFO:root:Text : 
    
    <!DOCTYPE html>
    ...
    ...
    """
