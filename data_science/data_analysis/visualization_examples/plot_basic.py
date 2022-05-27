import matplotlib.pyplot as plt


def line_dot_pic():
    year = [2001, 2010, 2020, 2030]
    pop = [2.519, 3.629, 5.263, 6.972]

    plt.plot(year, pop)  # line plot
    plt.show()

    plt.scatter(year, pop)  # dot plot
    plt.xscale('log')
    plt.show()


def histogram_pic():
    values = [0, 0.6, 1.2, 1.3, 2.2, 2.6, 3.3, 3.5, 3.9, 4.6, 6.6]

    plt.hist(values, bins=3)
    plt.show()
    plt.clf()

    plt.hist(values)  # bins default is 10
    plt.show()
    plt.clf()

    plt.hist(values, bins=5)
    plt.show()


if __name__ == '__main__':

    # line_dot_pic()
    histogram_pic()
