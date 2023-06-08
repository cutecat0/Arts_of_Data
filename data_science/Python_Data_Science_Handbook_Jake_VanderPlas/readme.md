##references:

https://github.com/jakevdp/PythonDataScienceHandbook

https://www.oreilly.com/library/view/python-data-science/9781491912126/

###online read: 

https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/00.00-Preface.ipynb

or 

https://jakevdp.github.io/PythonDataScienceHandbook/00.00-preface.html


##what?

The skills of A statistician who knows how to model and summarize datasets (which are growing ever larger);

The skills of a computer scientist who can design and use algorithms to efficiently store, process and visualize this data;

And the domain expertise: what we might think of as "classical" training in a subject--necessary to both formulate the right 
questions and to put their answers in context.

https://github.com/jakevdp/WhirlwindTourOfPython

###Outline of the Book

Each chapter of this book focuses on a particular package or tool that contributes a fundamental piece of the Python Data Sciece story.

**IPython and Jupyter**: these packages provide the computational environment in which many Python-using data scientists work.

**NumPy:** this library provides the ndarray for efficient storage and manipulation of dense data arrays in Python.

**Pandas**: this library provides the DataFrame for efficient storage and manipulation of labeled/columnar data in Python.

**Matplotlib**: this library provides capabilities for a flexible range of data visualizations in Python.

**Scikit-Learn**: this library provides efficient & clean Python implementations of the most important and established machine learning algorithms.


The Python Data Science Handbook by Jake VanderPlas (O’Reilly). Copyright 2016 Jake VanderPlas, 978-1-491-91205-8.


##IPython (short for Interactive Python) 

    ipython
    Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52)
    Type 'copyright', 'credits' or 'license' for more information
    IPython 7.20.0 -- An enhanced Interactive Python. Type '?' for help.

##jupyter notebook

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


## Navigation shortcuts
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
## Pasting Code Blocks: `%paste` and `%cpaste`
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

## Running External Code: `%run`
    In [18]: %run myscript.py
    1 square is 1
    2 square is 4
    3 square is 9

## Timing Code Execution: `%timeit`
    In [21]: %timeit L = [n ** 2 for n in range(1000)]
    220 µs ± 1.03 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
    
    In [23]: %%timeit
    ...: L = []
    ...: for n in range(1000):
    ...:     L.append(n ** 2)
    ...: 
    ...: 

    257 µs ± 3.88 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

## Help on Magic Functions: `?`, `%magic`, and `%lsmagic`
    %timeit?
    In [30]: %lsmagic
    In [31]: %magic

