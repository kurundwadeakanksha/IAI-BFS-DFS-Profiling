import timeit
from bfs_dfs import graph, bfs, dfs


START = 'A'
GOAL = 'AU'

# Number of searches inside each timing measurement
INTERNAL_RUNS = 1000

# Number of experimental runs required by SLE-2
EXPERIMENT_RUNS = 3


bfs_times = []
dfs_times = []


print("\n========= SLE-2 3-RUN PERFORMANCE TEST =========")


for run in range(1, EXPERIMENT_RUNS + 1):

    # Measure BFS
    bfs_total_time = timeit.timeit(
        lambda: bfs(graph, START, GOAL),
        number=INTERNAL_RUNS
    )

    # Measure DFS
    dfs_total_time = timeit.timeit(
        lambda: dfs(graph, START, GOAL),
        number=INTERNAL_RUNS
    )

    # Average time for one search
    bfs_average = (bfs_total_time / INTERNAL_RUNS) * 1000
    dfs_average = (dfs_total_time / INTERNAL_RUNS) * 1000

    bfs_times.append(bfs_average)
    dfs_times.append(dfs_average)

    print(f"\nRun {run}")
    print("BFS Time:", f"{bfs_average:.6f}", "ms")
    print("DFS Time:", f"{dfs_average:.6f}", "ms")


# Calculate final averages
bfs_final_average = sum(bfs_times) / len(bfs_times)
dfs_final_average = sum(dfs_times) / len(dfs_times)


# Get node counts
bfs_found, bfs_nodes = bfs(graph, START, GOAL)
dfs_found, dfs_nodes = dfs(graph, START, GOAL)


print("\n========= FINAL AVERAGE =========")

print("\nBFS")
print("Average Time:", f"{bfs_final_average:.6f}", "ms")
print("Nodes Expanded:", bfs_nodes)
print("Goal Found:", bfs_found)

print("\nDFS")
print("Average Time:", f"{dfs_final_average:.6f}", "ms")
print("Nodes Expanded:", dfs_nodes)
print("Goal Found:", dfs_found)

print("\n=================================")