references:

https://github.com/jakevdp/PythonDataScienceHandbook

https://www.oreilly.com/library/view/python-data-science/9781491912126/

online read: 

https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/00.00-Preface.ipynb

or 

https://jakevdp.github.io/PythonDataScienceHandbook/00.00-preface.html


what?

The skills of A statistician who knows how to model and summarize datasets (which are growing ever larger);

The skills of a computer scientist who can design and use algorithms to efficiently store, process and visualize this data;

And the domain expertise: what we might think of as "classical" training in a subject--necessary to both formulate the right 
questions and to put their answers in context.

https://github.com/jakevdp/WhirlwindTourOfPython

Outline of the Book

Each chapter of this book focuses on a particular package or tool that contributes a fundamental piece of the Python Data Sciece story.

IPython and Jupyter: these packages provide the computational environment in which many Python-using data scientists work.

NumPy: this library provides the ndarray for efficient storage and manipulation of dense data arrays in Python.

Pandas: this library provides the DataFrame for efficient storage and manipulation of labeled/columnar data in Python.

Matplotlib: this library provides capabilities for a flexible range of data visualizations in Python.

Scikit-Learn: this library provides efficient & clean Python implementations of the most important and established machine learning algorithms.


The Python Data Science Handbook by Jake VanderPlas (O’Reilly). Copyright 2016 Jake VanderPlas, 978-1-491-91205-8.


IPython (short for Interactive Python) 

    ipython
    Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52)
    Type 'copyright', 'credits' or 'license' for more information
    IPython 7.20.0 -- An enhanced Interactive Python. Type '?' for help.

jupyter notebook

    http://localhost:8889/edit/ArtsofData/data_science/Python_Data_Science_Handbook_Jake_VanderPlas/readme.md

    help(max)
    max?
    In [10]: L = [1, 2, 3]

    In [11]: L.insert?
    Signature: L.insert(index, object, /)
    Docstring: Insert object before index.
    Type:      builtin_function_or_method
    
    In [12]: L?
    Type:        list
    String form: [1, 2, 3]
    Length:      3
    Docstring:  
    Built-in mutable sequence.
    
    If no argument is given, the constructor creates a new empty list.
    The argument must be an iterable if specified.
    
    In [13]: def sum(a, b):
    ...:     return a + b
    ...: 

    In [14]: sum?
    Signature: sum(a, b)
    Docstring: <no docstring>
    File:      ~/github_projects/ArtsofData/data_science/python_part_basic/cookbook_practice/data_struct_algorithm/<ipython-input-13-8e3c0ca1d2eb>
    Type:      function

    In [17]: sum??
    Signature: sum(a, b)
    Docstring: <no docstring>
    Source:   
    def sum(a, b):
    return a + b
    File:      ~/github_projects/ArtsofData/data_science/python_part_basic/cookbook_practice/data_struct_algorithm/<ipython-input-13-8e3c0ca1d2eb>
    Type:      function
    
    In [24]: L.<TAB>
            append()  count()   insert()  reverse()
            clear()   extend()  pop()     sort()   
            copy()    index()   remove()  
    In [25]: L.c<TAB>
             clear() count()
             copy()  
    In [25]: L.co<TAB>
              copy()  count()
    In [44]: L.__
        __add__             __delitem__         __format__()        __gt__              __init__            __len__             __new__()           __reversed__()      __sizeof__()       
        __class__           __dir__()           __ge__              __hash__            __init_subclass__() __lt__              __reduce__()        __rmul__            __str__            
        __contains__        __doc__             __getattribute__    __iadd__            __iter__            __mul__             __reduce_ex__()     __setattr__         __subclasshook__() 
        __delattr__         __eq__              __getitem__()       __imul__            __le__              __ne__              __repr__            __setitem__                            

    In [45]: from itertools import combinations, c
                                               chain                           compress()                     
                                               combinations()                  count()                        
                                               combinations_with_replacement() cycle()                        


    In [50]: *Warning?
    BytesWarning
    DeprecationWarning
    FutureWarning
    ImportWarning
    PendingDeprecationWarning
    ResourceWarning
    RuntimeWarning
    SyntaxWarning
    UnicodeWarning
    UserWarning
    Warning
    
    In [51]: str.*find*?
    str.find
    str.rfind


    














