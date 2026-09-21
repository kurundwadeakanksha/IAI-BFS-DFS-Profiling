import timeit
from bfs_dfs import graph, bfs, dfs

# Numbers of repetitions for timing
RUNS = 3
start_node = 'A'
goal_node = 'AU'

#--------------------------------------
# Timing BFS
#--------------------------------------
bfs_time = timeit.timeit(
    lambda: bfs(graph, start_node, goal_node), 
     number=RUNS)

#--------------------------------------
# Timing DFS
#--------------------------------------
dfs_time = timeit.timeit(
    lambda: dfs(graph, start_node, goal_node), 
     number=RUNS)

#--------------------------------------
#Calculate average times
#--------------------------------------
average_bfs_time = (bfs_time / RUNS) * 1000
average_dfs_time = (dfs_time / RUNS) * 1000

#--------------------------------------
# Get nodes counts 
#--------------------------------------
bfs_found, bfs_nodes = bfs(graph, start_node, goal_node)
dfs_found, dfs_nodes = dfs(graph, start_node, goal_node)

#--------------------------------------
# Display results
#--------------------------------------
print("\n=========SLE-2 PERFORMANCE RESULTS=========")
print("\nBFS Results:")
print("Average Time:", f"{average_bfs_time:.6f}", "ms")
print("Nodes expanded:", bfs_nodes)
print("Goal found:", bfs_found)

print("\nDFS Results:")
print("Average Time:", f"{average_dfs_time:.6f}", "ms")
print(f"Nodes visited: {dfs_nodes}")
print("Goal found:", dfs_found)