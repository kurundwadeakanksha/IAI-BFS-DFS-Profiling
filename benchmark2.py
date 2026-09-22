import timeit
from bfs_dfs import graph, bfs, dfs

# --------------------------------------------------
# SLE-2: BFS vs DFS
# Best, Average and Worst Case Comparison
# --------------------------------------------------

START_NODE = 'A'

# Test cases based on the existing graph
test_cases = {
    "Best Case": "B",
    "Average Case": "J",
    "Worst Case": "AU"
}

NUMBER_OF_RUNS = 3
REPEAT_COUNT = 1000


def measure_bfs(goal):
    total_times = timeit.repeat(
        lambda: bfs(graph, START_NODE, goal),
        repeat=NUMBER_OF_RUNS,
        number=REPEAT_COUNT
    )

    average_time = (sum(total_times) / NUMBER_OF_RUNS) * 1000 / REPEAT_COUNT

    found, nodes = bfs(graph, START_NODE, goal)

    return average_time, nodes, found


def measure_dfs(goal):
    total_times = timeit.repeat(
        lambda: dfs(graph, START_NODE, goal),
        repeat=NUMBER_OF_RUNS,
        number=REPEAT_COUNT
    )

    average_time = (sum(total_times) / NUMBER_OF_RUNS) * 1000 / REPEAT_COUNT

    found, nodes = dfs(graph, START_NODE, goal)

    return average_time, nodes, found


print("==============================================")
print(" SLE-2: BFS vs DFS CASE ANALYSIS")
print("==============================================")
print("Start Node:", START_NODE)
print("Runs:", NUMBER_OF_RUNS)
print("Repetitions per run:", REPEAT_COUNT)


for case_name, goal in test_cases.items():

    print("\n----------------------------------------------")
    print(case_name)
    print("----------------------------------------------")
    print("Goal Node:", goal)

    bfs_time, bfs_nodes, bfs_found = measure_bfs(goal)
    dfs_time, dfs_nodes, dfs_found = measure_dfs(goal)

    print("\nBFS:")
    print("Average Time:", f"{bfs_time:.6f}", "ms")
    print("Nodes Expanded:", bfs_nodes)
    print("Goal Found:", bfs_found)

    print("\nDFS:")
    print("Average Time:", f"{dfs_time:.6f}", "ms")
    print("Nodes Expanded:", dfs_nodes)
    print("Goal Found:", dfs_found)

print("\n==============================================")
print(" Comparison completed successfully")
print("==============================================")