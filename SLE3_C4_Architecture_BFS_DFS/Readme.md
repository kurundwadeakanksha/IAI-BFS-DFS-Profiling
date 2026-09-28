# SLE-3: Architectural Design Using C4 Model

## Course:**02AML204 – Introduction to Artificial Intelligence**

**Name:** Akanksha Amol Kurundwade

**PRN:**25UAM092


## Project Title

**47-Node Graph Search System Using BFS and DFS**

## About the Project

This project represents the architecture of a 47-node graph search system using the **C4 Model**.

The system uses two search algorithms:

* **Breadth-First Search (BFS)**
* **Depth-First Search (DFS)**

The same search system was used in **SLE-2** for performance comparison using `timeit` and `py-spy`. In SLE-3, the system is represented using all four levels of the C4 architecture model.

## C4 Model

The project contains all four C4 levels:

### Level 1 – Context Diagram

Shows the overall system, user interaction, input, and search result.
The user provides the search input to the Graph Search System. The system contains the 47-node search tree and performs BFS or DFS to find the goal node. After the search is completed, the system returns the search result to the user.

### Level 2 – Container Diagram

Shows the major building blocks of the system:

* Input Module = Takes the start node and goal node/search input from the user.
* Graph Management = Stores and manages the 47-node tree using the graph/adjacency-list representation.
* Search Engine = Runs the selected BFS or DFS search algorithm.
* Visited / Memory = Stores already visited nodes to avoid repeated exploration.
* Output Module = Displays the final search result and search information.

### Level 3 – Component Diagram

Shows the internal components of the main **Search Engine** container:

* BFS
* DFS
* Queue
* Stack
* Goal Test
The Search Engine contains the two search strategies, BFS and DFS. BFS uses a queue to manage the order of node exploration, while DFS uses a stack. The goal test checks whether the currently processed node is the required goal. This view focuses only on the internal structure of the Search Engine container.

### Level 4 – Code Overview

Shows the important files, functions, and variables used in the implementation:

bfs_dfs.py – graph:	Stores the 47-node graph using adjacency-list representation.
bfs_dfs.py – bfs(): Performs Breadth-First Search using a queue.
bfs_dfs.py – dfs():	Performs Depth-First Search using a stack.
bfs_dfs.py – visited:	Stores already visited nodes during the search.
bfs_dfs.py – nodes_expanded:	Counts the nodes explored during the search.
benchmark.py – measure_bfs():	Measures the average execution time of BFS using timeit.
benchmark.py – measure_dfs():	Measures the average execution time of DFS using timeit.
profile_search.py:	Runs repeated BFS/DFS searches for py-spy profiling.


## SLE-2 Connection

In SLE-2, the BFS and DFS algorithms were tested on a **47-node graph**.

The performance was analyzed using:

* `timeit` for execution-time measurement
* `py-spy` for profiling
* Number of expanded nodes
* Best, average, and worst-case goal positions

The profiling result was generated as:

`profile_search.svg`

## Purpose of SLE-3

The purpose of SLE-3 is to understand how the existing search system can be represented at different levels of software architecture.

The C4 model helps move from:

**Big Picture → Main Parts → Internal Components → Code**

## Learning Outcome

Through this SLE, I learned:

* How to represent software architecture using the C4 Model.
* Difference between Context, Container, Component, and Code levels.
* How BFS and DFS fit into the architecture of a search system.
* How software architecture connects with implementation and performance analysis.

## Tools Used

* Python
* VS Code
* Git & GitHub
* diagrams.net (draw.io)
* `timeit`
* `py-spy`
