#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

logging.getLogger().setLevel(logging.INFO)


def application(envr, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hey, %s!</h1>' % (envr['PATH_INFO'][1:] or 'web')

    return [body.encode('utf-8')]


