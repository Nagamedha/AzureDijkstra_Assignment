from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("Dijkstra Shortest Path").setMaster("local[*]")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext.getOrCreate(conf=conf)
sc.setLogLevel("ERROR")

print("Spark Initialized Successfully!")

file_path = "weighted_graph.txt"
lines = sc.textFile(file_path)

header = lines.first()
edges = lines.filter(lambda line: line != header).map(lambda line: tuple(map(int, line.strip().split())))

nodes = edges.flatMap(lambda x: [x[0], x[1]]).distinct()
source = nodes.min()

print("Selected Source Node is:", source)

adjacency_list_rdd = edges.flatMap(lambda x: [(x[0], (x[1], x[2])), (x[1], (x[0], x[2]))]).groupByKey().mapValues(list)

adjacency_list_rdd.persist()

edges.saveAsTextFile("edges_output")
adjacency_list_rdd.saveAsTextFile("adjacency_list_output")

print("Edges and Adjacency List written successfully to output folders!")
print("Check edges_output/ and adjacency_list_output/ folders")

import shutil
import os

if os.path.exists("edges_output"):
    shutil.rmtree("edges_output")

if os.path.exists("adjacency_list_output"):
    shutil.rmtree("adjacency_list_output")

edges.saveAsTextFile("edges_output")
adjacency_list_rdd.saveAsTextFile("adjacency_list_output")
