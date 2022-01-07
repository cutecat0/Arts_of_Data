All above comes from this book:
_Hadoop: The Definitvie Guide_

Part I Hadoop基础芝士
	数据存储和分析的分布式系统
		Hadoop 是 Apache Lucene 创始人 Doug Cutting 创建的
			Hadoop 起源于开源网络搜索引擎 Apache Nutch 
	 MapReduce
		MapReduce 
			基本 是一个批处理系统，不适合交互式分析
			MapReduce 适合那些不需要用户在现场等待查询结果的离线使用场景
			MapReduce 适合一次写入，多次读取数据的应用（关系型数据库则更适合持续更新的数据集）
		Hadoop Streaming
			Hadoop提供了MapReduce的API， 可以非Java语言的其它语言来写自己的map和reduce函数
			Python 版 map 和 reduce 函数
			code
	Hadoop 的分布式问价系统
HDFS （Hadoop Distributed File System）
		HDFS 的设计
			HDFS 以流式数据访问模式来存储超大文件
				流式数据访问
					一次写入、多次读取
			HDFS 运行于商用硬件集群上
				商用硬件
			不适合在 HDFS 上运行的应用
				低时间延迟的数据访问
				大量的小文件
				多用户写入，任意修改文件
		HDFS 的概念
			数据块
				每个磁盘都有默认的数据块大小
					磁盘进行读/写的最小单位
				HDFS 默认数据块大小为 128MB
					每个块block也被划分为块大小的多个分块chunk
						BUT, 当一个块128MB的block中，有一个分块chunk只有1MB时， 它只占据1MB的磁盘大小，并不是128MB的块大小
				WHY  HDFS 中的块这么大呢？？？
					HDFS 的块比磁盘的块大， 主要目的是最小化寻址开销
				HDFS 块抽象的好处
					1. 一个文件的大小可以大于网络中任意一个磁盘的容量
						文件的所有块并不需要存储在同一个磁盘上
							它们可以利用集群上任意一个次磁盘进行存储
					2. 使用抽象块而非整个文件作为存储单元， 大大简化了存储子系统的设计
						简化存储管理
							由于每个块大小是固定的，所以可以很方便的计算出一个集群可以存储多少个块
					3. 块非常适用于数据备份进而提供数据容错能力和提高可用性
				显示块信息命令
					hdfs fsck / -files -blocks
			namenode 
