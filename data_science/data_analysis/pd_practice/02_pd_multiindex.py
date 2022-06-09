import pandas as pd
import numpy as np


def pd_arithmetic():
    cols = pd.MultiIndex.from_tuples(
        [(x, y) for x in ['A', 'B', 'C'] for y in ['o', 'I']]
    )

    df = pd.DataFrame(np.random.randn(2, 6), index=['m', 'n'], columns=cols)
    print(df)
    #     A                   B                   C
    #     o         I         o         I         o         I
    # m -1.647612 -0.124666 -1.100841 -0.007436  0.796428  0.132117
    # n -0.645900 -0.182829  0.485222  1.143299 -0.200310  1.492418

    df = df.div(df["C"], level=1)
    print(df)
    #     A                    B              C
    # o         I          o         I    o    I
    # m  0.843623 -2.473784  -0.039459 -2.159385  1.0  1.0
    # n -3.912239  0.317357  12.643313  0.004393  1.0  1.0


def pd_slice():

    tup = [
        ('AA', 'one'),
        ('AA', 'two'),
        ('BB', 'one'),
        ('BB', 'two'),
        ('BB', 'three')
    ]

    index = pd.MultiIndex.from_tuples(tup)

    df = pd.DataFrame([11, 22, 33, 44, 55], index, ['mData'])
    print(df)
    """
              mData
    AA one       11
       two       22
    BB one       33
       two       44
       three     55

    """

    # level and axis are optional, and default to zero
    # tdf = df.xs("BB", level=1, axis=0)  # It can't work here
    # print(tdf)

    tdf = df.xs('three', level=1, axis=0)
    print(tdf)
    #     mData
    # BB     55


if __name__ == '__main__':

    # pd_arithmetic()
    pd_slice()