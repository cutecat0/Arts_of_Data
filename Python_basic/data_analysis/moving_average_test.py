#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import logging
import numpy as np
import pandas as pd


logging.getLogger().setLevel(logging.INFO)


class MovingAverage(object):
    """
    ma means moving average
    above all references from http://wiki.qiyi.domain/pages/viewpage.action?pageId=1297823056
    There is no correct time frame to use when setting up your moving averages.
    The best way to figure out which one works best for you is to experiment
    with a number of different time periods until you find one that fits your strategy.
    :return:
    """
    def __init__(self):
        self._moving_window_size = 3
        self._data = [i for i in range(10)]
        self._data = [1, 3, 6, 0, 10, 20, 2, 1]

    def calculate_ma(self):
        ma_data, i = [], 0
        while i < len(self._data) - self._moving_window_size + 1:
            window = self._data[i: i + self._moving_window_size]
            moving_average = round(sum(window) / self._moving_window_size, 2)
            ma_data.append(moving_average)
            i += 1

        logging.info(f'using normal way ma is : \n {ma_data}')

    def numpy_ma(self):
        """
        Method 1: Using Numpy
        Numpy module of Python provides an easy way to calculate the simple moving average of the array of observations.
        It provides a method called numpy.sum() which returns the sum of elements of the given array.
        A moving average can be calculated by finding the sum of elements present in the window and dividing it with window size.
        :return:
        """
        ma_data, i = [], 0
        while i < len(self._data) - self._moving_window_size + 1:
            moving_average = round(np.sum(self._data[i:i+self._moving_window_size]) / self._moving_window_size, 2)
            ma_data.append(moving_average)
            i += 1

        logging.info(f'using numpy ma is: \n {ma_data}')

    def pandas_ma(self):
        """
        Method 2: Using Pandas
        Pandas module of Python provides an easy way to calculate the simple moving average of the series of observations.
        It provides a method called pandas.Series.rolling(window_size) which returns a rolling window of specified size.
        The mean of the window can be calculated by using pandas.Series.mean() function on the object of window obtained above.
        pandas.Series.rolling(window_size) will return some null series since it need at least k (size of window) elements to be rolling.
        :return:
        """
        data_series = pd.Series(self._data)
        ma_data = data_series.rolling(self._moving_window_size)
        moving_average = round(ma_data.mean(), 2)

        final_ma_data = moving_average.to_list()[self._moving_window_size - 1:]

        logging.info(f'using pandas ma is : \n {final_ma_data}')


if __name__ == '__main__':

    ma = MovingAverage()
    ma.calculate_ma()
    ma.numpy_ma()
    ma.pandas_ma()

    """ 
    INFO:root:using normal way ma is : 
     [3.33, 3.0, 5.33, 10.0, 10.67, 7.67]
    INFO:root:using numpy ma is: 
     [3.33, 3.0, 5.33, 10.0, 10.67, 7.67]
    INFO:root:using pandas ma is : 
     [3.33, 3.0, 5.33, 10.0, 10.67, 7.67]
    
    Process finished with exit code 0

    """
