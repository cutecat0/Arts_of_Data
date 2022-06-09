import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')


def hist_plot():
    fig, ax = plt.subplots()
    ax = tips['total_bill'].plot.hist()
    plt.show()


def hist_plot_v2():
    fig, ax = plt.subplots()
    ax = tips[['total_bill', 'tip']].plot.hist(alpha=0.6, bins=20, ax=ax)
    plt.show()


def kde_plot():
    fig, ax = plt.subplots()
    ax = tips['tip'].plot.kde()
    plt.show()


def scatter_plot():
    fig, ax = plt.subplots()
    ax = tips.plot.scatter(x='total_bill', y='tip', ax=ax, )
    plt.show()


def hexbin_plot():
    fig, ax = plt.subplots()
    ax = tips.plot.hexbin(x='total_bill', y='tip', gridsize=16, ax=ax)
    plt.show()


def box_plot():
    fig, ax = plt.subplots()
    ax = tips.plot.box(ax=ax)
    plt.show()


if __name__ == '__main__':
    # hist_plot()
    # hist_plot_v2()
    # kde_plot()
    # scatter_plot()
    # hexbin_plot()
    box_plot()