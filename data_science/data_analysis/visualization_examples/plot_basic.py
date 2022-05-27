import matplotlib.pyplot as plt


def line_dot_pic():
    year = [2001, 2010, 2020, 2030, 2050, 2100]
    pop = [2.519, 3.629, 5.263, 6.972, 7.222, 10.525]

    year = [1800, 1850, 1900] + year
    pop = [1.0, 1.262, 1.650] + pop

    plt.plot(year, pop)  # line plot

    # customization
    plt.xlabel('Year')
    plt.ylabel('Population')

    plt.title('World Population Projections')

    plt.yticks([i for i in range(14) if i % 2 == 0],
               [str(i) + 'B' for i in range(14) if i % 2 == 0])

    plt.show()

    plt.scatter(year, pop)  # dot plot
    # plt.xscale('log')
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

    line_dot_pic()
    # histogram_pic()
