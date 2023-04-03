"""
    Reference: https://medium.com/geekculture/if-you-ask-these-4-python-questions-you-might-still-be-a-nooby-7e4c503aa1c3

    Q3: What's the difference between a module, package, library and framework in Python?
    A3: 1. Module is a x.pt which contains different functions so on, use import x to call a module.
            some well-known modules are os, re and datetime.
        2. when developing large applications, the number of modules will increase, we group modules into a package.
            A package is a collection of modules that contain a __init__.py file.
            some well-known packages are pandas, numpy.
        3. Library is usually a collection of packages.
            some well-known libraries are requests, matplotlib, beautifulsoup
            (pandas are also usually known as library)
        4. Framework is a little bit like library, but frameworks contain a basic workflow and architecture of an application.
            some well-known frameworks are Django or Flask.

"""
import cat  # way 1 import all module from cat.py

from cat import cute_cat  # way 2 just import one function from module cat
import os
import pandas


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

    """
        2. Package: to use a package, use import package.subpackage.module1, or from package.subpackage import module1
    """


if __name__ == '__main__':
    module_eg()
