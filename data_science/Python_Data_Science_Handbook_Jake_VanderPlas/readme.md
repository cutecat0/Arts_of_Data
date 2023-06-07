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


## Navigation shortcuts¶
    Keystroke	Action
    Ctrl-a	Move cursor to the beginning of the line
    Ctrl-e	Move cursor to the end of the line
    Ctrl-b or the left arrow key	Move cursor back one character
    Ctrl-f or the right arrow key	Move cursor forward one character


## Text Entry Shortcuts
    Keystroke	Action
    Backspace key	Delete previous character in line
    Ctrl-d	Delete next character in line
    Ctrl-k	Cut text from cursor to end of line
    Ctrl-u	Cut text from beginning of line to cursor
    Ctrl-y	Yank (i.e. paste) text that was previously cut
    Ctrl-t	Transpose (i.e., switch) previous two characters 

## Command History Shortcuts
    Keystroke	Action
    Ctrl-p (or the up arrow key)	Access previous command in history
    Ctrl-n (or the down arrow key)	Access next command in history
    Ctrl-r	Reverse-search through command history

## Miscellaneous Shortcuts
    Ctrl-l	Clear terminal screen
    Ctrl-c	Interrupt current Python command
    Ctrl-d	Exit IPython session
    The Ctrl-c in particular can be useful when you inadvertently start a very long-running job.


# Ipython Magic Commands
## Pasting Code Blocks: %paste and %cpaste
    In [5]: %paste
    def donothing(x):
    ...:     return x
    ## -- End pasted text --
    
    In [6]: donothing(10)
    Out[6]: 10

    In [8]: %cpaste
    Pasting code; enter '--' alone on the line to stop or use Ctrl-D.
    :In [1]: def donothing(x):
    ...:     return x
    ...:
    
    In [9]: donothing(100)
    Out[9]: 100

## Running External Code: %run
    In [18]: %run myscript.py
    1 square is 1
    2 square is 4
    3 square is 9

## Timing Code Execution: %timeit
    In [21]: %timeit L = [n ** 2 for n in range(1000)]
    220 µs ± 1.03 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
    
    In [23]: %%timeit
    ...: L = []
    ...: for n in range(1000):
    ...:     L.append(n ** 2)
    ...: 
    ...: 

    257 µs ± 3.88 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

## Help on Magic Functions: ?, %magic, and %lsmagic
    %timeit?
    In [30]: %lsmagic
    In [31]: %magic

# Input and Output History
## Ipython's IN and Out Objects
    In [32]: import math

    In [33]: math.sin(20)
    Out[33]: 0.9129452507276277
    
    In [34]: math.cos(20)
    Out[34]: 0.40808206181339196

    In [35]: print(In)

    In [36]: Out

    In [43]: print(Out)
    {6: 10, 9: 100, 27: <IPython.core.magics.basic.MagicsDisplay object at 0x7f9deac09310>, 30: <IPython.core.magics.basic.MagicsDisplay object at 0x7f9def5c7950>, 33: 0.9129452507276277, 34: 0.40808206181339196}

    In result is  a list while Out reesult is a tuple dict

    In [44]: print(In[1])
    def donothing(x):
    return x
    
    In [46]: print(Out[6])
    10






    
    


    











