import pandas as pd

import seaborn as sns

tips = sns.load_dataset('tips')

# tips.to_csv('data/seaborn_tips.csv')

# print(type(tips))


def pd_basic_show_info():

    df = pd.read_csv('data/seaborn_tips.csv', sep=',')
    print(type(df))  # <class 'pandas.core.frame.DataFrame'>
    print(df.head())
    """
       Unnamed: 0  total_bill   tip     sex smoker  day    time  size
    0           0       16.99  1.01  Female     No  Sun  Dinner     2
    1           1       10.34  1.66    Male     No  Sun  Dinner     3
    2           2       21.01  3.50    Male     No  Sun  Dinner     3
    3           3       23.68  3.31    Male     No  Sun  Dinner     2
    4           4       24.59  3.61  Female     No  Sun  Dinner     4
    """
    print(df.shape)  # (244, 8)  rows and columns of a DataFrame
    print(df.columns)
    # Index(['Unnamed: 0', 'total_bill', 'tip', 'sex', 'smoker', 'day', 'time',
    #        'size'],
    #       dtype='object')
    print(type(df.columns))  # <class 'pandas.core.indexes.base.Index'>
    print(df.dtypes)
    # Unnamed: 0      int64
    # total_bill    float64
    # tip           float64
    # sex            object
    # smoker         object
    # day            object
    # time           object
    # size            int64
    # dtype: object
    print(df.info())
    # <class 'pandas.core.frame.DataFrame'>
    # RangeIndex: 244 entries, 0 to 243
    # Data columns (total 8 columns):
    #  #   Column      Non-Null Count  Dtype
    # ---  ------      --------------  -----
    #  0   Unnamed: 0  244 non-null    int64
    #  1   total_bill  244 non-null    float64
    #  2   tip         244 non-null    float64
    #  3   sex         244 non-null    object
    #  4   smoker      244 non-null    object
    #  5   day         244 non-null    object
    #  6   time        244 non-null    object
    #  7   size        244 non-null    int64
    # dtypes: float64(2), int64(2), object(4)
    # memory usage: 15.4+ KB
    # None
    tip_df = df['tip']
    print(tip_df.head())
    # 0    1.01
    # 1    1.66
    # 2    3.50
    # 3    3.31
    # 4    3.61
    # Name: tip, dtype: float64
    print('tail\n', tip_df.tail())
    # tail
    # 239    5.92
    # 240    2.00
    # 241    2.00
    # 242    1.75
    # 243    3.00
    # Name: tip, dtype: float64
    subset = df[['total_bill', 'tip', 'sex']]
    print('subset\n', subset.head())
    # subset
    #   total_bill   tip     sex
    # 0       16.99  1.01  Female
    # 1       10.34  1.66    Male
    # 2       21.01  3.50    Male
    # 3       23.68  3.31    Male
    # 4       24.59  3.61  Female
    print('tail of subset \n', subset.tail(2))
    # tail of subset
    #       total_bill   tip     sex
    # 242       17.82  1.75    Male
    # 243       18.78  3.00  Female


if __name__ == '__main__':

    pd_basic_show_info()