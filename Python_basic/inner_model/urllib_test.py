#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import ssl
from urllib import request, parse
import urllib
import json

logging.getLogger().setLevel(logging.INFO)

ssl._create_default_https_context = ssl._create_unverified_context


def urllib_test(url):
    """
    Get
    :return:
    """
    with request.urlopen(url) as f:
        data = f.read()
        logging.info(f'Status: {f.status}, {f.reason}')

        for k, v in f.getheaders():
            logging.info(f'({k}:{v})')

        logging.info(f'Data: {data.decode("utf-8")}')


def get_test(url):
    req = request.Request(url)
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    urllib_test(url)


def post_test():
    """
    if use POST send a request, just need to input parameter 'data'
    as bytes style
    :return:
    """
    logging.info('Login to weibo.cn...')

    email = input('Email: ')
    pwd = input('Password: ')
    login_data = parse.urlencode([
        ('username', email),
        ('password', pwd),
        ('entry', 'mweibo'),
        ('client_id', ''),
        ('savestate', '1'),
        ('ec', ''),
        ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
    ])

    req = request.Request('https://passport.weibo.cn/sso/login')
    req.add_header('Origin', 'https://passport.weibo.cn')
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

    with request.urlopen(req, data=login_data.encode('utf-8')) as f:
        logging.info(f'Status: {f.status}, {f.reason}')
        for k, v in f.getheaders():
            logging.info(f'{k}:{v}')

        logging.info(f'Data: {f.read().decode("utf-8")}')


def proxy_handler_test():
    proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
    proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
    proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
    opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
    with opener.open('http://www.example.com/login.html') as f:
        pass


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Mobile Safari/537.36'
}


def fetch_data(url):

    req = request.Request(url, headers=HEADERS)
    with request.urlopen(req) as f:
        return json.loads(f.read().decode('utf-8'))


if __name__ == '__main__':

    # # urllib_test()
    # """
    # result:
    # INFO:root:Status: 200, OK
    # INFO:root:(Connection:close)
    # INFO:root:(Content-Length:49704)
    # INFO:root:(Server:nginx)
    # INFO:root:(Content-Type:text/html; charset=utf-8)
    # INFO:root:(X-Frame-Options:DENY)
    # INFO:root:(Via:1.1 vegur, 1.1 varnish, 1.1 varnish)
    # INFO:root:(Accept-Ranges:bytes)
    # INFO:root:(Date:Wed, 26 Jan 2022 06:36:57 GMT)
    # INFO:root:(Age:655)
    # INFO:root:(X-Served-By:cache-iad-kjyo7100127-IAD, cache-qpg1256-QPG)
    # INFO:root:(X-Cache:HIT, HIT)
    # INFO:root:(X-Cache-Hits:5, 9)
    # INFO:root:(X-Timer:S1643179017.043127,VS0,VE0)
    # INFO:root:(Vary:Cookie)
    # INFO:root:(Strict-Transport-Security:max-age=63072000; includeSubDomains)
    # INFO:root:Data: <!doctype html>
    # <!--[if lt IE 7]>   <html class="no-js ie6 lt-ie7 lt-ie8 lt-ie9">   <![endif]-->
    # <!--[if IE 7]>      <html class="no-js ie7 lt-ie8 lt-ie9">          <![endif]-->
    # <!--[if IE 8]>      <html class="no-js ie8 lt-ie9">                 <![endif]-->
    # <!--[if gt IE 8]><!--><html class="no-js" lang="en" dir="ltr">  <!--<![endif]-->
    #
    # <head>
    # ...
    # ...
    # ...
    # long text
    # """

    # url = 'https://www.python.org/'
    # get_test(url)

    # post_test()
    # """
    # INFO:root:Login to weibo.cn...
    # Email: xxx@xxx.com
    # Password: xxxxxxx
    # INFO:root:Status: 200, OK
    # INFO:root:Server:nginx/1.6.1
    # INFO:root:Date:Wed, 26 Jan 2022 12:42:56 GMT
    # INFO:root:Content-Type:text/html
    # INFO:root:Transfer-Encoding:chunked
    # INFO:root:Connection:close
    # INFO:root:Vary:Accept-Encoding
    # INFO:root:Cache-Control:no-cache, must-revalidate
    # INFO:root:Expires:Sat, 26 Jul 1997 05:00:00 GMT
    # INFO:root:Pragma:no-cache
    # INFO:root:Access-Control-Allow-Origin:https://passport.weibo.cn
    # INFO:root:Access-Control-Allow-Credentials:true
    # INFO:root:DPOOL_HEADER:tc-pub-10-85-144-115
    # INFO:root:Data: {"retcode":50011002,"msg":"\u7528\u6237\u540d\u6216\u5bc6\u7801\u9519\u8bef","data":{"username":"xxx@xxx.com","errline":15}}
    #
    # Process finished with exit code 0
    #
    # """
    # proxy_handler_test()

    url = 'https://www.liaoxuefeng.com/wiki/1016959663602400/1019223241745024'
    data = fetch_data(url)


