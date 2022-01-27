#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import random
from PIL import Image, ImageFilter, ImageDraw, ImageFont

logging.getLogger().setLevel(logging.INFO)


def test():
    """
    PIL: Python Imaging Library just support to python 2.7
    On the base of PIL, create new Pillow to support Python 3.x
    :return:
    """
    # pip3 install pillow

    img = Image.open('hogwarts-legacy-desktop.jpg')

    width, height = img.size
    logging.info(f'Image size is: {width}\t{height}')

    img.thumbnail((width//2, height//2))
    logging.info(f'Resize image to {width//2}\t{height//2}')

    # img.save('thumbnail.jpg', 'jpeg')

    img2 = img.filter(ImageFilter.BLUR)
    img2.save('blue.jpg', 'jpeg')


def rndChar():
    return chr(random.randint(65, 90))


def rndColor():
    return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)


def rndColor2():
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)


def draw_test():
    width, height = 60 * 4, 60
    image = Image.new('RGB', (width, height), (255, 255, 255))
    font = ImageFont.truetype('Arial.ttf', 36)
    draw = ImageDraw.Draw(image)

    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())

    for t in range(6):
        draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())

    image = image.filter(ImageFilter.BLUR)
    image.save('code.jpg', 'jpeg')


if __name__ == '__main__':

    # test()
    draw_test()
