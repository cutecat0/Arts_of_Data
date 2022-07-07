import copy

"""
    Reference: https://medium.com/geekculture/if-you-ask-these-4-python-questions-you-might-still-be-a-nooby-7e4c503aa1c3
    
    Q1: Copying an object is as simple as using "=", right?
    A1: "=" is just a shallow copy of the object, when the original object changes, the copy one also change at the same time.
    Using package copy and copy.deepcopy can solve this. 
"""


def shallow_copy():
    """
        Here the = operator just returns to a shallow copy of an object
        when the original object change, the copy one also change.
    """
    numbers = [1, 2, 3]
    numbers_copied = numbers

    numbers.append(4)
    print(numbers)
    # [1, 2, 3, 4]
    print(numbers_copied)  # It expects to be [1, 2, 3], but it's not
    # [1, 2, 3, 4]


def deep_copy():
    """
        If u want to copy an object to another and keep it unique from the original object,
        u shold use deep copy not just the "=" operator which is just a shallow copy
        deep copy can use "import copy then use copy.deepcopy(obj1) to solve.
    """
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