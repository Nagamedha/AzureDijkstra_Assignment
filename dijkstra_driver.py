import collections
import heapq

# Read adjacency list
adjacency_list = {}

with open('adjacency_list_output/part-00000', 'r') as f:
    for line in f:
        node, neighbors = eval(line.strip())
        adjacency_list[node] = neighbors

source = 0  # From spark output (or hardcode)

distances = collections.defaultdict(lambda: float('inf'))
distances[source] = 0

visited = set()
pq = [(0, source)]

while pq:
    curr_dist, u = heapq.heappop(pq)
    if u in visited:
        continue
    visited.add(u)
    for neighbor, weight in adjacency_list.get(u, []):
        if distances[neighbor] > curr_dist + weight:
            distances[neighbor] = curr_dist + weight
            heapq.heappush(pq, (distances[neighbor], neighbor))

print(f"Shortest distances from node {source}:")

result = []
for node in sorted(adjacency_list.keys()):
    dist = distances[node]
    print(f"Node {node}: {dist}")
    result.append((node, dist))

# Save Output to File inside Azure VM
with open("shortest_paths_output.txt", "w") as f:
    f.write(f"Shortest distances from node {source}:\n")
    for node, dist in result:
        f.write(f"Node {node}: {dist}\n")

print("Output successfully saved to shortest_paths_output.txt")
