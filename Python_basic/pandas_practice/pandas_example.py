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

    mask = pd.DataFrame(
        {'name': [True] * 4,
         'weight': [False] * 4,
         'height': [True, False] * 2,
         'lovely': [True, False] * 2
         }
    )
    mask_df = df.where(mask, -9999)
    # print(mask_df)
    #     name  weight  height  lovely
    # 0    Cat -9999.0      -1     100
    # 1  Kitty -9999.0   -9999   -9999
    # 2    Dog -9999.0     666     666
    # 3   Duck -9999.0   -9999   -9999
    # 4  -9999 -9999.0   -9999   -9999

    df["logic"] = np.where(df['weight'] > 6, 'heavy', 'thin')
    # print(df)
    #     name  weight  height  lovely  logic
    # 0     Cat     4.2      -1     100   thin
    # 1   Kitty     6.6     666     666  heavy
    # 2     Dog    12.5     666     666  heavy
    # 3    Duck     3.1      -1      88   thin
    # 4  Rabbit     3.8      -1      98   thin

    # print(df[df.lovely > 100])
    #     name  weight  height  lovely  logic
    # 1  Kitty     6.6     666     666  heavy
    # 2    Dog    12.5     666     666  heavy
    # print(df[df.weight < 4])
    #     name  weight  height  lovely logic
    # 3    Duck     3.1      -1      88  thin
    # 4  Rabbit     3.8      -1      98  thin


if __name__ == '__main__':

    pandas_practice()
