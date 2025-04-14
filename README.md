##  README.md

```markdown
# Cloud Computing - Programming Assignment: Implementing Dijkstra's Algorithm with Apache Spark on Azure VMs

## Overview
This project demonstrates the implementation of Dijkstra's Shortest Path Algorithm using Apache Spark, deployed and executed on Microsoft Azure Virtual Machines (VMs).

The solution includes:
- PySpark RDD-based Implementation
- Scala GraphX-based Implementation

---

## Tech Stack Used
- Microsoft Azure Virtual Machine (Ubuntu)
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
├── final_Code.py                  # PySpark RDD-based Dijkstra Implementation
├── dijkstra_driver.py            # Python logic to run Dijkstra on generated RDD outputs
│
├── GraphXDijkstra.scala          # GraphX-based Dijkstra Implementation in Scala
├── GraphXDijkstra.jar            # Compiled Jar for Scala GraphX code
│
├── weighted_graph.txt            # Input Graph (10K Nodes, 100K Edges)
│
├── shortest_paths_output.txt     # Final Output from PySpark
├── graphx_output/                # Output from GraphX Approach
│
└── README.md                     # This file


---

## Execution Instructions (Step-by-step)

```
### 1. SSH into Azure VM

> NOTE:
> - Use your own `.pem` key file that was generated while creating your Azure VM.
> - The key name can be anything like `CloudAssignmentKey.pem` or any other name based on your VM setup.
> - Replace `<Your-VM-Public-IP>` with your own VM's Public IP.

```bash
ssh -i /path/to/Your-Key-File.pem azureuser@<Your-VM-Public-IP>
```
---

### 2. Running PySpark RDD-based Implementation

#### Step 1: Generate Edges & Adjacency List using Spark
```bash
spark-submit final_Code.py
```

#### Step 2: Run Dijkstra Logic
```bash
python3 dijkstra_driver.py
```

#### Output Generated At:
```
shortest_paths_output.txt
```

---

### 3. Running Scala GraphX-based Implementation

#### Step 1: Compile Scala Code
```bash
scalac -classpath "$SPARK_HOME/jars/*" GraphXDijkstra.scala
jar -cvf GraphXDijkstra.jar GraphXDijkstra*.class
```

#### Step 2: Execute GraphX Job using Spark
```bash
spark-submit --class GraphXDijkstra --master local[*] --jars "$SPARK_HOME/jars/*" GraphXDijkstra.jar
```

#### Output Generated At:
```
graphx_output/part-00000
```

---

## How to Prove Execution Happened on Azure VM?

- Show your SSH connection:
    ```bash
    ssh -i /path/to/Your-Key.pem azureuser@<Your-VM-Public-IP>
    ```

- Inside VM, show execution commands & outputs generated:
    ```bash
    ls
    cat shortest_paths_output.txt
    cat graphx_output/part-00000
    ```

- Additionally, you can verify that your local machine's public IP is different from Azure VM's IP:
    ```bash
    curl ifconfig.me   # On Local Machine
    curl ifconfig.me   # Inside Azure VM
    ```

---

## Challenges Faced & Learnings
| Challenge | Solution |
|-----------|-----------|
| Spark initialization & binding issues | Fixed using Spark conf bindAddress |
| Data not writing in single output file | Used `.coalesce(1)` in GraphX for single output |
| PySpark not supporting GraphX | Used Scala GraphX for large-scale Graph Processing |
| Different .pem file & IP setups | Clearly mentioned user-specific key and IP setup in instructions |

---

## Author

Prepared by: *Nagamedha Sakhamuri*  
GitHub Repository: [AzureDijkstra_Assignment](https://github.com/Nagamedha/AzureDijkstra_Assignment)

---

## Final Note:
> Clone or Download the Repository → SSH into your own Azure VM → Place these files → Follow above steps → Execute → Output will be generated inside VM → Download if needed.

