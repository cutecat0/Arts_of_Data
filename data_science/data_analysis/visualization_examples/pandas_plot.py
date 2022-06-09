import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')


def hist_plot():
    fig, ax = plt.subplots()
    ax = tips['total_bill'].plot.hist()
    plt.show()


if __name__ == '__main__':
    hist_plot()