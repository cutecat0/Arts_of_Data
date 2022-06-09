import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


tips = sns.load_dataset('tips')


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
    ax = sns.kdeplot(tips['total_bill'])
    ax.set_title('Total Bill Density')
    ax.set_xlabel('Total Bill')
    ax.set_ylabel('Unit Probability')
    plt.show()


def rug_plot():
    tips = sns.load_dataset('tips')
    hist_den_rug, ax = plt.subplots()
    ax = sns.distplot(tips['total_bill'], rug=True)
    ax.set_title('Total Bill Histogram with Density and Rug Plot')
    ax.set_xlabel('Total Bill')
    plt.show()


def count_plot():
    count, ax = plt.subplots()
    ax = sns.countplot('day', data=tips)
    ax.set_title('Count of Days')
    ax.set_xlabel('Day of the Week')
    ax.set_ylabel('Frequency')
    plt.show()


def sns_scatter_plot():
    scatter, ax = plt.subplots()
    ax = sns.regplot(
        x='total_bill',
        y='tip',
        data=tips,
        fit_reg=True,  # if ser fit_reg=False 拟合回归线将不显示
        label='True Data'
    )

    lr = LinearRegression()
    predicted = lr.fit(X=tips['total_bill'].values.reshape(-1, 1),
                       y=tips['tip'].values)
    Y_predict = lr.predict(tips.index.values.reshape(-1, 1))
    pa, pb = predicted.coef_[0], predicted.intercept_

    mse = mean_squared_error(tips['tip'].values.reshape(-1, 1), Y_predict)
    plt.plot(tips.index.values, Y_predict, 'red', label='Liner Regression')

    plt.xlim(0, 50)
    plt.ylim(0, 10)

    ax.set_title('ScatterPlot of Total Bill and Tip' + f'   y={pa:.2f}x + {pb:.2f} MSE={mse:.3f}')
    ax.set_xlabel('Total Bill')
    ax.set_ylabel('Tip')
    plt.show()

    # way2
    # fig = sns.lmplot(
    #     x='total_bill',
    #     y='tip',
    #     data=tips
    # )
    # plt.show()


def sns_joint_plot():
    joint = sns.jointplot(x='total_bill', y='tip', data=tips)
    joint.set_axis_labels(xlabel='Total Bill', ylabel='Tip')

    joint.fig.suptitle('Joint Plot of Total Bill and Tip', fontsize=10, y=1.03)
    plt.show()


def sns_beehive_plot():
    hexbin = sns.jointplot(x='total_bill', y='tip', data=tips, kind='hex')
    hexbin.set_axis_labels(xlabel='Total Bill', ylabel='Tip')
    hexbin.fig.suptitle('Hexbin Joint Plot of Total Bill and Tip', fontsize=10, y=1.03)
    plt.show()


def _2D_kde_plot():
    kde, ax = plt.subplots()
    ax = sns.kdeplot(data=tips['total_bill'], data2=tips['tip'],
                     shade=True)
    ax.set_title('Kernel Density Plot of Total Bill and Tip')
    ax.set_xlabel('Total Bill')
    ax.set_ylabel('Tip')
    plt.show()

    kde_joint = sns.jointplot(x='total_bill', y='tip', data=tips, kind='kde')
    plt.show()


def bar_plot():
    bar, ax = plt.subplots()
    ax = sns.barplot(x='time', y='total_bill', data=tips)
    ax.set_title('Bar plot of average total bill for time of day')
    ax.set_xlabel('Time of day')
    ax.set_ylabel('Average total bill')
    plt.show()


def box_plot():
    """
    min、第一个四分位数、中位数、第三个四分位数、max、（若有）基于四分位差的离散值
    """
    box, ax = plt.subplots()
    ax = sns.boxplot(x='time', y='total_bill', data=tips)
    ax.set_title('Box plot of total bill by time of day')
    ax.set_xlabel('Time of day')
    ax.set_ylabel('Total bill')
    plt.show()


def violin_plot():
    violin, ax = plt.subplots()
    ax = sns.violinplot(x='time', y='total_bill', data=tips)
    ax.set_title('Violin plot of total bill by time of day')
    ax.set_xlabel('Time of day')
    ax.set_ylabel('Total bill')
    plt.show()


def violin_color_plot():
    violin, ax = plt.subplots()
    ax = sns.violinplot(x='time', y='total_bill', hue='sex', data=tips, split=True)
    plt.show()


def pair_plot():
    fig = sns.pairplot(tips)
    plt.show()


def color_pair_plot():
    fig = sns.pairplot(tips, hue='sex')
    plt.show()


def pair_grid_plot():
    pair_grid = sns.PairGrid(tips)
    pair_grid = pair_grid.map_upper(sns.regplot)  # plt.scatter
    pair_grid = pair_grid.map_lower(sns.kdeplot)
    pair_grid = pair_grid.map_diag(sns.distplot, rug=True)
    plt.show()


def color_lmplot():
    scatter = sns.lmplot(x='total_bill', y='tip', data=tips,
                         fit_reg=False,
                         hue='sex',
                         # scatter_kws={'s': tips['size']*10}  # can't work here
                         )
    plt.show()


def color_lmplot_2():
    scatter = sns.lmplot(x='total_bill', y='tip', data=tips,
                         hue='sex', fit_reg=False)
    plt.show()


def color_lmplot_markers():
    scatter = sns.lmplot(x='total_bill', y='tip', data=tips,
                         fit_reg=False,
                         hue='sex',
                         markers=['o', 'x'],
                         # scatter_kws={'s': tips['size']*10}
                         )
    plt.show()


def anscombe_plot():
    anscombe = sns.load_dataset('anscombe')

    anscombe_plot = sns.lmplot(x='x', y='y', data=anscombe,
                               fit_reg=False,
                               col='dataset',
                               col_wrap=2
                               )
    plt.show()


def facet_grid_plot():
    facet = sns.FacetGrid(tips, col='time')
    facet.map(sns.distplot, 'total_bill', rug=True)
    plt.show()


def facet_grid_plot_v2():
    facet = sns.FacetGrid(tips, col='day', hue='sex')
    facet = facet.map(plt.scatter, 'total_bill', 'tip')
    facet = facet.add_legend()
    plt.show()


def lmplot_v3():
    fig = sns.lmplot(x='total_bill', y='tip', data=tips, fit_reg=False,
                     hue='sex', col='day',
                     # col_wrap=2
                     )
    plt.show()


def facet_grid_plot_v3():
    facet = sns.FacetGrid(tips, col='time', row='smoker', hue='sex')
    facet = facet.map(plt.scatter, 'total_bill', 'tip')
    plt.show()


def facet_plot():
    facet = sns.factorplot(x='day', y='total_bill',
                           hue='sex', data=tips,
                           row='smoker', col='time',
                           kind='violin')
    plt.show()


if __name__ == '__main__':

    # anscomde_example()

    # hist_plot()

    # scatter_plot()

    # box_plot()

    # colored_scatter_plot()

    # single_value_plot()

    # density_plot()

    # rug_plot()
    # count_plot()
    # sns_scatter_plot()
    # sns_joint_plot()
    # sns_beehive_plot()
    # _2D_kde_plot()
    # bar_plot()
    # box_plot()
    # violin_plot()
    # pair_plot()
    # color_pair_plot()
    # pair_grid_plot()
    # violin_color_plot()
    # color_lmplot()
    # color_lmplot_2()
    # color_lmplot_markers()
    # anscombe_plot()
    # facet_grid_plot()
    # facet_grid_plot_v2()
    # lmplot_v3()

    # facet_grid_plot_v3()
    facet_plot()