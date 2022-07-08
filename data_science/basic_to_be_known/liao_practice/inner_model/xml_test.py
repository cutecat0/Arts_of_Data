#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from base64 import encode
from xml.parsers.expat import ParserCreate

logging.getLogger().setLevel(logging.INFO)


def xml_test():
    """
    There's two ways to operator XML: DOM & SAX
    DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。
    SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。
    正常情况下，优先考虑SAX，因为DOM实在太占内存。
    在Python中使用SAX解析XML非常简洁，
    通常我们关心的事件是start_element，end_element和char_data，
    准备好这3个函数，然后就可以解析xml了。
    :return:
    """
    pass


class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        logging.info(f'sax:start_element: {name}, attrs: {str(attrs)}')

    def end_element(self, name):
        logging.info(f'sax:end_element: {name}')

    def char_data(self, text):
        logging.info(f'sax:char_data:{text}')


def create_xml():
    L = []
    L.append(r'<?xml version="1.0"?>')
    L.append(r'<root>')
    L.append(encode('some & data_science'))
    L.append(r'</root>')

    return ''.join(L)


# todo
def test():
    pass


if __name__ == '__main__':
    xml = r'''<?xml version="1.0"?>
    <ol>
        <li><a href="/python">Python</a></li>
        <li><a href="/ruby">Ruby</a></li>
    </ol>
    '''
    handler = DefaultSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml)
    """
    INFO:root:sax:start_element: ol, attrs: {}
    INFO:root:sax:char_data:
    
    INFO:root:sax:char_data:        
    INFO:root:sax:start_element: li, attrs: {}
    INFO:root:sax:start_element: a, attrs: {'href': '/python'}
    INFO:root:sax:char_data:Python
    INFO:root:sax:end_element: a
    INFO:root:sax:end_element: li
    INFO:root:sax:char_data:
    
    INFO:root:sax:char_data:        
    INFO:root:sax:start_element: li, attrs: {}
    INFO:root:sax:start_element: a, attrs: {'href': '/ruby'}
    INFO:root:sax:char_data:Ruby
    INFO:root:sax:end_element: a
    INFO:root:sax:end_element: li
    INFO:root:sax:char_data:
    
    INFO:root:sax:char_data:    
    INFO:root:sax:end_element: ol

    """
