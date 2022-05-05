import heapq

"""
    Q: How to get Max or Min N elements list from a Set?
    A: heapq has two functions which can perfectly solve this problem
    nlargest() and nsmallest()

"""


def do_heapq():
    numbers = [12, 1998, 0, -66, 5, 20, 99, 24]

    largest = heapq.nlargest(3, numbers)
    smallest = heapq.nsmallest(3, numbers)

    print(largest, '\n', smallest)


def use_heapq():
    tools = [
        {'App': 'Agenda',  'use_time': 2.5, 'like': 7.8},
        {'App': 'WeChat',  'use_time': 0.1, 'like': 8.8},
        {'App': 'Pycharm',  'use_time': 6.5, 'like': 19.8},
        {'App': 'Google',  'use_time': 2.6, 'like': 29.8},
        {'App': 'Safari',  'use_time': 1.2, 'like': 1.8},
        {'App': 'Gmail',  'use_time': 0.2, 'like': 0.8},
        {'App': 'Music',  'use_time': 0.8, 'like': 2.8},
        {'App': 'IntelliJ',  'use_time': 8.5, 'like': 9.8},
        {'App': 'iTerm',  'use_time': 3.2, 'like': 9.1},
    ]
    use_time_less_app = heapq.nsmallest(2, tools, key=lambda s: s['use_time'])
    like_most_app = heapq.nlargest(2, tools, key=lambda s: s['like'])

    print('Spend only few hours app: ', use_time_less_app)
    print('Like it very much app: ', like_most_app)


if __name__ == '__main__':

    # do_heapq()

    use_heapq()