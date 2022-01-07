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

above from https://github.com/apache/spark

`spark-shell
    Using Scala version 2.12.15 (Java HotSpot(TM) 64-Bit Server VM, Java 1.8.0_241)
    Type in expressions to have them evaluated.
    Type :help for more information.
    
    scala> 

` `scala> spark.range(1000 * 1000 * 1000).count()
   res0: Long = 1000000000                                                         
   
   scala> 
`

` pyspark
    Using Python version 3.7.4 (v3.7.4:e09359112e, Jul  8 2019 14:54:52)
    Spark context Web UI available at http://192.168.31.12:4040
    Spark context available as 'sc' (master = local[*], app id = local-1641545438342).
    SparkSession available as 'spark'.
    >>> spark.range(1000 * 1000 * 1000).count()
    1000000000
>>> 


`