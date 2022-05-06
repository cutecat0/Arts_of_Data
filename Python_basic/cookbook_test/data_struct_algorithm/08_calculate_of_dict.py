"""
    Q: How to calculate in a dict?
    A: use zip() turn around the order of the key and value of the dict
"""


def calculate_dict():
    apps = {
        'Agenda': 82.3,
        'WeChat': 88.1,
        'Google': 90.2,
        'IntelliJ': 18.8,
        'Music': 6.6
    }

    lowest_score = min(zip(apps.values(), apps.keys()))
    print(lowest_score)  # (6.6, 'Music')

    best_score = max(zip(apps.values(), apps.keys()))
    print(best_score)  # (90.2, 'Google')

    sorted_score = sorted(zip(apps.values(), apps.keys()))
    print(sorted_score)
    # [(6.6, 'Music'), (18.8, 'IntelliJ'), (82.3, 'Agenda'), (88.1, 'WeChat'), (90.2, 'Google')]

    # normal way
    lowest = min(apps, key=lambda k: apps[k])
    print(lowest, apps[lowest])  # Music 6.6


if __name__ == '__main__':

    calculate_dict()