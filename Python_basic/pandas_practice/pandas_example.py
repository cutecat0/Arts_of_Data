import pandas as pd
import numpy as np


def pandas_practice():
    pets = {
        'name': ['Cat', 'Kitty', 'Dog', 'Duck', 'Rabbit'],
        'weight': [4.2, 6.6, 12.5, 3.1, 3.8],
        'height': [6, 7, 20, 3, 5],
        'lovely': [100, -20, 99, 88, 98]
    }

    df = pd.DataFrame(pets)
    # print(df)
    #     name  weight  height  lovely
    # 0     Cat     4.2       6     100
    # 1   Kitty     6.6       7     -20
    # 2     Dog    12.5      20      99
    # 3    Duck     3.1       3      88
    # 4  Rabbit     3.8       5      98

    df.loc[df.weight <= 6, 'height'] = -1
    # print(df)
    #     name  weight  height  lovely
    # 0     Cat     4.2      -1     100
    # 1   Kitty     6.6       7     -20
    # 2     Dog    12.5      20      99
    # 3    Duck     3.1      -1      88
    # 4  Rabbit     3.8      -1      98

    df.loc[df.weight > 6, ['height', 'lovely']] = 666
    # print(df)
    #     name  weight  height  lovely
    # 0     Cat     4.2      -1     100
    # 1   Kitty     6.6     666     666
    # 2     Dog    12.5     666     666
    # 3    Duck     3.1      -1      88
    # 4  Rabbit     3.8      -1      98


if __name__ == '__main__':

    pandas_practice()
