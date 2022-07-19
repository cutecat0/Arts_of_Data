"""
    Reference: https://pandas.pydata.org/docs/user_guide/basics.html
"""
import pandas as pd
import numpy as np


def basic():
    index = pd.date_range('15/7/2022', periods=8)
    s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
    df = pd.DataFrame(np.random.randn(8, 3), index=index, columns=['A', 'B', 'C'])

    print(s)
    """
    a   -0.434197
    b    0.395526
    c   -0.918827
    d   -0.215662
    e   -0.055373
    dtype: float64
    """
    print(df.head())
    """
                       A         B         C
    2022-07-15  1.150356 -0.201596 -1.158423
    2022-07-16 -0.618148 -1.100873  0.650654
    2022-07-17  0.086898 -0.716115  0.203106
    2022-07-18  0.351271  0.975082  1.305610
    2022-07-19  1.503442  0.723368  0.946969
    """
    print(df.tail())
    """
                       A         B         C
    2022-07-18  0.351271  0.975082  1.305610
    2022-07-19  1.503442  0.723368  0.946969
    2022-07-20 -0.837931  1.293797 -1.711009
    2022-07-21 -0.309344 -1.154464  0.971995
    2022-07-22 -0.362262 -0.967317 -1.336987
    """


if __name__ == '__main__':
    basic()