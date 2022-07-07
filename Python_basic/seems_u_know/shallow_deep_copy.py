import copy

"""
    Reference: https://medium.com/geekculture/if-you-ask-these-4-python-questions-you-might-still-be-a-nooby-7e4c503aa1c3
"""


def shallow_copy():
    numbers = [1, 2, 3]
    numbers_copied = numbers

    numbers.append(4)
    print(numbers)
    # [1, 2, 3, 4]
    print(numbers_copied)  # It expects to be [1, 2, 3], but it's not
    # [1, 2, 3, 4]


def deep_copy():
    numbers = [1, 2, 3]
    numbers_copied = copy.deepcopy(numbers)

    numbers.append(4)
    print(numbers)
    # [1, 2, 3, 4]
    print(numbers_copied)  # It is [1, 2, 3]
    # [1, 2, 3]


if __name__ == '__main__':
    # shallow_copy()
    deep_copy()