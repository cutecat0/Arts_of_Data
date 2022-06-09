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
    # print(ndf2_1)
    #     name  weight  height  lovely
    # 2  Kitty     6.6       7     -20
    # 3    Dog    12.5      20      99

    ndf2_2 = new_df2.loc[1:3]  # label-oriented
    # print(ndf2_2)
    #     name  weight  height  lovely
    # 1    Cat     4.2       6     100
    # 2  Kitty     6.6       7     -20
    # 3    Dog    12.5      20      99

    # print(df)
    other_df = df[~((df.weight < 6) & (df.lovely < 100))]
    # print(other_df)
    #     name  weight  height  lovely  logic
    # 0    Cat     6.0      -1     100   thin
    # 1  Kitty     6.6     666     666  heavy
    # 2    Dog    12.5     666     666  heavy


def df_use_2():
    items = {
        'AA': [1, 2, 1, 1],
        'BB': [1, 2, 1, 2],
        'CC': [1, 2, 3, 3],
        'DD': [1, 2, 3, 4]
    }

    df = pd.DataFrame(items)
    # print(df)
    #     AA  BB  CC  DD
    # 0   1   1   1   1
    # 1   2   2   2   2
    # 2   1   1   3   3
    # 3   1   2   3   4

    source_cols = df.columns
    new_cols = [str(x) + '_cat' for x in source_cols]
    categories = {1: 'Cat', 2: 'Dog', 3: 'Duck', 4: 'Rubbit'}
    df[new_cols] = df.applymap(categories.get)
    # print(df)
    #     AA  BB  CC  DD AA_cat BB_cat CC_cat  DD_cat
    # 0   1   1   1   1    Cat    Cat    Cat     Cat
    # 1   2   2   2   2    Dog    Dog    Dog     Dog
    # 2   1   1   3   3    Cat    Cat   Duck    Duck
    # 3   1   2   3   4    Cat    Dog   Duck  Rubbit

    df = pd.DataFrame({
        'AA': [1, 2, 3, 1, 1, 2, 1, 3, 1],
        'BB': [0, 1, 3, 2, 1, 6, 0, 9, 1]
    })
    # print(df)
    df_idxmin = df.loc[df.groupby('AA')['BB'].idxmin()]
    # print(df_idxmin)
    #     AA  BB
    # 0   1   0
    # 1   2   1
    # 2   3   3
    # sort then take first for each
    sort_df = df.sort_values(by='BB').groupby('AA', as_index=False).first()
    print(sort_df)
    #     AA  BB
    # 0   1   0
    # 1   2   1
    # 2   3   3


def df_use_3():
    df = pd.DataFrame(
        {
            'id': [0, 1, 2],
            'x_a': [1.1, 1.1, 1.1],
            'x_b': [1.2, 1.2, 1.2],
            'y_a': [1.11, 1.11, 1.11],
            'y_b': [1.22, 1.22, 1.22]
        }
    )
    # print(df)
    #     id   x1   y1    x2    y2
    # 0   0  1.1  1.2  1.11  1.22
    # 1   1  1.1  1.2  1.11  1.22
    # 2   2  1.1  1.2  1.11  1.22
    # as Labelled index
    df = df.set_index('id')
    # print(df)
    #     x1   y1    x2    y2
    # id
    # 0   1.1  1.2  1.11  1.22
    # 1   1.1  1.2  1.11  1.22
    # 2   1.1  1.2  1.11  1.22

    df.columns = pd.MultiIndex.from_tuples([tuple(c.split("_")) for c in df.columns])
    # print(df)
    #     x          y
    # a    b     a     b
    # id
    # 0   1.1  1.2  1.11  1.22
    # 1   1.1  1.2  1.11  1.22
    # 2   1.1  1.2  1.11  1.22

    df = df.stack(0).reset_index(1)
    # print(df)
    #     level_1     a     b
    # id
    # 0        x  1.10  1.20
    # 0        y  1.11  1.22
    # 1        x  1.10  1.20
    # 1        y  1.11  1.22
    # 2        x  1.10  1.20
    # 2        y  1.11  1.22
    # fix the labels (the label 'level_1' got added automatically)
    df.columns = ['col_xy', 'all_a', 'all_b']
    print(df)
    #     col_xy  all_a  all_b
    # id
    # 0       x   1.10   1.20
    # 0       y   1.11   1.22
    # 1       x   1.10   1.20
    # 1       y   1.11   1.22
    # 2       x   1.10   1.20
    # 2       y   1.11   1.22


if __name__ == '__main__':
    # df_use()

    # df_use_2()

    df_use_3()