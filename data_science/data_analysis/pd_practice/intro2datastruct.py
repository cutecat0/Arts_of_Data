import pandas as pd
import numpy as np

"""
    Reference: https://pandas.pydata.org/docs/user_guide/dsintro.html
"""


def series_from_ndarray():
    """
    A  Series is one-dimensional labeled array.
    s = pd.Series(data, index=index)
    """
    # 1. From ndarray
    # If data is ndarray, index must be the same length as data.
    s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
    print(s)
    """
    a   -0.261770
    b   -0.164276
    c    0.590781
    d   -1.468494
    e   -0.107874
    dtype: float64
    """
    print(s.index)
    " Index(['a', 'b', 'c', 'd', 'e'], dtype='object') "

    # when data is ndarray-like, and U want it to be real ndarray, use the follow
    s.to_numpy()
    # Out[13]: array([-0.39385148, -0.93355423,  1.1051972 ,  0.71894043, -0.21014577])

    # a series which is like a fixed_size dict, U can get and set values by index label
    print(s["a"], s["e"])
    # -0.006321635835820239 0.8299959086276444
    s["e"] = 0.66666
    print(s["e"])
    # 0.66666

    # Using the get(), the missing label will turn None or, set a special default
    s.get("f")
    s.get("e")
    # Out[3]: 1.169925222834734
    s.get("f", np.nan)
    # Out[4]: nan


def series_from_dict():
    """
    When the data is a dict and index isn't passed, the index of Series will be ordered by the dict's insertion order.
    """
    dic = {"cat": 100, "Duck": 98, "Rabbit": 88}
    s = pd.Series(dic)

    print(s)
    """
    cat       100
    Duck       98
    Rabbit     88
    dtype: int64
    """
    """ If an index is passed, the values in the dict will be instead of by passed index """
    s2 = pd.Series(dic, index=["cat", "Duck", "r", "o"])
    print(s2)
    """
    cat     100.0
    Duck     98.0
    r         NaN
    o         NaN
    dtype: float64
    """
    # NaN(Not a Number) is the standard missing data marker used in pandas


def series_from_scalar_value():
    """
    If the data is a scalar value, the index must be provided, the value will be repeated to match the length of index
    """
    s = pd.Series(6.6, index=["a", "b", "c", "d", "e", "f"])
    print(s)
    """
    a    6.6
    b    6.6
    c    6.6
    d    6.6
    e    6.6
    f    6.6
    dtype: float64
    """


if __name__ == '__main__':
    series_from_ndarray()
    """
    s[0]
    Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
    Type 'copyright', 'credits' or 'license' for more information
    IPython 7.20.0 -- An enhanced Interactive Python. Type '?' for help.
    PyDev console: using IPython 7.20.0
    Out[1]: -0.3938514756551117
    s[:3]
    Out[2]: 
    a   -0.393851
    b   -0.933554
    c    1.105197
    dtype: float64
    s[s > s.median()]
    Out[3]: 
    c    1.105197
    d    0.718940
    dtype: float64
    s
    Out[4]: 
    a   -0.393851
    b   -0.933554
    c    1.105197
    d    0.718940
    e   -0.210146
    dtype: float64
        s[[4, 3, 1]]
    Out[6]: 
    e   -0.210146
    d    0.718940
    b   -0.933554
    dtype: float64
    np.exp(s)
    Out[7]: 
    a    0.674454
    b    0.393154
    c    3.019820
    d    2.052258
    e    0.810466
    dtype: float64
    s
    Out[8]: 
    a   -0.393851
    b   -0.933554
    c    1.105197
    d    0.718940
    e   -0.210146
    dtype: float64
    s.dtype
    Out[9]: dtype('float64')
    s.array
    Out[10]: 
    <PandasArray>
    [ -0.3938514756551117,  -0.9335542253402275,   1.1051972009660536,
       0.7189404297237888, -0.21014576709650493]
    Length: 5, dtype: float64
    s
    Out[11]: 
    a   -0.393851
    b   -0.933554
    c    1.105197
    d    0.718940
    e   -0.210146
    dtype: float64

    """
    # series_from_dict()
    # series_from_scalar_value()
