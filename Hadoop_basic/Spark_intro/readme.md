Apache Spark: 用于大数据处理的集群计算框架

Spark 并没有以 MapReduce 作为执行引擎，而是使用了 它自己的分布式环境在集群上执行工作

Spark 最突出的表现在于它能将作业于作业之间产生的大规模的工作数据集存储在内存中
【 MapReduce 的数据集始终要从 磁盘 上加载】
above makes Spark 在性能上 超过了 等效的 MapReduce 【高 1 个数量级】

Spark 还是用于构建 分析工具 的出色平台


RDD (Resilient Distributed Dataset, 弹性分布式数据集)
RDD 是 Spark 最核心的 概念
RDD 是集群中 多个机器 分区存储 的一个 只读 对象集合
弹性分布式数据集——弹性： Spark 可以通过重新安排计算 来 自动重建 丢失的分区 

Spark 作业由任意的 多阶段（stages） 有向无环图 （DAG） 构成
其中每个阶段大致相当于 MapReduce 中的 map 阶段 或 reduce 阶段

这些阶段又被 Spark 运行环境 分解为 多个 任务（task）
任务并行运行在 分布于集群中的 RDD 分区上，就像 MapReduce 中的任务一样


RDD 弹性分布式数据集是所有 Spark 程序的核心


