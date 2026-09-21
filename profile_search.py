from bfs_dfs import graph, bfs, dfs
import time


START = 'A'
GOAL = 'AU'

# Run the searches many times so py-spy has enough time
REPETITIONS = 500000


print("Starting BFS profiling...")

for _ in range(REPETITIONS):
    bfs(graph, START, GOAL)

print("BFS profiling completed.")


print("Starting DFS profiling...")

for _ in range(REPETITIONS):
    dfs(graph, START, GOAL)

print("DFS profiling completed.")

print("Profiling program finished.")