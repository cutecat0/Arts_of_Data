#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from wsgiref.simple_server import make_server
from wsgi_test_client import application


logging.getLogger().setLevel(logging.INFO)


httpd = make_server('', 8000, application)
logging.info('Server HTTP on port 8000...')
httpd.serve_forever()

