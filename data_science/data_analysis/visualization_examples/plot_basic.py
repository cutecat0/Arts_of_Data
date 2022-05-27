import matplotlib.pyplot as plt


def pic():
    year = [2001, 2010, 2020, 2030]
    pop = [2.519, 3.629, 5.263, 6.972]

    plt.plot(year, pop)  # line plot
    plt.show()

    plt.scatter(year, pop)  # dot plot
    plt.show()


if __name__ == '__main__':
    pic()
