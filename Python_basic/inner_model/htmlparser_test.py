#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from html.parser import HTMLParser
from html.entities import name2codepoint

logging.getLogger().setLevel(logging.INFO)


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        logging.info(f'<{tag}>')

    def handle_endtag(self, tag):
        logging.info(f'<{tag}>')

    def handle_startendtag(self, tag, attrs):
        logging.info(f'<{tag}>')

    def handle_data(self, data):
        logging.info(f'{data}')

    def handle_comment(self, data):
        logging.info(f'<!--{data}-->')

    def handle_entityref(self, name):
        logging.info(f'&{name}')

    def handle_charref(self, name):
        logging.info(f'&#{name}')


if __name__ == '__main__':

    parser = MyHTMLParser()
    parser.feed(
        '''<html>
            <head></head>
            <body>
            <!-- test html parser -->
                <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
            </body></html>'''
    )

    """
    INFO:root:<html>
    INFO:root:
                
    INFO:root:<head>
    INFO:root:<head>
    INFO:root:
                
    INFO:root:<body>
    INFO:root:
                
    INFO:root:<!-- test html parser -->
    INFO:root:
                    
    INFO:root:<p>
    INFO:root:Some 
    INFO:root:<a>
    INFO:root:html
    INFO:root:<a>
    INFO:root: HTML tutorial...
    INFO:root:<br>
    INFO:root:END
    INFO:root:<p>
    INFO:root:
                
    INFO:root:<body>
    INFO:root:<html>
    
    Process finished with exit code 0
    """



