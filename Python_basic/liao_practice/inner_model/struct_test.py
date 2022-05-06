#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import struct
import base64

logging.getLogger().setLevel(logging.INFO)

bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAA' +
                            'AAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3/' +
                            '/f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/A' +
                            'HwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9' +
                            '//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f' +
                            '/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHw' +
                            'AfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//' +
                            '38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9' +
                            '//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAf' +
                            'AB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHw' +
                            'AfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//' +
                            '3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')


def struct_test():
    """
    struct model solve bytes and other 01 data_science type change
    :return:
    """
    bytes_data = struct.pack('>I', 10240099)
    logging.info(f'pack change any type data_science into bytes: {bytes_data}')

    bytes2data = struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
    logging.info(f'unpack change bytes to itself data_science type: {bytes2data}')

    s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
    bmp = struct.unpack('<ccIIIIIIHH', s)
    logging.info(f'windows BMP result: {bmp}')


def bmp_info(data):
    """
    check whether any file is BMP file,
    if it is, then print picture size and color number.
    :param data:
    :return:
    """
    data = data[:30]
    s = struct.unpack('<ccIIIIIIHH', data)
    logging.info(f's is: {s}')
    # INFO:root:s is: (b'B', b'M', 616, 0, 54, 40, 28, 10, 1, 16)
    b, m = s[0], s[1]
    if b == b'B' and m == b'M':
        logging.info(f'data_science is BMP file {s}')
        width, height, color = s[-4], s[-3], s[-1]
        return {
            'width': width,
            'height': height,
            'color': color
        }


if __name__ == '__main__':

    # struct_test()
    # INFO:root:pack change any type data_science into bytes: b'\x00\x9c@c'
    # INFO:root:unpack change bytes to itself data_science type: (4042322160, 32896)
    # INFO:root:windows BMP result: (b'B', b'M', 691256, 0, 54, 40, 640, 360, 1, 24)

    bi = bmp_info(bmp_data)
    assert bi['width'] == 28
    assert bi['height'] == 10
    assert bi['color'] == 16
    print('ok')



