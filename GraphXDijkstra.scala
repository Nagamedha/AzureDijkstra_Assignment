import org.apache.spark.sql.SparkSession
import org.apache.spark.graphx._
import org.apache.spark.rdd.RDD
import sys.process._

object GraphXDijkstra {
  def main(args: Array[String]): Unit = {

    val spark = SparkSession.builder
      .appName("Dijkstra Shortest Path using GraphX")
      .master("local[*]")
      .getOrCreate()

    val sc = spark.sparkContext
    sc.setLogLevel("ERROR")

    println("Spark Initialized Successfully!")

    val inputPath = "weighted_graph.txt"
    val lines = sc.textFile(inputPath)

    val header = lines.first()

    // Undirected edges for both directions
    val edgesRDD: RDD[Edge[Int]] = lines.filter(_ != header).flatMap { line =>
      val fields = line.split(" ")
      Seq(
        Edge(fields(0).toLong, fields(1).toLong, fields(2).toInt),
        Edge(fields(1).toLong, fields(0).toLong, fields(2).toInt)
      )
    }

    val graph = Graph.fromEdges(edgesRDD, Int.MaxValue)

    val nodes = edgesRDD.flatMap(e => Seq(e.srcId, e.dstId)).distinct()
    val sourceId = nodes.min()

    println(s"Selected Source Node is: $sourceId")

    val initialGraph = graph.mapVertices((id, _) => if (id == sourceId) 0 else Int.MaxValue)

    val shortestPaths = initialGraph.pregel(Int.MaxValue)(
      (id, dist, newDist) => math.min(dist, newDist),
      triplet => {
        if (triplet.srcAttr != Int.MaxValue && triplet.srcAttr + triplet.attr < triplet.dstAttr) {
          Iterator((triplet.dstId, triplet.srcAttr + triplet.attr))
        } else {
          Iterator.empty
        }
      },
      (a, b) => math.min(a, b)
    )

    val resultRDD = shortestPaths.vertices.sortByKey().map {
      case (id, dist) => s"Node $id: ${if (dist == Int.MaxValue) "INF" else dist}"
    }

    // Remove old output
    "rm -rf graphx_output".!

    // Save output to single file
    resultRDD.coalesce(1).saveAsTextFile("graphx_output")

    println("Shortest Paths Computed and Saved Successfully!")
    println("Output saved at: graphx_output/part-00000")

    spark.stop()
  }
}
