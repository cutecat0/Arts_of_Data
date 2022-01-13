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

### `Process V.S Thread`
`1. Master-Worker model`<br>
<b>If use Multiprocessing, main process is Master, other processes are Workers<br>
<b>If use Multithreading, main thread is Master, other threads are Workers<br>
`2. Advantages `<br>
The most advantage of MultiProcessing model is stability : while one subprocess collapse, there's nothing wrong with main process & other subprocesses.
<brr>
While the main process collapse, all the subprocesses must die... <br>
But this the possibility ofn this situation is very rare, cause the main job of the main process(Master) is just, only distribute tasks
while the job of other subprocesses(Worker) are executing tasks<br>

The following comes from : https://www.liaoxuefeng.com/wiki/1016959663602400/1017631469467456<br>
多进程模式的缺点是创建进程的代价大，在Unix/Linux系统下，用fork调用还行，在Windows下创建进程开销巨大。<br>
另外，操作系统能同时运行的进程数也是有限的，在内存和CPU的限制下，如果有几千个进程同时运行，操作系统连调度都会成问题。<br>

多线程模式通常比多进程快一点，但是也快不到哪去，而且，多线程模式致命的缺点就是任何一个线程挂掉都可能直接造成整个进程崩溃，因为所有线程共享进程的内存。<br>
在Windows上，如果一个线程执行的代码出了问题，你经常可以看到这样的提示：“该程序执行了非法操作，即将关闭”，其实往往是某个线程出了问题，但是操作系统会强制结束整个进程。

在Windows下，多线程的效率比多进程要高，所以微软的IIS服务器默认采用多线程模式。<br>
由于多线程存在稳定性的问题，IIS的稳定性就不如Apache。<br>
为了缓解这个问题，IIS和Apache现在又有多进程+多线程的混合模式，真是把问题越搞越复杂"""_****

## **`Thread Exchange`**

##**`计算密集型 vs. IO密集型`**
要最高效地利用CPU，计算密集型任务同时进行的数量应当等于CPU的核心数。<br>
计算密集型任务由于主要消耗CPU资源，因此，代码运行效率至关重要。<br>
Python这样的脚本语言运行效率很低，完全不适合计算密集型任务。对于计算密集型任务，最好用C语言编写。

IO密集型任务执行期间，99%的时间都花在IO上，花在CPU上的时间很少，<br>
因此，用运行速度极快的C语言替换用Python这样运行速度极低的脚本语言，完全无法提升运行效率。<br>
对于IO密集型任务，最合适的语言就是开发效率最高（代码量最少）的语言，脚本语言是首选，C语言最差。

##**`异步IO`**
对应到Python语言，单线程的异步编程模型称为协程



