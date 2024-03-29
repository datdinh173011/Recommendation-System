from pyspark import SparkContext
from operator import add
from pyspark import SparkContext

sc = SparkContext("local", "Hello World App")
# parallelize is used to create an RDD from a list collection
data = sc.parallelize(list("Hello World"))

counts = data.map(lambda x: 
	(x, 1)).reduceByKey(add).sortBy(lambda x: x[1],
	 ascending=False).collect()

for (word, count) in counts:
    print("{}: {}".format(word, count))