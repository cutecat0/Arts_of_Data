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
    """
    s + s
    Out[2]:
    a   -1.569224
    b    0.829274
    c   -0.464486
    d   -3.408521
    e   -3.003048
    dtype: float64
    s * 2
    Out[3]:
    a   -1.569224
    b    0.829274
    c   -0.464486
    d   -3.408521
    e   -3.003048
    dtype: float64
    np.exp2(s)
    Out[4]:
    a    0.580508
    b    1.332963
    c    0.851310
    d    0.306878
    e    0.353180
    dtype: float64
    
    s[1:] + s[:-1]
    Out[5]: 
    a         NaN
    b    0.829274
    c   -0.464486
    d   -3.408521
    e         NaN
    dtype: float64
    """

    s2 = pd.Series(np.random.randn(5), name="magic")
    print(s2)
    """
    0    0.409252
    1    0.338865
    2    0.818272
    3   -0.247809
    4    0.589885
    Name: magic, dtype: float64
    """
    s3 = s2.rename("MagicData")
    print(s3, '\n', s3.name)
    """
    0   -2.005633
    1   -1.640921
    2   -0.041737
    3   -1.053985
    4    0.388305
    Name: MagicData, dtype: float64 
     MagicData
    """

    brk = 1


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


def dataframe_from_dicts_of_series():
    """
    A DataFrame is 2D(Dimensional) labeled Sstruct Data Type
    Index(row), 行
    Columns(columns) 列
    """
    pet = {
        "cat": pd.Series([1.0, 2.0, 3.0], index=["food", "weight", "cute"]),
        "duck": pd.Series([1.0, 2.0, 3.0, 4.0], index=["food", "weight", "cute", "water"])
    }

    df = pd.DataFrame(pet)

    print(df)
    """
            cat  duck
    cute    3.0   3.0
    food    1.0   1.0
    water   NaN   4.0
    weight  2.0   2.0
    """

    # df.columns
    # Out[3]: Index(['cat', 'duck'], dtype='object')
    # df.index
    # Out[4]: Index(['cute', 'food', 'water', 'weight'], dtype='object')


def df_from_dict_of_ndarry_or_list():
    """
    The ndarray must be the same length. If the index is passed, it must be cleary and also the same length as the array.
    """

    pets = {
        "cat": [1.0, 2.0, 3.0, 4.0],
        "duck": [4.0, 4.0, 2.0, 1.0]
    }

    df = pd.DataFrame(pets)

    print(df)
    """
       cat  duck
    0  1.0   4.0
    1  2.0   4.0
    2  3.0   2.0
    3  4.0   1.0
    """

    df = pd.DataFrame(pets, index=["weight", "food", "water", "name"])
    # index here is the name of rows.
    print(df)
    """
            cat  duck
    weight  1.0   4.0
    food    2.0   4.0
    water   3.0   2.0
    name    4.0   1.0
    """

    brk = 1


if __name__ == '__main__':
    # series_from_ndarray()
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
    # dataframe_from_dicts_of_series()
    df_from_dict_of_ndarry_or_list()
