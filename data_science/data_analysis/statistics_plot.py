import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


def standard_plot():
    ma, sd = 0.0, 1.0
    x = np.linspace(ma - 4 * sd, ma + 4 * sd, 50)  # x range
    y = stats.norm.pdf(x)

    plt.plot(x, y, "r", linewidth=2)
    plt.grid(True)

    plt.show()


def right_plot():
    ma, sd = 0.0, 1.0
    x = np.linspace(ma - 2 * sd, ma + 5 * sd, 50)
    y = stats.norm.pdf(x)

    plt.plot(x, y, "g", linewidth=2)
    plt.grid(True)

    plt.show()


def left_plot():
    ma, sd = 0.0, 1.0
    x = np.linspace(ma - 5 * sd, ma + 2 * sd, 50)
    y = stats.norm.pdf(x)

    plt.plot(x, y, "b", linewidth=2)
    plt.grid(True)

    plt.show()


def kurtosis_plot():
    ma, sd = 0.0, 1.0
    sd2, sd3 = 2.0, 3.0

    x = np.linspace(ma - 3 * sd, ma + 3 * sd, 50)
    y = stats.norm.pdf(x)
    plt.plot(x, y, "r", linewidth=2, label='standard=1.0')

    x2 = np.linspace(ma - 6 * sd, ma + 6 * sd, 50)
    y2 = stats.norm.pdf(x2, ma, sd2)
    plt.plot(x2, y2, "g", linewidth=2, label='standard=2.0')

    x3 = np.linspace(ma - 10 * sd, ma + 10 * sd, 50)
    y3 = stats.norm.pdf(x3, ma, sd3)
    plt.plot(x3, y3, "b", linewidth=2, label='standard=3.0')

    plt.grid(True)
    plt.title('Kurtosis Plot ')
    plt.legend()

    plt.show()


def _95_median_plot():
    data = np.array([i for i in range(100)])
    ma, sd = 0.0, 1.0

    median_value = np.median(data)
    _25_tp_value = np.percentile(data, 25)
    _95_tp_value = np.percentile(data, 95)

    print(f'median={median_value}\n25% TP={_25_tp_value}\n95% TP={_95_tp_value}')

    x = np.linspace(ma - 3 * sd, ma + 3 * sd, 100)
    y = stats.norm.pdf(x)
    plt.plot(x, y, 'r', label='Standard')

    x2 = np.linspace(ma - 6 * sd, ma + 6 * sd, 100)
    y2 = stats.norm.pdf(x2, ma, 2.0)
    plt.plot(x2, y2, 'g', label='25% TP')

    x3 = np.linspace(ma - 10 * sd, ma + 10 * sd, 100)
    y3 = stats.norm.pdf(x3, ma, 3.0)
    plt.plot(x3, y3, 'b', label='95% TP')

    plt.legend()
    plt.title('TP 25%、 95% Plot')
    plt.grid(True)

    plt.show()


def tp_vs_average():
    data = [0.17, 0.17, 0.18, 0.20, 0.21, 0.17, 0.16, 0.17, 0.17, 0.18, 0.15, 0.15, 0.20, 0.19, 0.20, 0.15, 0.15, 0.16, 0.16, 0.17, 0.20]
    data2 = [i * 1.2 if i < 0.20 else i * 0.8 for i in data]
    avg = sum(data2) / len(data2)
    median = np.median(data2)
    tp95 = np.percentile(data2, 95)
    tp25 = np.percentile(data2, 25)

    print(f'avg={avg}\nmedian={median}\nTP95={tp95}\nTP25={tp25}')

    index = [i for i in range(len(data))]
    plt.plot(index, data, 'lightgreen', label='Ratio')
    plt.plot(index, data2, 'lightblue', label='Score')

    lr = LinearRegression()
    predicted = lr.fit(np.array(index).reshape(-1, 1), np.array(data).reshape(-1, 1))
    Y_predict = lr.predict(np.array(index).reshape(-1, 1))
    pa, pb = predicted.coef_[0], predicted.intercept_[0]
    mse = mean_squared_error(data, Y_predict)
    plt.plot(index, Y_predict, 'pink', label='LineRegression of Ratio')
    print(pa, pb, mse)

    plt.xlabel('Index')
    plt.ylabel('Ratio(%)')
    plt.title('Ratio of Data' + f' y={pa:.3f}x + {pb:.3f} MSE={mse}')

    plt.legend()

    plt.show()


if __name__ == '__main__':
    # standard_plot()
    # right_plot()
    # left_plot()
    # kurtosis_plot()
    # _95_median_plot()
    tp_vs_average()
