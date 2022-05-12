import pandas as pd
import numpy as np


def pd_eg():
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



if __name__ == '__main__':
    pd_eg()
