import seaborn as sns
import matplotlib.pyplot as plt


def anscomde_example():

    anscombe = sns.load_dataset("anscombe")

    data1 = anscombe[anscombe['dataset'] == 'I']
    data2 = anscombe[anscombe['dataset'] == 'II']
    data3 = anscombe[anscombe['dataset'] == 'III']
    data4 = anscombe[anscombe['dataset'] == 'IV']

    fig = plt.figure()

    axes1 = fig.add_subplot(2, 2, 1)
    axes2 = fig.add_subplot(2, 2, 2)
    axes3 = fig.add_subplot(2, 2, 3)
    axes4 = fig.add_subplot(2, 2, 4)

    axes1.scatter(data1['x'], data1['y'])
    axes2.scatter(data2['x'], data2['y'])
    axes3.scatter(data3['x'], data3['y'])
    axes4.scatter(data4['x'], data4['y'])

    axes1.set_title('Data I')
    axes2.set_title('Data II')
    axes3.set_title('Data III')
    axes4.set_title('Data IV')

    fig.suptitle('anscombe')
    fig.tight_layout()

    fig.show()


def hist_plot():
    tips = sns.load_dataset('tips')
    # print(tips.head())
    """
       total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4
    """
    fig = plt.figure()

    axes1 = fig.add_subplot(1, 1, 1)
    axes1.hist(tips['total_bill'], bins=12)
    axes1.set_title('Histogram of Total Bill')
    axes1.set_xlabel('Frequency')
    axes1.set_ylabel('Total Bill')

    fig.show()


def scatter_plot():
    tips = sns.load_dataset('tips')

    fig = plt.figure()

    axes1 = fig.add_subplot(1, 1, 1)
    axes1.scatter(tips['total_bill'], tips['tip'])
    axes1.set_title('Scatter plot of Total Bill cs Tip')
    axes1.set_xlabel('Toal Bill')
    axes1.set_ylabel('Tip')

    fig.show()


def box_plot():
    tips = sns.load_dataset('tips')
    labels = tips.sex.unique()
    data_list = []
    for i in labels:
        data_list.append(tips[tips.sex == i].tip.to_list())

    fig = plt.figure()
    axes1 = fig.add_subplot(1, 1, 1)
    # axes1.boxplot(
    #     [tips[tips['sex'] == 'Female']['tip'],
    #      tips[tips['sex'] == 'Male']['tip']],
    #     labels=['Female', 'Male']
    # )
    print(data_list)
    axes1.boxplot(data_list, labels=labels, showmeans=True)
    axes1.set_title('Box Plot of Tips by Sex')
    axes1.set_xlabel('Sex')
    axes1.set_ylabel('Tip')

    fig.show()


# create a value with color based on sex
def recode_sex(sex):
    if sex == 'Female':
        return 0
    else:
        return 1


def colored_scatter_plot():
    tips = sns.load_dataset('tips')
    tips['sex_color'] = tips['sex'].apply(recode_sex)

    fig = plt.figure()
    axes1 = fig.add_subplot(1, 1, 1)
    axes1.scatter(
        x=tips['total_bill'],
        y=tips['tip'],

        # 根据聚餐人数设置点的大小，*10以放大不同
        s=tips['size'] * 10,

        # set color for sex
        c=tips['sex_color'],

        # 设置alpha值， 增加点的透明度，用于表现重叠的点
        alpha=0.5
    )
    axes1.set_title('Total Bill vs Tip Colored by Sex & Sized by Size')
    axes1.set_xlabel('Total Bill')
    axes1.set_ylabel('Tip')
    fig.show()


def single_value_plot():
    tips = sns.load_dataset('tips')

    hist, ax = plt.subplots()
    ax = sns.displot(tips['total_bill'], kde=True)  # while kde=True show line
    ax = sns.displot(tips['total_bill'], kde=False)  # line here will not show

    ax.set_titles('Total Bill Histgram with Density Plot')
    plt.show()


def density_plot():
    tips = sns.load_dataset('tips')
    den, ax = plt.subplots()
    ax = sns.distplot(tips['total_bill'], hist=False)
    ax.set_title('Total Bill Density')
    ax.set_xlabel('Total Bill')
    ax.set_ylabel('Unit Probability')
    plt.show()


if __name__ == '__main__':

    # anscomde_example()

    # hist_plot()

    # scatter_plot()

    # box_plot()

    # colored_scatter_plot()

    # single_value_plot()

    density_plot()
