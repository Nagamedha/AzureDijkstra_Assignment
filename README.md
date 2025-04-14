## `README.md`

```markdown
# Cloud Computing - Programming Assignment: Implementing Dijkstra's Algorithm with Apache Spark on Azure VMs

## Overview
This project demonstrates the implementation of Dijkstra's Shortest Path Algorithm using Apache Spark deployed on Microsoft Azure Virtual Machines (VMs).

The assignment explores both:
- Spark RDD-based solution (PySpark)
- Spark GraphX-based solution (Scala)

---

## Tech Stack Used
- Microsoft Azure Virtual Machine (Ubuntu 20.04)
- Apache Spark 3.4.1 (Standalone Mode)
- Java 8, Scala 2.12
- Python 3.x with PySpark
- Graph Processing using RDD & GraphX
- SSH & SCP for remote access
- Git & GitHub for version control

---

## Folder Structure

Dijkstra_Assignment/
│
├── final_Code.py                  # PySpark RDD based Dijkstra Implementation
├── dijkstra_driver.py            # Python Dijkstra Logic using RDD Output
│
├── GraphXDijkstra.scala          # GraphX based Dijkstra Implementation in Scala
├── GraphXDijkstra.jar            # Compiled Jar for Scala Code
│
├── weighted_graph.txt            # Input Graph (10K Nodes, 100K Edges)
│
├── shortest_paths_output.txt     # Final Output from Python RDD-based Approach
├── graphx_output/                # Final Output from Scala GraphX-based Approach
│
└── README.md                     # This file


### Execution Instructions:

```
### 1. SSH into Azure VM:

```bash
ssh -i /path/to/CloudAssignmentKey.pem azureuser@<VM-Public-IP>
```

### 2. Running PySpark RDD-based Code:

#### Run Spark Job to create edges & adjacency list:
```bash
spark-submit final_Code.py
```

#### Then run Dijkstra logic:
```bash
python3 dijkstra_driver.py
```

Output will be in:
```
shortest_paths_output.txt
```

---

### 3. Running GraphX Scala-based Code:

#### Compile:
```bash
scalac -classpath "$SPARK_HOME/jars/*" GraphXDijkstra.scala
jar -cvf GraphXDijkstra.jar GraphXDijkstra*.class
```

#### Run:
```bash
spark-submit --class GraphXDijkstra --master local[*] --jars "$SPARK_HOME/jars/*" GraphXDijkstra.jar
```

Output will be in:
```
graphx_output/part-00000
```

---

## Output Sample

Python RDD Output:
```
Shortest distances from node 0:
Node 0: 0
Node 1: 12
Node 2: 6
...
```

Scala GraphX Output:
```
Node 0: 0
Node 1: 12
Node 2: 6
...
```

---

## Challenges Faced & Learnings
| Challenge | Solution |
|-----------|-----------|
| Spark errors in VM | Correct configurations & binding IP |
| Data locality issues | Used `.coalesce(1)` to get single output file |
| Python vs Scala output variation | Handled graph as Undirected for consistency |
| PySpark not compatible with GraphX | Used Scala for GraphX implementation |

---

## Proof of Execution on Azure VM
- Azure VM Public IP → `20.94.43.56`
- My local system IP → Verified via `ifconfig` & `curl ifconfig.me`
- Output generated & saved inside Azure VM
- Downloaded outputs via `scp` to local machine

---

## Contact
Prepared by: Nagamedha Sakhamuri  
GitHub Repo: [https://github.com/Nagamedha/AzureDijkstra_Assignment](https://github.com/Nagamedha/AzureDijkstra_Assignment)

---