datanode
				HDFS有两类节点以管理节点-工作节点模式运行
				一个namenode（管理节点）
					管理文件系统的命名空间
					维护文件系统树及整棵树内所有的文件和目录
				多个datanode（工作节点）
					记录着每个文件中各个块所在的数据节点信息
					并不永久保存块的位置信息
					根据需要存储并检索数据块
					并且定期向namenode发送它们所存储的块的列表
				客户端
					client代表用户通过与namenode和datanode交互来访问整个文件系统
				对namenode实现容错非常重要
					Hadoop 为此提供两种机制
						备份那些组成文件系统元数据持久状态的文件
							将持久状态写入本地磁盘的同时、写入一个远程挂载的网络文件系统NFS
						运行一个辅助namenode， 但不能被用作namenode
							这个辅助namenode的重要作用是定期合并编辑日志与命名镜像， 以防止编辑日志过大
			块缓存
				通常datanode从磁盘中读取块
				But对于频繁访问的文件，起对应的块可能被显示的缓存在datanode的内存中——以堆外块缓存（off-heap block cache）的形式存在
					默认情况下，一个块仅缓存在一个datanode内存中
			联邦HDFS
				内存会是限制文件系统横向扩展的瓶颈
					因为namenode在内存中保存文件系统中每个文件和数据块的引用关系
				联邦HDFS允许系统通过添加namenode实现扩展
					其中每个namenode管理文件系统命名空间中的一部分
						e.g.
							一个namenode可能管理/usr目录下面的所有文件
							而另外一个namenode可能管理/share目录下的所有文件
			HDFS 的高可用性（HA）
				配置了一对活动-备用（active-standby）namenode
					当活动namenode失效、备用namenode会接管它的任务并服务来自于客户端的请求，不会有任何明显的中断
				故障切换与规避
					故障转移控制器
						默认的一种是使用ZooKeeper来确保有且仅有一个活动namenode
					规避
						高可用实现做了更近一步的优化、以确保先前活动的namenode不会执行危害系统并导致系统崩溃的操作
		命令行接口
			文件系统的基本操作
				hadoop fs -help
				自己常用基本命令
					查看 
						hdfs dfs -ls /hive/warehouse/hcdn.db/corejob/coredayuvv2/dt=2021-11-25
					复制
						从本地文件系统将一个文件复制到HDFS
							hdfs dfs -cooyFromLocal local.txt /hdfslocation hdfslocation.txt
							hadoop fs -copyFromLocal
						从HDFS复制一个文件到本地
							hdfs dfs -copyToLocal 
								e.g
							hadoop fs -copyToLocal
					新建文件
						hadoop fs -mkdir books 
							hdfs dfs -mkdir books
						hadoop fs -ls
							hdfs dfs -ls 
					列出本地文件系统根目录下的文件
						hadoop fs -ls file:///
				HDFS 中的文件访问权限
					r 只读
					w 写入
					x 可执行
		Hadoop  文件系统
			Hadoop有一个抽象的文件系统概念， HDFS 只是其中的一个实现
				HDFS
					Hadoop 的分布式文件系统。将HDFS设计成与MapReduce结合使用，可以实现高性能
				FTP
					由FTP服务器支持的文件系统
				S3
					s3a 由Amazon S3支持的文件系统
				Azure 
					由Microsoft Azure 支持的文件系统 
				Swift
					由OpenStack Swift 支持的文件系统 
			接口
				Hadoop 是由 Java 写的
					通过Java API 可以调用大部分Hadoop文件系统的交互操作
				HTTP
					由WebHDFS 提供的 HTTP REST API 使得其它非Java语言开发的应用可以方便的同HDFS进行交互
						直接访问
						通过代理
				C 语言
					Hadoop 提供了一个名为 libhdfs 的C语言库
						该语言库是Java FileSystem 接口的一个镜像
						使用 Java 原生接口 JNI 调用 Java 文件系统客户端
				NFS
					使用Hadoop 的 HFSv3 网管将HDFS 挂载为本地客户端文件系统
				FUSE 
					用户空间文件系统（Filesystem in Userspace）
						将用户空间实现的文件系统作为Unix文件系统进行集成
							通过使用Hadoop的Fuse-DFS 模块（C语言实现）
		Java 接口
		数据流
		distcp复制
			distcp 替代 hadoop fs -cp 
			hadoop distcp file1 file2
			hadoop distcp dir1 dir2
			hadoop distcp update dir1 dir2 
			保持HDFS的均衡
				当文件块在集群中均匀分布时， HDFS能达到最佳工作状态
				so, 要确保distcp 不会破坏上述均衡
	YARN（Yet Another Resource Negotiator）
		简介
			YARN是一个集群资源管理系统
				允许任何一个分布式程序（not only MapReduce）基于Hadoop集群的数据而运行
				为了改善MapReduce的实现
			一些分布式计算框架（MapReduce、SPark）作为 YARN 应用，运行在集群计算层（YARN） 和集群存储层（HDFS和HBase）之上
		YARN 应用运行机制
			YARN 通过两类长期运行的守护进程提供自己的核心服务
				资源管理器
				节点管理器
			资源请求
				本地化
			应用生命期
				一个用户作业对应一个应用
				作业的每个工作流/每个用户对话对应一个应用
				多个用户共享一个长期运行的应用
			构建YARN应用
		YARN V.S. MapReduce
			YARN的很多设计是为了解决MapReduce 1 的局限性
			YARN 的好处
				可扩展性（Scalability）
					YARN 可以在更大规模集群上运行
				可用性（Availability）
					获得高可用性（HA High Availability）
				利用率（Utilizatone）
					一个节点管理器管理一个资源池
					而不是指定的固定数目的slot
				多租户（Multitenancy）
					YARN的最大优点在于向MapReduce以外的其它类型的分布式应用开放了Hadoop
					MapReduce仅仅是许多YARN应用中的一个
		YARN 中的调度
			调度选项
				FIFO调度器（FIFO Schedular）
					不适合共享集群
				容量调度器（Capacity Schedular）
					以整个集群的利用率为代价
				公平调度器（Fair Schedular）
					动态平衡资源
			容量调度器配置
				允许多个组织共享一个Hadoop集群
			公平调度器配置
				为所有运行的应用公平分配资源
			延迟调度
				所有YARN调度器都试图以本地请求为重
			主导资源公平性
	Hadoop的I/O操作
		简介
		数据完整性
			HDFS的数据完整性
				HDFS 会对写入的所有数据计算校验和
				并在读取数据时验证校验和
			LocalFIleSystem
				Hadoop 的 LocalFileSystem在
			ChecksumFileSystem
		压缩
			文件压缩2大好处
				减少存储文件所需的磁盘空间
				加速数据在网络和磁盘上的传输
			codec
				说明
					codec是压缩-解压算法的一种实现
				原生类库
					为了提高性能，最好使用原生类库来实现压缩和解压缩
			压缩和输入分片
				在考虑如何压缩将由 MapReduce 处理的数据时， 理解这些压缩格式是否支持切分（splitting）是非常重要的！！！
			在MapReduce中使用压缩
		序列化
			Writable接口
			Writable类
			实现定制的Writable集合
			序列化框架
		基于文件的数据结构
			关于SequenceFile
			其它文件格式和面向列的格式
	网格计算
		HPC
			（High Performance Computing， HPC）
				将作业分散到集群的各台机器上
		Grid Computing
		MPI
			（Message Passing Interface， MPI）
				消息传递接口
		无共享
			（sharing-nothing）框架
				MapReduce的分布式处理框架，意味着各个任务之间是彼此独立的
	Spark
		简介（大数据处理框架）
			Apache Spark 是一个围绕速度、易用性和复杂分析构建的大数据处理框架
			最初在2009年由加州大学伯克利分校的AMPLab开发，并于2010年成为Apache的开源项目之一。