# Input and Output History
## Ipython's `IN` and `Out` Objects
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

    In [47]: Out
    Out[47]:
    {6: 10,
    9: 100,
    27: 

    In [49]: Out[6] ** 2 + Out[9] ** 2
    Out[49]: 10100

## Underscore Shortcuts and Previous Outputs
    In [52]: print(_)
    36.48212121148016
    
    In [53]: print(__)
    0.6080353535246694
    
    In [54]: print(___)
    10100

    In [56]: Out[6]
    Out[56]: 10
    
    In [57]: _6
    Out[57]: 10
    
    In [58]: 

## Suppressing Output
    In [58]: math.sin(2) + math.cos(2)
    Out[58]: 0.4931505902785393
    
    In [59]: 14 in Out
    Out[59]: False

## Related Magic Commands
    In [60]: %history -n 1-4
    1:
    def donothing(x):
    return x
    2:
    In [1]: def donothing(x):
    ...:     return x
    ...:
    3: %paste
    4:
    def donothing(x):
    ...:     return x
    
    In [61]: 

# Ipython and Shell Commands
## Quick Introduction to the shell
    In [63]: pwd
    Out[63]: '/Users/xxx/github_projects/ArtsofData/data_science/Python_Data_Science_Handbook_Jake_VanderPlas'
    
    In [64]: ls
    myscript.py  readme.md
    
    In [65]: cd ..
    /Users/xxx/github_projects/ArtsofData/data_science
    
    In [66]: pwd
    Out[66]: '/Users/xxx/github_projects/ArtsofData/data_science'
    
    In [67]: ls
    Julia_study/                                  linux_command/
    Python_Data_Science_Handbook_Jake_VanderPlas/ python_part_basic/
    QoS/                                          readme.md
    data_analysis/                                sql_part/
    intersting_examples/
    
    In [68]: cd Python_Data_Science_Handbook_Jake_VanderPlas/
    /Users/xxx/github_projects/ArtsofData/data_science/Python_Data_Science_Handbook_Jake_VanderPlas
    
    In [69]: ls
    myscript.py  readme.md
    
    In [70]: mkdir myproject
    
    In [71]: ls
    myproject/   myscript.py  readme.md

# Shell Commands in IPython
    In [77]: !ls
    myproject       myscript.py     readme.md
    
    In [78]: ls
    myproject/   myscript.py  readme.md
    
    In [79]: !pwd
    /Users/xxx/github_projects/ArtsofData/data_science/Python_Data_Science_Handbook_Jake_VanderPlas

    In [81]: pwd
    Out[81]: '/Users/xxx/github_projects/ArtsofData/data_science/Python_Data_Science_Handbook_Jake_VanderPlas'
    
## Passing Values to and from the Shell
    In [82]: contents = !ls

    In [83]: print(contents)
    ['myproject', 'myscript.py', 'readme.md']
    
    In [84]: directory = !pwd

    In [85]: print(directory)
    ['/Users/xxx/github_projects/ArtsofData/data_science/Python_Data_Science_Handbook_Jake_VanderPlas']
    
    In [86]: type(directory)
    Out[86]: IPython.utils.text.SList

    In [87]: message = "hey from Three body"

    In [88]: !echo {message}
    hey from Three body

## Shell-Related Magic Commands
    In [89]: !pwd
    /Users/xxx/github_projects/ArtsofData/data_science/Python_Data_Science_Handbook_Jake_VanderPlas
    
    In [90]: !cd ..
    
    In [91]: !pwd
    /Users/xxx/github_projects/ArtsofData/data_science/Python_Data_Science_Handbook_Jake_VanderPlas
    
    In [92]: %cd ..
    /Users/xxx/github_projects/ArtsofData/data_science

    In [99]: cd myproject/
    /Users/xxx/github_projects/ArtsofData/data_science/Python_Data_Science_Handbook_Jake_VanderPlas/myproject
    
    In [100]: ls
    
    In [101]: mkdir tmp
    
    In [108]: cp ../myscript.py tmp/

    In [111]: ls
    myscript.py

    In [117]: rm -r tmp/

    In [118]: ls

# Errors and Debugging
## Controlling Exceptions:
    In [121]: def func1(a, b):
     ...:     return a / b
     ...: 

    In [122]: def func2(x):
    ...:     a = x
    ...:     b = x - 1
    ...:     return func1(a, b)
    ...:
    
    In [123]: func2(1)
    ---------------------------------------------------------------------------
    ZeroDivisionError                         Traceback (most recent call last)
    <ipython-input-123-7cb498ea7ed1> in <module>
    ----> 1 func2(1)
    
    <ipython-input-122-25e419aa729c> in func2(x)
          2     a = x
          3     b = x - 1
    ----> 4     return func1(a, b)
          5 
    
    <ipython-input-121-165aea2c932f> in func1(a, b)
          1 def func1(a, b):
    ----> 2     return a / b
          3 
    
    ZeroDivisionError: division by zero

    In [124]: %xmode Plain
    Exception reporting mode: Plain
    
    In [125]: func2(1)
    Traceback (most recent call last):
    File "<ipython-input-125-7cb498ea7ed1>", line 1, in <module>
    func2(1)
    File "<ipython-input-122-25e419aa729c>", line 4, in func2
    return func1(a, b)
    File "<ipython-input-121-165aea2c932f>", line 2, in func1
    return a / b
    ZeroDivisionError: division by zero


    In [126]: %xmode Verbose
    Exception reporting mode: Verbose
    
    In [127]: func2(1)
    ---------------------------------------------------------------------------
    ZeroDivisionError                         Traceback (most recent call last)
    <ipython-input-127-7cb498ea7ed1> in <module>
    ----> 1 func2(1)
    global func2 = <function func2 at 0x7f9deadbb4d0>
    
    <ipython-input-122-25e419aa729c> in func2(x=1)
          2     a = x
          3     b = x - 1
    ----> 4     return func1(a, b)
            global func1 = <function func1 at 0x7f9df036b050>
            a = 1
            b = 0
          5 
    
    <ipython-input-121-165aea2c932f> in func1(a=1, b=0)
          1 def func1(a, b):
    ----> 2     return a / b
            a = 1
            b = 0
          3 
    
    ZeroDivisionError: division by zero

## Debugging: When Reading Tracebacks Is Not Enough
    In [128]: %debug
    > <ipython-input-121-165aea2c932f>(2)func1()
    1 def func1(a, b):
    ----> 2     return a / b
    3
    
    ipdb> print(a)
    1
    ipdb> print(b)
    0
    ipdb> quit

    In [129]: %debug
    > <ipython-input-121-165aea2c932f>(2)func1()
    1 def func1(a, b):
    ----> 2     return a / b
    3
    
    ipdb> up
    > <ipython-input-122-25e419aa729c>(4)func2()
    1 def func2(x):
    2     a = x
    3     b = x - 1
    ----> 4     return func1(a, b)
    5
    
    ipdb> print(x)
    1
    ipdb> up
    > <ipython-input-127-7cb498ea7ed1>(1)<module>()
    ----> 1 func2(1)
    
    ipdb> down
    > <ipython-input-122-25e419aa729c>(4)func2()
    1 def func2(x):
    2     a = x
    3     b = x - 1
    ----> 4     return func1(a, b)
    5
    
    ipdb> quit

    In [130]: %xmode Plain
    Exception reporting mode: Plain
    
    In [131]: %pdb on
    Automatic pdb calling has been turned ON
    
    In [132]: func2(1)
    Traceback (most recent call last):
    File "<ipython-input-132-7cb498ea7ed1>", line 1, in <module>
    func2(1)
    File "<ipython-input-122-25e419aa729c>", line 4, in func2
    return func1(a, b)
    File "<ipython-input-121-165aea2c932f>", line 2, in func1
    return a / b
    ZeroDivisionError: division by zero
    
    > <ipython-input-121-165aea2c932f>(2)func1()
    1 def func1(a, b):
    ----> 2     return a / b
    3
    
    ipdb> print(b)
    0
    ipdb> quit

## Partial list of debugging commands

    Command	Description
    list	Show the current location in the file
    h(elp)	Show a list of commands, or find help on a specific command
    q(uit)	Quit the debugger and the program
    c(ontinue)	Quit the debugger, continue in the program
    n(ext)	Go to the next step of the program
    <enter>	Repeat the previous command
    p(rint)	Print variables
    s(tep)	Step into a subroutine
    r(eturn)	Return out of a subroutine

# Profiling and Timing Code
    %time: Time the execution of a single statement
    %timeit: Time repeated execution of a single statement for more accuracy
    %prun: Run code with the profiler
    %lprun: Run code with the line-by-line profiler
    %memit: Measure the memory use of a single statement
    %mprun: Run code with the line-by-line memory profiler

## Timing Code Snippets: `%timeit` and `%time`
    In [149]: %timeit sum(range(1000))
    24.4 µs ± 12.2 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)

    In [150]: %%timeit
     ...: total = 0
     ...: for i in range(1000):
     ...:     for j in range(1000):
     ...:         total += i * (-1) ** j
     ...: 
    455 ms ± 1.34 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

    In [151]: import random

    In [152]: L = [random.random() for i in range(100000)]
    
    In [153]: %timeit L.sort()
    714 µs ± 30 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

    In [159]: import random

    In [160]: L = [random.random() for i in range(100000)]
    
    In [161]: print("sorting an unsorted list: ")
    sorting an unsorted list:
    
    In [162]: %time L.sort
    CPU times: user 3 µs, sys: 0 ns, total: 3 µs
    Wall time: 5.96 µs
    Out[162]: <function list.sort(*, key=None, reverse=False)>
    
    In [163]: print("sorting an already sorted list:"
    ...: )
    sorting an already sorted list:
    
    In [164]: %time L.sort()
    CPU times: user 19.1 ms, sys: 48 µs, total: 19.2 ms
    Wall time: 19.1 ms

    In [165]: %%time
     ...: s = 0
     ...: for i in range(1000):
     ...:     for j in range(1000):
     ...:         s += i * (-1) ** j
     ...: 
    CPU times: user 339 ms, sys: 856 µs, total: 340 ms
    Wall time: 339 ms
    
    In [166]: s
    Out[166]: 0
    
    In [167]: 

## Profiling Full Scripts: `%prun`
    In [167]: def sum_of_list(N):
     ...:     s = 0
     ...:     for i in range(5):
     ...:         L = [j ^ (j >> i) for j in range(N)]
     ...:         s += sum(L)
     ...:     return s
     ...: 

    In [168]: %prun sum_of_list(1000000)
    14 function calls in 0.588 seconds
    
    Ordered by: internal time
    
    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    5    0.498    0.100    0.498    0.100 <ipython-input-167-3554648dc078>:4(<listcomp>)
    5    0.049    0.010    0.049    0.010 {built-in method builtins.sum}
    1    0.031    0.031    0.578    0.578 <ipython-input-167-3554648dc078>:1(sum_of_list)
    1    0.010    0.010    0.588    0.588 <string>:1(<module>)
    1    0.000    0.000    0.588    0.588 {built-in method builtins.exec}
    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     












    


    

    





    











    




    

    






    
    


    











