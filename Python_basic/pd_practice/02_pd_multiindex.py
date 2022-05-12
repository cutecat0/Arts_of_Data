import pandas as pd
import numpy as np


def pd_eg():
    cols = pd.MultiIndex.from_tuples(
        [(x, y) for x in ['A', 'B', 'C'] for y in ['0', '1']]
    )

    df = pd.DataFrame(np.random.randn(2, 6), index=['m', 'n'], columns=cols)
    print(df)


#      A                   B                   C
# 0         1         0         1         0         1
# m -1.718251 -0.911251 -0.312013 -0.894137 -2.356291  0.848239
# n  0.163396 -0.156341 -0.607056 -0.232332 -0.253261 -1.823689


if __name__ == '__main__':
    pd_eg()
