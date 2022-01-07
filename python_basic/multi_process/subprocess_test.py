#!/usr/bin/env python3
# -*- coding : utf-8 -*-

import subprocess
import logging

logging.getLogger().setLevel(logging.INFO)


def test_subprocess():
    """
        Many times subprocess is not itself, it's an outer process,
    after we create subprocess, we need to control the input and output of subprocess we have created
    subprocess model can let us start a subprocess very conveniently, then control its input and output
    :return:
    """

    logging.info('$ nslookup www.python.org')

    r = subprocess.call(['nslookup', 'www.python.org'])

    logging.info('Exit code: %s ' % r)


def subprocess_continue_input():

    """
        if subprocess still needs to input, can through communicate() way to input
    :return:
    """

    logging.info('$ nslookup')

    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b'set q=mx\npython.org\nexit\n')

    logging.info(output.decode('utf-8'))
    logging.info('Exit code:  %s ' % p.returncode)


if __name__ == '__main__':

    # test_subprocess()

    # the result is:
    """
        /usr/local/bin/python3.7 /Users/gwendolynhai/AI/Gwendolyn_s_Art/multi_process/subprocess_test.py
        INFO:root:$ nslookup www.python.org
        Server:		10.1.30.51
        Address:	10.1.30.51#53
        
        Non-authoritative answer:
        www.python.org	canonical name = dualstack.python.map.fastly.net.
        Name:	dualstack.python.map.fastly.net
        Address: 199.232.44.223
        
        INFO:root:Exit code: 0 
        
        Process finished with exit code 0

    """

    subprocess_continue_input()
