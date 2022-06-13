import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


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


if __name__ == '__main__':
    # standard_plot()
    # right_plot()
    # left_plot()
    kurtosis_plot()