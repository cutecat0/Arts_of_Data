import pandas as pd
import numpy as np


def df_use():
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

    df_1 = df.loc[(df.weight <= 6) & (df.lovely >= 100), 'weight']
    # print(df_1)
    #     0    4.2
    # Name: weight, dtype: float64

    df_2 = df.loc[(df.weight <= 6) | (df.lovely >= 100), 'weight']
    # print(df_2)
    # 0     4.2
    # 1     6.6
    # 2    12.5
    # 3     3.1
    # 4     3.8

    df.loc[(df.weight <= 6) & (df.lovely >= 100), 'weight'] = 6
    # print(df)
    #     name  weight  height  lovely  logic
    # 0     Cat     6.0      -1     100   thin
    # 1   Kitty     6.6     666     666  heavy
    # 2     Dog    12.5     666     666  heavy
    # 3    Duck     3.1      -1      88   thin
    # 4  Rabbit     3.8      -1      98   thin

    num = 20
    df_3 = df.loc[(df.lovely - num).abs().argsort()]
    # print(df_3)
    #     name  weight  height  lovely  logic
    # 3    Duck     3.1      -1      88   thin
    # 4  Rabbit     3.8      -1      98   thin
    # 0     Cat     6.0      -1     100   thin
    # 1   Kitty     6.6     666     666  heavy
    # 2     Dog    12.5     666     666  heavy

    sub_df1 = df.weight <= 6
    sub_df2 = df.height == -1
    sub_df3 = df.lovely < 100
    all_sub_df = sub_df1 & sub_df2 & sub_df3
    # print(df[all_sub_df])
    #     name  weight  height  lovely logic
    # 3    Duck     3.1      -1      88  thin
    # 4  Rabbit     3.8      -1      98  thin

    import functools
    sub_df_list = [sub_df1, sub_df2, sub_df3]
    all_sub_df_v2 = functools.reduce(lambda x, y: x & y, sub_df_list)
    # print(df[all_sub_df_v2])
    #     name  weight  height  lovely logic
    # 3    Duck     3.1      -1      88  thin
    # 4  Rabbit     3.8      -1      98  thin

    df_selected = df[(df.weight >= 6.0) & (df.index.isin([0, 2, 4]))]
    # print(df_selected)
    #     name  weight  height  lovely  logic
    # 0  Cat     6.0      -1     100   thin
    # 2  Dog    12.5     666     666  heavy

    # print(df)
    #     name  weight  height  lovely  logic
    # 0     Cat     6.0      -1     100   thin
    # 1   Kitty     6.6     666     666  heavy
    # 2     Dog    12.5     666     666  heavy
    # 3    Duck     3.1      -1      88   thin
    # 4  Rabbit     3.8      -1      98   thin
    new_df = pd.DataFrame(pets,
                          index=['aa', 'bb', 'cc', 'dd', 'ee'])
    # print(new_df)
    #     name  weight  height  lovely
    # aa     Cat     4.2       6     100
    # bb   Kitty     6.6       7     -20
    # cc     Dog    12.5      20      99
    # dd    Duck     3.1       3      88
    # ee  Rabbit     3.8       5      98
    ndf1 = new_df.loc["aa": "cc"]
    # print(ndf1)
    #     name  weight  height  lovely
    # aa    Cat     4.2       6     100
    # bb  Kitty     6.6       7     -20
    # cc    Dog    12.5      20      99

    ndf2 = new_df[0:3]
    # print(ndf2)
    #     name  weight  height  lovely
    # aa    Cat     4.2       6     100
    # bb  Kitty     6.6       7     -20
    # cc    Dog    12.5      20      99

    ndf3 = new_df["aa":"cc"]
    # print(ndf3)
    #     name  weight  height  lovely
    # aa    Cat     4.2       6     100
    # bb  Kitty     6.6       7     -20
    # cc    Dog    12.5      20      99

    new_df2 = pd.DataFrame(pets,
                           index=[1, 2, 3, 4, 5])  # here index from 1 not 0 start  label
    # print(new_df2)
    #     name  weight  height  lovely
    # 1     Cat     4.2       6     100
    # 2   Kitty     6.6       7     -20
    # 3     Dog    12.5      20      99
    # 4    Duck     3.1       3      88
    # 5  Rabbit     3.8       5      98

    ndf2_1 = new_df2.iloc[1:3]  # position-oriented
    print(ndf2_1)
    #     name  weight  height  lovely
    # 2  Kitty     6.6       7     -20
    # 3    Dog    12.5      20      99

    ndf2_2 = new_df2.loc[1:3]  # label-oriented
    print(ndf2_2)
    #     name  weight  height  lovely
    # 1    Cat     4.2       6     100
    # 2  Kitty     6.6       7     -20
    # 3    Dog    12.5      20      99


if __name__ == '__main__':
    df_use()
