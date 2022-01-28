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
    req = requests.get('https://www.liaoxuefeng.com/wiki/1016959663602400/1183249464292448',
                       params={'q': 'python', 'cat': '1001'},
                       headers=HEADERS)
    logging.info(f'real url is : {req.url}')

    logging.info(f'requests encoding: {req.encoding}')

    content = req.content
    logging.info(f'request content is: {content}')


def test2():
    req = requests.post('https://www.liaoxuefeng.com/wiki/1016959663602400/1183249464292448',
                        data={'form_email': 'abc@example.com', 'form_password': '123456'})
    logging.info(f'real url is : {req.url}')

    logging.info(f'requests encoding: {req.encoding}')

    content = req.content
    logging.info(f'request content is: {content}')


def test3(url):
    """
    requests默认使用application/x-www-form-urlencoded对POST数据编码。
    如果要传递JSON数据，可以直接传入json参数：
    把post()方法替换为put()，delete()等，就可以以PUT或DELETE方式请求资源。
    :return:
    """
    params = {'key': 'value'}
    req = requests.post(url, json=params)

    logging.info(f'req {req}')

    upload_file = {'file': open('report.xls', 'rb')}  # 在读取文件时，注意务必使用'rb'即二进制模式读取，这样获取的bytes长度才是文件的长度。

    req = requests.post(url, files=upload_file)
    logging.info(f'req: {req}')
    logging.info(f'headers: {req.headers}\n headers content type: {req.headers["Content-Type"]}')

    # requests对Cookie做了特殊处理，使得我们不必解析Cookie就可以轻松获取指定的Cookie：
    logging.info(f'cookies: {req.cookies["ts"]}')

    # 要在请求中传入Cookie，只需准备一个dict传入cookies参数：
    cs = {
        'token': '12345',
        'status': 'working'
    }

    req = requests.get(url, cookies=cs)
    logging.info(f'req: {req}')

    # after 3 seconds 超时
    req = requests.get(url, timeout=3)

    logging.info(f'req: {req}')


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

    # test1()
    # INFO:root:real url is : https://www.douban.com/search?q=python&cat=1001
    # INFO:root:requests encoding: None

    # test2()

    test3(url)