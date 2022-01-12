all examples from this site: https://www.liaoxuefeng.com/wiki/1016959663602400/1017628290184064

under Unix/Linux, can use fork() call to use multiprocess

cross platform multiprocess, use multiprocessing model

processes communication use Queue, Pipes and so on to work 

Multiprocessing is a complex model which is full of 'dangerous'
Must use lock to make it be alone
at the same time, be careful of 'dead lock'

Python cauz GIL Global Interpreter Lock, can not use multi threads in multi cores

It's just a beautiful dream in Python to make multi thread run in the same time, which means simultaneously


` Even a ThreadLocal variable is global variable, each thread can only read the copy of it's own thread
without boring each other`

