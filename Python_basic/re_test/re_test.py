#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import re

logging.getLogger().setLevel(logging.INFO)


def re_test(s):
    if re.match(r'^[a~zA~Z*]', s):
        logging.info('right')
    else:
        logging.info('failed')


if __name__ == '__main__':
    s = 'I am a cute cat'
    re_test(s)

    # reference : https://www.liaoxuefeng.com/wiki/1016959663602400/1017639890281664
