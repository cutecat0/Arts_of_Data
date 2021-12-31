from pyspark import SparkContext
import re, sys


def max_temperature():
    sc = SparkContext("local", "Max Temperature")
    sc.textFile(sys.argv[1])\
        .map(lambda s: s.split("\t"))\
        .filter(lambda rec: (rec[1] != "9999" and re.match("[011459]", rec[2])))\
        .map(lambda rec: (int(rec[0]), int(rec[1])))\
        .reduceByKey(max)\
        .saveAsTextFile(sys.argv[2])


if __name__ == '__main__':

    max_temperature()