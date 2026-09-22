Name: Akanksha Amol Kurundwade  <br>
PRN: 25UAM092  <br>
Course: Introduction to Artificial Intelligence  <br>
SLE-2: BFS vs DFS Performance Profiling  <br>

---------------------------------------------------------------------------------------------------
Overview
---------------------------------------------------------------------------------------------------

This project is part of Self Learning Exercise (SLE-2) for the Introduction to Artificial Intelligence course.
The purpose of this experiment is to compare the practical performance of two uninformed search algorithms:
- Breadth-First Search (BFS)<br>
- Depth-First Search (DFS)
Both algorithms were tested on the same graph to make the comparison fair.

------------------------------------------------------------------------------
Objective
------------------------------------------------------------------------------

The main objectives of this SLE-2 experiment are:<br>
1. Implement BFS and DFS.<br>
2. Run both algorithms on the same graph.<br>
3. Measure their execution time.<br>
4. Count the number of nodes expanded.<br>
5. Compare Best, Average, and Worst cases.<br>
6. Run the experiment three times and calculate the average time.<br>
7. Use py-spy for additional profiling.<br>
8. Compare the experimental results with the expected behavior of the algorithms.<br>

---------------------------------------------------------------------------------------------------
Problem Used
---------------------------------------------------------------------------------------------------

A small graph containing 47 nodes was used for the experiment.
Start Node: A<br>
Test Cases:<br>
- Best Case: B<br>
- Average Case: J<br>
- Worst Case: AU<br>
Both BFS and DFS were given the same graph and starting node.
Graph used:
             
                              A
                           /     \
                          B       C
                        /  \     /  \
                       D    E   F    G
                      / \  / \ / \  / \
                     H  I J  K L M N  O
                    / \ / \ / \ / \ / \
                   P  Q R S T U V W X Y Z AA AB AC AD AE
                   |  | | | | | | | | | |  |  |  |  |  |
                  AF AG AH AI AJ AK AL AM AN AO AP AQ AR AS AT AU           

==========================================
Breadth-First Search (BFS)
BFS explores a graph level by level.
It uses a queue data structure.
Basic idea:<br>
Start<br>
↓<br>
Explore nearby nodes<br>
↓<br>
Explore next level<br>
↓<br>
Continue until goal is found<br>

==============================

Depth-First Search (DFS)<br>
DFS explores one branch as deeply as possible before backtracking.
It uses a stack data structure.
Basic idea:<br>
Start<br>
↓<br>
Go deeper<br>
↓<br>
Continue along the branch<br>
↓<br>
Backtrack when required<br>

------------------------------------
Tools Used<br>
------------------------------------
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
Samples: 3<br>
Errors: 0<br>
The py-spy output is included in this repository as profile.svg.

-------------------------------------------------------
## Experimental Results
------------------------------------------------------
| Case | Goal Node | BFS Time (ms) | BFS Nodes Expanded | DFS Time (ms) | DFS Nodes Expanded |
|---|---|---:|---:|---:|---:|
| Best Case | B | 0.000999 | 2 | 0.000872 | 2 |
| Average Case | J | 0.003761 | 10 | 0.008100 | 15 |
| Worst Case | AU | 0.013468 | 47 | 0.017964 | 47 |

Worst Case – 3 Run Results
------------------------------------

| Metric | BFS | DFS |
|---|---:|---:|
| Run 1 Time (ms) | 0.014054 | 0.019412 |
| Run 2 Time (ms) | 0.013642 | 0.019668 |
| Run 3 Time (ms) | 0.013061 | 0.018913 |
| **Average Time (ms)** | **0.013585** | **0.019331** |
| Nodes Expanded | **47** | **47** |
| Goal Found | **True** | **True** |

--------------------------------------------------
Observation
-----------------------------------------------------

For the selected graph and experimental setup, the goal position affected the practical performance of BFS and DFS.
In the Best Case, both algorithms expanded 2 nodes.
In the Average Case, BFS expanded 10 nodes while DFS expanded 15 nodes.
In the Worst Case, both algorithms expanded 47 nodes.
The measured results are specific to this graph and implementation and do not mean that BFS will always be faster than DFS.

-----------------------------------------------------------------------
Project Files
--------------------------------------------------------------------
| File | Description |
|---|---|
| bfs_dfs.py | Contains the graph, BFS implementation, and DFS implementation |
| benchmark.py | Measures BFS and DFS execution time |
| benchmark2.py | Performs Best, Average, and Worst Case analysis |
| profile_search.py | Runs BFS and DFS for py-spy profiling |
| profile.svg | Flame graph generated using py-spy |
| README.md | Project documentation |
| .gitignore | Prevents Python cache files from being uploaded |

--------------------------------------------
How to Run
--------------------------------------------

Run the BFS/DFS program<br>
python bfs_dfs.py<br>
This displays:<br>
Nodes expanded by BFS<br>
Nodes expanded by DFS<br>
Whether the goal was found<br>
Run the case analysis<br>
python benchmark2.py<br>
This displays:<br>
Best Case<br>
Average Case<br>
Worst Case<br>
Execution time<br>
Nodes expanded<br>
Goal found status<br>
Run the profiling program<br>
python profile_search.py<br>
Generate the py-spy flame graph<br>
py-spy record --output profile.svg -- python profile_search.py<br>
On Windows, if py-spy is not available directly in PATH, the installed executable can be used with its full path.

-----------------------------------------------------------
Conclusion
--------------------------------------------

This experiment demonstrates how theoretical search algorithms can be evaluated using actual performance measurements.
BFS and DFS were tested fairly on the same graph. Execution time and node expansion were recorded for Best, Average, and Worst cases, and additional profiling was performed using py-spy.
The experiment helped in understanding the practical use of performance profiling and the importance of using measured data when comparing algorithms