Part II 关于MapReduce
	MapReduce应用开发
		关于配置的API
		关于Apache Oozie
			Apache Oozie 是一个运行工作流的系统
			该工作流由相互依赖的作业组成
			Oozie由2部分组成
				工作流引擎
					负责存储和运行由不同类型的Hadoop作业（MapReduce、Hive、Pig）等组成的工作流
				cooradiator 引擎
					负责基于预定义的调度策略及数据可用性运行工作流作业
	MapReduce的工作机制
	MapReduce的类型与格式
		map: (K1, V1) -> list(K2, V2) 
		reduce: (K2, list(V2) -> list(K3, V3)
	MapReduce的特性
		计数器
			内置计数器
				任务计数器
				文件系统计数器
				作业计数器
		排序
		连接
		边数据分布
			边数据（side data）
			作业所需的额外的只读数据
			以辅助处理主数据集
		MapReduce库类

Part III Hadoop的操作
	构建Hadoop集群
		环境设置
			默认下，Hadoop 为每个守护进程分配1GB内存
		委托令牌
			由服务器创建
	管理Hadoop

Part IV Hadoop相关开源项目
	关于Avro
		Apache Avro 是一个独立于编程语言的数据序列化系统
		Python API
	关于Parquet
		简介
			Apache Parquet 是一种能够有效存储嵌套数据的列式存储格式
			列式存储下，同一列的数据连续保存
				这一做法可以允许更高效的编码方式
				使列式存储格式的文件，比行式存储格式的同等文件，占用更少空间
				查询引擎能够跳过对本次查询无用的行，从而提高了查询性能
			parquet的突出贡献
				能够以真正的列式存储格式来保存具有深度嵌套结构的数据
				parquet脱胎于Google发表的一篇关于Dremel的论文
					以扁平的列式存储格式&很小的额外开销来存储嵌套的结构
					above，带来性能上的提升
			有很多工具都支持这种格式
		数据模型
			原子数据类型
			使用面向列式的存储格式时， 同一列数据连续存储
			parquet使用Dremel编码方法
				模式中的每个原子类型的字段都单独存储为一列
				且每个值都要通过使用2个整数来对其结构进行编码
					这两个整数分别是列定义深度（definition level）
					列元素重复次数（repetition level）
					这种编码的好处
						对任意一列（即使是嵌套列）数据的读取都不需要涉及到其它列
		Parquet文件格式
			parquet文件由一个文件头（header）
				文件头中仅包含一个称为PAR1的4字节数字（Magic Number）
				用来识别整个Parquet文件格式
			一个或多个紧随其后的文件块（block）
			以及一个用于结尾的文件尾（footer）构成
				文件的所有元数据都被保存在文件尾中
				文件尾中的元数据包括文件格式的版本信息、模式信息、额外的键值对、所有块的元数据信息
				文件尾的最后2个字段分别是
					一个4字节字段（其中包含了文件尾中元数据长度的编码）
					和一个PAR1（与文件头中的相同）
			由于读取文件尾可以定位文件块， 一次Parquet文件是可分割&可并行处理的（例如通过MapReduce处理）
			Parquet的默认设置不使用任何压缩算法，但可以支持Snappy、gzip、LZO等压缩工具
		parquet的配置
			Parquet文件的属性在写操作时设置
			在设置文件块儿的大小时， 需折衷考虑扫描效率与内存的使用
				每个文件块在读/写操作时都需要缓存在内存中，这个限制使得问价块儿不能太大
				默认文件块儿大小为128MB
			Parquet文件块儿的大小不能超过其HDFS块大小
				只有这样才能使得每个Parquet文件块仅需读一个HDFS块（因而也只需要从一个数据结点上读）
				比较常见的做法是为这两个属性设置相同的值
					事实上，它们的默认值都是128MB
			页是Parquet文件的最小存储单元
				默认情况下，页的大小为1MB
		parquet文件的读写
			大多数情况下，使用高级工具处理Parquet文件的读/写操作（e.g. Pig， Hive， Impala）
			有些时候也需要低级的顺序访问
				Parquet具有一个可插入式的内存数据模型
					让Parquet文件格式更好的与类型广泛的各种工具和组建集成
			Avro、Protocol Buffers、Thrift
				框架定义数据模型
			投影模式&读取模式
				有时只是想读取文件中的少数几列
				这正是像Parquet这样的列式存储格式存在的真正原因
					提升I/O操作的效率
					节省时间
				投影模式必须是Parquet文件在写操作时所使用的一个子集，因而文法通过增加新的字段来对模式进行扩展
				这2种模式的用途不同&可同时使用
					投影模式：过滤想要从Parquet文件中读取的列
						痛殴Avro模式来表示
					读取模式：仅用于解析Avro记录
		parquet MapReduce
			MapReduce的输入/输出格式中有一部分是用于通过MapReduce作业来读/写Parquet文件Parquet格式
	关于Flume
		简介
			设计Flume的宗旨就是向Hadoop批量导入基于事件的海量数据
			source-channel-sink
				使用Flume，需运行Flume代理
Flume代理是由持续运行的source
-sink-channel构成的Java进程
					source（数据来源）
					sink（数据目标）
					channel（用于连接source和sink）
				Flume的source产生事件、并将其传递给channel，channel存储这些事件直至转发给sink
					source-channle-sink 可视为Flume基本构件
		HDFS sink
			分区&拦截器
				大型数据集常常被组织为分区（partition）
					好处：
						如果查询仅设计到数据的某个子集
查询过程就可以被限制在特定的分区范围内
					一个事件被决定写入哪个分区是由header中的timestamp来决定的
						默认情况下，事件header中没有timestamp
						但是可以通过Flume拦截器（interceptor）来添加
				拦截器（interceptor）是一种能够对事件流中的事件进行修改修改或删除的组件
					interceptor连接source并在事件被传递到channel之前对事件进行处理
		扇出
			简介
				术语扇出（fan out）指的是从一个source向多个channel、亦即向多个sink传递事件
	关于Sqoop
		Apache Sqoop是一个开源工具，允许用户将数据从结构化存储器抽取到Hadoop中，用于进一步的处理
	关于Pig
		Apache Pig为大型数据集的处理提供了更高层次的抽象
		Pig包括2部分
			用于描述数据流的语言，称为 Pig Latin
				Pig Latin 程序由一系列“操作”（operation） 或“变换”（transformation）组成
			用于允许Pig Latin程序的执行环境
				当前有2个环境
					单JVM中的本地执行环境
					Hadoop集群上的分布式执行环境
		Pig 是一种探索大规模数据集的脚本语言
			Pig的诱人之处在于仅用控制台上的五六行 Pig Latin 代码就能够处理TB级的数据
		安装与运行Pig
			执行类型
				Pig有两种执行类型或称为模式（mode）
					本地模式（local mode）
					MapReduce 模式（MapReduce mode）
			运行Pig程序
				脚本
				Grunt
					Grunt是运行Pig命令的交互式shell环境
				嵌入式方法
			与数据库进行比较
				最显著的不同
					Pig Latin 是一种数据流编程语言
					SQL 是一种声明式编程语言
				Pig 对复杂的嵌套数据结构的支持、SQL只能处理平面数据类型
		Pig Latin
			结构
				e.g.
					grouped_records = GROUP records BY year;
			语句
				Pig的物理计划是一系列的MapReduce作业
				在本地模式下，这些作业在本地JVM中运行
				而在MapReduce模式下，它们在Hadoop集群上运行
			类型
			模式
			函数
			宏
		用户自定义函数
		数据处理操作
		Pig实战
			并行处理
	关于Hive
		简介
			Apache Hive是一个构建在Hadoop上的数据仓库框架
Facebook， Jeff团队，是应Facebook每天产生海量新兴社会网络数据进行管理和（机器）学习的需求而产生和发展的
				Jeff Hammerbacher
			Hive的设计目的是让精通SQL技能但Java编程技能相对较弱的分析师能够对Facebook存放在HDFS中的大规模数据集执行查询
		安装Hive
			Hive一般在工作站上运行，它把SQL查询转换为一系列在Hadoop集群上运行的作业
			Hive把数据组织为表， 通过这种方式为存储在HDFS上的数据赋予结构
			元数据（如表模式）存储在metastore数据库中
		e.g.
			HiveQL 
				HiveQL 是 Hive的查询语言，相当于SQL的一种“方言”
					e.g
				hive -e 
					在行内嵌入命令， 此时不需要表示结束的分号；
				hive -S 
					whatever交互or非交互，Hive都会把操作运行时的信息打印输出到标准输出
					可以用 -S 强制不输出这些信息
					hive -S -e 'select ...' > 'output.txt'
				hive ！ 
					使用！ 前缀来运行宿主操作系统的命令
				hive dfs 
					使用 dfs 命令来访问 Hadoop 文件系统
				create hive table
					e.g.
				ROW FORMAT 
					ROW FORMAT SERDE
						HiveQL特有
此子句所声明的是数据文件的每一行是由制表符分隔的文本
		运行Hive
			配置Hive
				执行引擎
					原始（默认）为MapReduce
					Apache Tez
					Spark
			Hive服务
				hive --service help
					cli Hive的命令行接口（shell环境），默认服务
					hiveserver2: 让Hive以提供Thrift服务的服务器形式运行
					beeline： 以嵌入方式工作的Hive命令行接口
					hwi: Hive的Web接口
						Hue是一个功能更全面的Hadoop Web 接口
					jar: 与Hadoop jar等价
					metastore： 默认情况下，metastore和Hive服务运行在同一个进程里
				Hive客户端
					Thrift 客户端
					JDBC 驱动
			Metastore
				metastore是Hive元数据的集中存放地
				metastore包括2部分
					&后台数据的存储
					默认情况下，metastore服务和Hive服务运行在同一个JVM中
					它包含一个内嵌的以本地磁盘作为存储的Derby数据库实例
				if要支持多会话（&多用户），需要使用一个独立的数据库
					这种配置称为本地metastore配置（local metastore）
				远程metastore配置（remote metastore）
					一个或多个metastore服务器和Hive服务器在不同的进程内
		Hive与传统数据库相比
			读时模式 vs. 写时模式
				写时模式（schema on write）
					传统数据库，表的模式时在数据加载时强制确定的
					如果在加载时发现数据不符合模式，则拒绝加载数据
					因为数据是在写入数据库时对照模式进行检查
					因此这一设计有时被称之为“写时模式”
				读时模式（schema on read）
					Hive对数据的验证并不在加载数据时进行
					而是在查询时进行
					这称为“读时模式”
			更新、事务&索引
				更新、事务&索引都是传统数据库最重要的特性
				Hive也还没有考虑支持这些特性—
					因为Hive被设计为用MapReduce操作HDFS数据
					在这样的环境下，“全表扫描（full-table scan）是常态操作
					而表更新则是通过把数据变换后放入新表实现的
				Hive的索引分为2类
					紧凑（compact）索引
						存储每个HDFS的块号
						因此存储不会占用过多的磁盘空间
					位图（bitmap）索引
						使用压缩的位集合（bitset）来高效存储具有某个特殊值的行
						一般适合于具有较少取值可能（low-cardinality）的列（如性别/国别）
			其它SQL-on-Hadoop技术
				Cloudera Impala
					开源交互式SQL引擎
					Impala在性能上要比基于MapReduce的Hive高一个数量级
					Impala使用专用的守护进程，这些守护进程运行在集群中的每个数据节点上
					Impala使用Hive的metastore并支持Hive格式和绝大多数的HiveQL结构
						因此在实际操作中这2个系统可以直观地相互移植
						或者运行在同一个集群上
				Facebook Presto
				Apache Drill
				Spark SQL 
					Spark SQL 与在Hive中使用Spark执行引擎并不是一回事
					基于Spark的Hive能够提供Hive的所有功能，因为它本身隶属于Hive项目
					另一方面，Spark SQL则是一种新兴的SQL引擎，它只是某种程度上提供与Hive的兼容
				Apache Phoenix
					采取了另一种完全不同的方式
						提供基于HBase的SQL
						通过JDBC驱动实现SQL访问
						JDBC驱动将查询转换为HBase扫描，并利用HBase协同处理器来执行服务器端的聚合
						另外，其元数据也存储在HBase中
		HiveQL
			Hive的SQL“方言”称为HiveQL
			数据类型
				Hive支持原子和复杂数据类型
					原子数据类型
						数值型、布尔型、字符串型、时间戳型
					复杂数据类型
						数组、映射、结构
			操作与函数
				e.g.
					hive>show functions;
		表
			在逻辑上由存储的数据和描述表中数据形式的相关元数据组成
				数据一般存放在HDFS中，but也可以放在其它任何Hadoop文件系统中呢
					包括本地系统或S3
				Hive把元数据存放在关系型数据库中，！！！NOT put in HDFS中
			托管表和外部表
				在Hive中创建表时， 默认情况下Hive负责管理数据， which means Hive 把数据移入它的 “仓库目录”（warehouse directory）
				Another choice is 创建一个外部表（external table）， which makes Hive 到仓库目录以外的位置访问数据
				托管表（managed table）
					drop table managed_table; 会删除元数据和数据——数据会彻底消失
						CREATE TABLE managed_table(dummy STRING);
LOAD DATA INPATH '/usr/gwendolyhai/data.txt' INTO table managed_table;
						把文件hdfs://usr/gwendolynhai/data.txt 移动到 Hive 的 managed_table 表的仓库目录中， 即 hdfs://usr/hive/warehouse/managed_table
					因为最初的LOAD是一个移动操作，DROP是一个删除操作
				外部表（external table）
					由你来控制数据的创建和删除
						CREATE EXTERNAL TABLE external_table(dummy STRING)
LOCATION '/usr/gwendolynhai/external_table';
LOAD DATA INPATH 'usr/gwendolynhai/data.txt' INTO TABLE external_table;
						使用EXTERNAL关键字以后，Hive知道数据并不由自己管理， 因此不会把数据移到自己的仓库目录
						事实上， 在定义时， 它甚至都不会去检查这一外部位置是否存在
							which is really a wonderful character
							cauz which means U CAN 把创建数据推迟到创建表之后才进行
					外部数据的位置需要在创建表的时候就指明！！！
					丢弃外部表时， Hive 不会碰数据，而只会删除元数据
				如何选择使用哪种表呢？
					多数情况下，managed 和 external table没有太大区别（of course DROP 语义除外）
					经验法则
						如果所有处理都由Hive完成， 应该使用托管表
						如果要用Hive和其它工具来处理同一个数据，应该使用外部表
					普遍用法
						把存放在HDFS（由其它进程创建）的初始数据集用作外部表使用
						然后用Hive的变换功能把数据移到托管的Hive表
						above way 反之也可
						外部表（未必在HDFS中）可以用于从Hive导出数据供其它应用程序使用
					需要使用外部表的另一个原因是： 你想为同一个数据集关联不同的模式
			分区和桶
				Hive 把表组织成分区（partition）
					这是一种根据分区列（partition column， 如日期）的值对表进行粗略划分的机制
					使用分区可以加快数据分片（slice）的查询速度
				表或分区可以进一步分为桶（bucket）
					它会为数据提供额外的结构以获得更高效的查询处理
					例如，通过根据用户ID来划分桶、可以在所有用户集合的随机样本上快速计算基于用户 的查询
				分区（partition）
					一个表可以有多个维度的分区
						子分区（sub partition）
					PARTITIONED BY (
  `dt` STRING)

						分区是在建表时通过 partitioned by  子句定义的
						e.g.
					把数据加载到分区表时， 要显式指定分区值
						e.g.
					在文件系统级别，分区只是表目录下嵌套的子目录。
					可以使用hive>show partitions 让Hive告诉我们表中有哪些分区
						e.g.
						切记： partitioned by 子句中的列定义是表中正式的列，称为 分区列（partition column）
						BUT， 数据文件中并不包含这些列的值， 因为它们源于目录名
				桶（bucket）
					把表（或分区）组织成桶
has 2 reasons
						获得更高的查询处理效率
						使 取样 或者 采样（sampling）更高效
					如何告诉 Hive 一个表应该被划分成桶
						使用 clustered by  来指定划分桶所用的列和要划分的桶的个数
						create table bucked_users (id INT, name STRING)
clustered by (id) into  buckets;
							使用用户ID来确定如何划分桶
							Hive对值进行哈希并将结果除以桶的个数取余数
							这样任何一桶里都会有一个随机的用户集合
						每个桶的连接为高效的归并排序（merge-sort）
							create table bucketed_users (id INT, name STRING)
clustered by (id) sorted by (id asc) into 4 buckets;
							上述语句声明一个表使其使用桶排序
			存储格式
				Hive 从2个维度对表的存储进行管理
					行格式（row format）
						行和一行中的字段如何存储
						SerDe 序列化和反序列化工具（Serialiser-Deserializer）
					文件格式（file format）
						一行中字段容器的格式
						最简单的格式是纯文本文件
						也可以使用面向行的和面向列的二进制格式
				默认存储格式： 分隔的文本
					如果在创建时没有用ROW FORMAT 或 STORED AS 子句， 那么 Hive 所使用的默认格式时分隔的文本， 每行（line） 存储一个数据行（row）
			导入数据
				insert 语句
					insert overwrite table target
select col1, col2
from source;
					分区表使用partition
指明数据要插入哪个分区
						insert overwrite table target
partition (dt='2021-12-07')
select col1, col2
from source;
					动态分区插入
使用分区值来指明分区
						insert overwrite table target
partition (dt)
select col1, col2
from source;
				多表插入
					from source
insert overwrite table target
select col1, col2
					在同一个查询中使用多个insert子句
这种多表插入（multiable insert）方法比使用多个单独的insert语句效率更高
					只需扫描一遍源表就可以生成多个 不相交的输出
					e.g.
						from records
insert overwrite table stations_by_year
select year, count(distinct station)
group by year
insert overwrite table records_by_year
select year, count(1)
group by year
insert overwrite table good_records_by_year
select year, count(1)
where temperature != 9999 and quality in (0, 1, 4, 5, 9)
group by year
							这里只有一个源表，但有三个
表用于存放针对这个源表的三个不同查询
所产生的结果
				create table... as select 语句
					把Hive查询的输出结果存放到一个新的表
					新表的列的定义是从select子句所检索的列导出的
					create table target
as
select col1, col2
from source;
			子主题 8
			表的修改
				由于Hive使用读时模式（schema on read）
so after create table， 它可以非常灵活的支持对表定义的修改
				alter table source rename to target;
				alter table target add columns (col3 STRING）；
			表的丢弃
				drop table 语句用于删除表的数据和元数据
				如果是外部表， 就只删除元数据， 数据不会受到影响
				如果要删除表内的所有数据，BUT保留表的定义
					truncate table 
					truncate table my_table;
					此方法对外部表不起作用，这种情况需要在Hive的shell环境中使用 dfs -rmr 命令直接删除外部表目录 
					anther way 达到类似目的的方法
使用 like 创建一个于第一个表模式相同的表
						create table new_table like existing_table;
		查询数据
			排序和聚集
				控制某个特定行应该到哪个reducer
其目的是为了进行后续的聚集操作
					distribute by 子句
					from record2
select year, temperature
distribute by year
sort by year ASC, temperature DESC;
					可以使用Hive的非标准的扩展 sort by 为每个 reducer 产生一个排序文件
				if sort by and distribute by 中所使用的列相同，可以缩写为 cluster by 以便同时指定2者所用的列
			MapReduce 脚本
				和 Hadoop Streaming 类似， transform、map、reduce 子句可以在 Hive 中调用外部脚本或程序
				用一个脚本过滤不符合某条件的行
					e.g. code 
				code e.g. 
			连接
				内连接
					# inner join
select table_A.*, table_B.*
from table_A JOIN table_B on (table_A.id = table_B.id);
					Hive 只支持等值连接（equijoin）
						which means 在连接谓词中只能使用等号=
					可以在on条件添加and组成多个条件
					# use where
select table_A.*, table_B.*
from table_A, table_B
where table_A.id = table_B.id;
					explan
select sales.*, things.*
from sales join things on (sales.id = things.id);
						使用 explan 关键字查看 Hive 将为某个查询使用
多少个 MapReduce 作业
				外连接
					left outer join
						
# left outer join
# 左边列都在，右边不匹配的直接为null
select sales.*, things.*
from sales left outer join things on (sales.id = things.id);

					right outer join
						# right outer join
# 右边列都匹配，左边不匹配的直接为null
select sales.*, things.*
from sales right outer join things on (sales.id = things.id);

					full outer join
						# full outer join
# 左右两边所有的都保留
select sales.*, things.*
from sales full outer join things on (sales.id = things.id);

				半连接
					left semi join 
						# left semi join
# 半连接
select *
from things
where things.id in (select id from sales);

						#above equels to below
select * from things left semi join sales on (sales.id = things.id)

						# use left semi join ... on 's limit:
# 右表只能在on子句出现（不能在select表达式中引用右表）

				map 连接
					如果有一个连接表小到足以放入内存，Hive就可以把较小的表放入每个mapper的内存来执行连接操作——and this way called 【map 连接】
					SET hive.optimize.bucketmapjoin=true;
			子查询
				子主题 1
			视图
		用户定义函数
			写UDF
			写UDAF
	关于Crunch
	关于Spark
	关于HBase
	关于ZooKeeper

Part V 案例学习
	医疗公司塞纳（Cerner）的可聚合数据
	生物数据科学：用软件拯救生命
	开源项目Cascading
