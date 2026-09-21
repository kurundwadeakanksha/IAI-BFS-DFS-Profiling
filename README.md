Name: Akanksha Amol Kurundwade<br>
PRN: 25UAM092<br>
Course: Introduction to Artificial Intelligence<br>
SLE-2: BFS vs DFS Performance Profiling<br>

---------------------------------------------------------------------------------------------------
Overview
----------------------------------------------------------------------------------------------------

This project is part of Self Learning Exercise (SLE-2) for the Introduction to Artificial Intelligence course.

The purpose of this experiment is to compare the practical performance of two uninformed search algorithms:

Breadth-First Search (BFS)
Depth-First Search (DFS)

Both algorithms were tested on the same graph, with the same start node and goal node, to make the comparison fair.

------------------------------------------------------------------------------
Objective
------------------------------------------------------------------------------

The main objectives of this SLE-2 experiment are:

1.Implement BFS and DFS.<br>
2.Run both algorithms on the same graph.<br>
3.Measure their execution time.<br>
4.Count the number of nodes expanded.<br>
5.Run the experiment three times and calculate the average time.<br>
6.Use py-spy for additional profiling.<br>
7.Compare the experimental results with the expected behavior of the algorithms.<br>

---------------------------------------------------------------------------------------------------
Problem Used
----------------------------------------------------------------------------------------------------

A small graph containing 47 nodes was used for the experiment.

Start Node: A
Goal Node: AU

Both BFS and DFS were given exactly the same graph and search problem.

Algorithms
1. Breadth-First Search (BFS)

BFS explores a graph level by level.

It uses a queue data structure.

Basic idea:

Start
  ↓
Explore nearby nodes
  ↓
Explore next level
  ↓
Continue until goal is found

==========================================================

2. Depth-First Search (DFS)

DFS explores one branch as deeply as possible before backtracking.

It uses a stack data structure.

Basic idea:

Start
  ↓
Go deeper
  ↓
Continue along the branch
  ↓
Backtrack when required

-------------------------------------------------------------------------------------------
Tools Used
----------------------------------------------------------------------------------------------------

Python timeit

The timeit module was used to measure the execution time of BFS and DFS.

Each algorithm was tested in 3 experimental runs.

Each timing measurement internally performed multiple searches to obtain a measurable timing value.

Manual Node Counter

A node counter was included in both BFS and DFS to record how many nodes were expanded before reaching the goal.

py-spy

py-spy was used as an additional profiling tool to generate a flame graph.

The profiling command used was:

py-spy record --output profile.svg -- python profile_search.py

The profiler completed successfully with:

Samples: 3
Errors: 0

The py-spy output is included in this repository as profile.svg.

------------------------------------------------------------------------------------------
Experimental Results
----------------------------------------------------------------------------------------------------

Metric	                          BFS	                                     DFS
Run 1 Time (ms)	               0.014054	                                 0.019412
Run 2 Time (ms)	               0.013642	                                 0.019668
Run 3 Time (ms)	               0.013061	                                 0.018913
Average Time (ms)	             0.013585	                                 0.019331
Nodes Expanded	                  47	                                      47
Goal Found	                     True                                     	True

----------------------------------------------------------------------------------------
Observation
----------------------------------------------------------------------------------------------------

For the selected graph and experimental setup, BFS recorded a lower average execution time than DFS.

The measured average times were:

BFS: 0.013585 ms
DFS: 0.019331 ms

Both algorithms expanded 47 nodes and successfully found the goal node AU.

The result applies specifically to this graph and implementation. It does not mean that BFS will always be faster than DFS for every problem.

---------------------------------------------------------------------------------------------
Project Files
----------------------------------------------------------------------------------------------------
File	                                   Description
1.bfs_dfs.py	                     Contains the graph, BFS implementation, and DFS implementation<br>
2.benchmark.py	                   Measures BFS and DFS execution time over three experimental runs<br>
3.profile_search.py	               Runs BFS and DFS repeatedly for profiler observation<br>
4.profile.svg	                     Flame graph generated using py-spy<br>
5.README.md	                       Project documentation<br>
6.gitignore                        Prevents Python cache files from being uploaded<br>

---------------------------------------------------------------------------------------------
How to Run
----------------------------------------------------------------------------------------------------
1. Run the BFS/DFS benchmark
python benchmark.py

This displays:
1.Time for each run
2.Average execution time
3.Nodes expanded
4.Whether the goal was found

2. Run the profiling program
python profile_search.py

3. Generate the py-spy flame graph
py-spy record --output profile.svg -- python profile_search.py

On Windows, if py-spy is not available directly in PATH, the installed executable can be used with its full path.

-----------------------------------------------------------------------------------------------------
Conclusion
----------------------------------------------------------------------------------------------------

This experiment demonstrates how theoretical search algorithms can be evaluated using actual performance measurements.

BFS and DFS were tested fairly on the same graph. Execution time and node expansion were recorded, and additional profiling was performed using py-spy.

The experiment helped in understanding the practical use of performance profiling and the importance of using measured data when comparing algorithms.

--------------------------------------------------------------------------------------------------
AI Contribution
----------------------------------------------------------------------------------------------------

AI tools were used during this SLE-2 to:

Understand profiling concepts.
Understand BFS and DFS implementation.
Prepare and explain the benchmarking approach.
Understand timeit and py-spy.
Organize the project documentation.

The code was executed locally, the experiments were performed on the student's computer, and the reported performance values were obtained from the actual experiments.
