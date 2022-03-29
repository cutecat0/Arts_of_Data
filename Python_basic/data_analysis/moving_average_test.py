#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import logging
import pandas as pd
import random


logging.getLogger().setLevel(logging.INFO)


class MovingAverage(object):
    """
    ma means moving average
    http://wiki.qiyi.domain/pages/viewpage.action?pageId=1297823056
    There is no correct time frame to use when setting up your moving averages.
    The best way to figure out which one works best for you is to experiment
    with a number of different time periods until you find one that fits your strategy.
    :return:
    """
    def __init__(self):
        self._moving_window_size = 3
        self._data = [i for i in range(10)]

    def calculate_ma(self):
        ma_data, i = [], 0
        while i < len(self._data) - self._moving_window_size + 1:
            window = self._data[i: i + self._moving_window_size + 1]
            window_average = round(sum(window) / self._moving_window_size, 2)
            ma_data.append(window_average)
            i += 1

        logging.info(f'moving average is : \n {ma_data}')


if __name__ == '__main__':

    ma = MovingAverage()
    ma.calculate_ma()
    # y_predict = i_df[-NUM:].rolling(window=MOVING_WINDOW_SIZE).mean()
