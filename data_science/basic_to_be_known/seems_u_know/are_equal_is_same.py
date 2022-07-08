"""
    Reference: https://medium.com/geekculture/if-you-ask-these-4-python-questions-you-might-still-be-a-nooby-7e4c503aa1c3
    Q4: What's the difference between '=' and '==', are '==' and 'is' the same?
    A4: '==' is used to compare the values of two objects, while 'is' is used to compare the identity!
"""


def is_equal():
    x = 666
    y = 666
    print(x == y)  # True
    print(x is y)  # False
    id(x)   # Out[7]: 140415060721264
    id(y)   # Out[8]: 140415060720336
    """
    x = 200
    y = 200
    id(x)
    Out[12]: 4407616528
    id(y)
    Out[13]: 4407616528
    x == y
    Out[14]: True
    x is y
    Out[15]: True
    """


if __name__ == '__main__':
    is_equal()