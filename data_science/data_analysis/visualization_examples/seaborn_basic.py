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


def seaborn_example():
    tips = sns.load_dataset('tips')
    print(tips.head())


if __name__ == '__main__':

    # anscomde_example()

    seaborn_example()
