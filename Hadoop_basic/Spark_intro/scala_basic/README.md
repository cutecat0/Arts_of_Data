reference: https://docs.scala-lang.org/scala3/book/introduction.html<br>
Scala is a beautiful, expressive programming language, with a clean,
 modern syntax, which supports functional programming (FP) 
 and object-oriented programming (OOP), and that provides a safe static type system. 
 
 **The name Scala comes from the word scalable,** 
 and true to that name, the Scala language is used to power busy websites and analyze huge data sets.
 ~~~~It’s a high-level programming language
 It has a concise, readable syntax
 It’s statically-typed (but feels dynamic)
 It has an expressive type system
 It’s a functional programming (FP) language
 It’s an object-oriented programming (OOP) language
 It supports the fusion of FP and OOP
 Contextual abstractions provide a clear way to implement term inference
 It runs on the JVM (and in the browser)
 It interacts seamlessly with Java code
 It’s used for server-side applications (including microservices), big data applications, and can also be used in the browser with Scala.js
~~~~

follow from https://github.com/apache/spark



```spark-shell
``    Using Scala version 2.12.15 (Java HotSpot(TM) 64-Bit Server VM, Java 1.8.0_241)
    Type in expressions to have them evaluated.
    Type :help for more information.
    
    scala> 

`   scala> spark.range(1000 * 1000 * 1000).count()
`   res0: Long = 1000000000                                                         
   
   scala> 


 pyspark
    Using Python version 3.7.4 (v3.7.4:e09359112e, Jul  8 2019 14:54:52)
    Spark context Web UI available at http://192.168.31.12:4040
    Spark context available as 'sc' (master = local[*], app id = local-1641545438342).
    SparkSession available as 'spark'.
    >>> spark.range(1000 * 1000 * 1000).count()
    1000000000
    >>> 
`
end 

Scala 是一门类 Java 的编程语言，它结合了面向对象编程和函数式编程。Scala 是
纯面向对象的，每个值都是一个对象，对象的类型和行为由类定义，不同的类可以通过混
入(mixin)的方式组合在一起。Scala 的设计目的是要和两种主流面向对象编程语言
Java 和 C#实现无缝互操作，这两种主流语言都非纯面向对象。

Scala 也是一门函数式编程语言，每个函数都是一个值，原生支持嵌套函数定义和高
阶函数。Scala 也支持一种通用形式的模式匹配，模式匹配用来操作代数式类型，在很多
函数式语言中都有实现。

Scala 始于 2001 年，由洛桑联邦理工学院(EPFL)的编程方法实验室研发。