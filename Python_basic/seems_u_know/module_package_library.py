"""
    Reference: https://medium.com/geekculture/if-you-ask-these-4-python-questions-you-might-still-be-a-nooby-7e4c503aa1c3

    Q3: What's the difference between a module, package, library and framework in Python?
    A3: 1. module is a x.pt which contains different functions so on, use import x to call a module.

"""
import cat  # way 1 import all module from cat.py

from cat import cute_cat  # way 2 just import one function from module cat


def module_eg():
    """
        1. Module
        module is just a x.py file which contains different variables, functions or classes.
        Here we already have a cat.py which owns a cute_cat(name) function, and if we want to
        use the cat module, we need to import cat module at first and then use its function
    """
    name = 'Simba'
    cat.cute_cat(name)
    # This cute cat's name is Simba

    """
        Modules usually contains more items than the above example, so if we don't need all items,
        we'd better use from cat import cute_cat
    """
    name_2 = 'Tom'
    cute_cat(name_2)
    # This cute cat's name is Tom


if __name__ == '__main__':
    module_eg()
