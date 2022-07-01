import pandas as pd
import numpy as np


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


if __name__ == '__main__':

    # series_from_ndarray()
    series_from_dict()