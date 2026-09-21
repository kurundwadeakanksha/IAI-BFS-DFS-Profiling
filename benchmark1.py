import timeit
from benchmark import RUNS
from bfs_dfs import graph, bfs, dfs

start_node = 'A'
goal_node = 'AU'

#--------------------------------------
# Repeat the same experiment many times
#--------------------------------------
REPEATS = 1000

#--------------------------------------
# Timing BFS
#--------------------------------------
bfs_total_time = timeit.timeit(
    lambda: bfs(graph, start_node, goal_node), 
     number=REPEATS)

#--------------------------------------
# Timing DFS
#--------------------------------------
dfs_total_time = timeit.timeit(
    lambda: dfs(graph, start_node, goal_node), 
     number=REPEATS)

#-------------------------------------
# Convert total times to milliseconds
#--------------------------------------
bfs_total_time_ms = bfs_total_time * 1000
dfs_total_time_ms= dfs_total_time * 1000

#--------------------------------------
#Calculate average times
#--------------------------------------
average_bfs_time = (bfs_total_time_ms / REPEATS)
average_dfs_time = (dfs_total_time_ms / REPEATS)

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
print("Total runs:", REPEATS)
print("Total Time:", f"{bfs_total_time_ms:.6f}", "ms")
print("Average Time:", f"{average_bfs_time:.6f}", "ms")
print("Nodes expanded:", bfs_nodes)
print("Goal found:", bfs_found)

print("\nDFS Results:")
print("Total runs:", REPEATS)
print("Total Time:", f"{dfs_total_time_ms:.6f}", "ms")
print("Average Time:", f"{average_dfs_time:.6f}", "ms")
print("Nodes expanded:", dfs_nodes)
print("Goal found:", dfs_found)