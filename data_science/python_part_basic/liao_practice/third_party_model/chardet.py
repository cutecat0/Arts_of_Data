#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import chardet

logging.getLogger().setLevel(logging.INFO)


def test():
    """
    use chardet to config codec
    :return:
    """
    chardet.detect(b"Hey, lovely cat!")

    data = '晴空一鹤排云上，便引诗情到碧霄'.encode('gbk')
    chardet.detect(data)
    result: {'encoding': 'GB2312', 'confidence': 0.617283950617284, 'language': 'Chinese'}

    data = '晴空一鹤排云上，便引诗情到碧霄'.encode('utf-8')
    chardet.detect(data)
    result: {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}

    data = '最新の主要ニュース'.encode('euc-jp')
    chardet.detect(data)
    result: {'encoding': 'EUC-JP', 'confidence': 0.99, 'language': 'Japanese'}


if __name__ == '__main__':

    test()
    # Out[4]: {'encoding': 'ascii', 'confidence': 1.0, 'language': ''}
