from bfs_dfs import graph, bfs, dfs

START_NODE = 'A'

test_cases = {
    "Best Case": "B",
    "Average Case": "J",
    "Worst Case": "AU"
}

# Repeat searches so py-spy has enough time to collect samples
REPETITIONS = 100000

print("==============================================")
print(" SLE-2 py-spy PROFILING - CASE ANALYSIS")
print("==============================================")

for case_name, goal in test_cases.items():

    print("\n----------------------------------------------")
    print(case_name)
    print("Goal Node:", goal)
    print("----------------------------------------------")

    print("Running BFS...")

    for _ in range(REPETITIONS):
        bfs(graph, START_NODE, goal)

    print("BFS completed.")

    print("Running DFS...")

    for _ in range(REPETITIONS):
        dfs(graph, START_NODE, goal)

    print("DFS completed.")

print("\nProfiling program finished.")