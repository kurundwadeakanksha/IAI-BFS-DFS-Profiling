# AI Contribution Log

## SLE-2: BFS vs DFS Performance Profiling

**Name:** Akanksha Amol Kurundwade  
**PRN:** 25UAM092  
**Course:** 02AML204 – Introduction to Artificial Intelligence  
**Project:** BFS vs DFS Performance Profiling  

---

## 1. AI Tools Used

The following AI tools were used during the development of this SLE-2 project:

- ChatGPT
- GitHub Copilot

---

## 2. Contribution Log

| Sr. No. | AI Tool | Purpose / Assistance | Student's Work |
|---|---|---|---|
| 1 | ChatGPT | Helped understand the SLE-2 profiling requirements and report structure. | Read and understood the requirements and prepared the experiment accordingly. |
| 2 | ChatGPT | Explained BFS and DFS concepts and their implementation. | Implemented and tested the algorithms. |
| 3 | GitHub Copilot | Provided code suggestions for BFS/DFS and performance-testing code. | Reviewed, modified, and tested the suggested code. |
| 4 | ChatGPT | Helped understand Python `timeit` and execution-time measurement. | Ran the benchmark programs and collected actual timing results. |
| 5 | ChatGPT | Helped understand manual node counting. | Added/checked the node counter and verified the number of nodes expanded. |
| 6 | ChatGPT | Helped understand Best, Average, and Worst Case testing. | Selected the goal nodes B, J, and AU and performed the experiments. |
| 7 | ChatGPT | Helped understand and troubleshoot `py-spy`. | Installed py-spy, executed the profiling command, and generated `profile.svg`. |
| 8 | ChatGPT | Helped troubleshoot Git/GitHub commands and repository organization. | Managed the Git repository, commits, and GitHub push operations. |
| 9 | ChatGPT | Helped organize the README and documentation. | Reviewed the documentation and added the actual project information and results. |

---

## 3. AI-Assisted Code

AI assistance was used for understanding and generating code suggestions related to:

- BFS implementation
- DFS implementation
- Execution-time benchmarking
- Node counting
- Best/Average/Worst case testing
- py-spy profiling setup

The AI-generated suggestions were reviewed and modified according to the requirements of the experiment.

---

## 4. Work Performed by Student

The following work was performed and verified by the student:

- Created and used the 47-node graph.
- Implemented and tested BFS and DFS.
- Selected the Best, Average, and Worst Case goal nodes.
- Ran the programs locally.
- Performed the timing experiments.
- Performed three experimental runs.
- Collected the actual execution-time results.
- Verified the number of nodes expanded.
- Installed and executed py-spy.
- Generated the profiling output.
- Organized the project files.
- Created and maintained the GitHub repository.
- Prepared the final experimental analysis.

---

## 5. Actual Experimental Results

The reported values were obtained from actual program execution.

| Case | Goal | BFS Time (ms) | BFS Nodes | DFS Time (ms) | DFS Nodes |
|---|---|---:|---:|---:|---:|
| Best Case | B | 0.000999 | 2 | 0.000872 | 2 |
| Average Case | J | 0.003761 | 10 | 0.008100 | 15 |
| Worst Case | AU | 0.013468 | 47 | 0.017964 | 47 |

### Worst Case – 3 Run Average

| Metric | BFS | DFS |
|---|---:|---:|
| Run 1 | 0.014054 ms | 0.019412 ms |
| Run 2 | 0.013642 ms | 0.019668 ms |
| Run 3 | 0.013061 ms | 0.018913 ms |
| **Average** | **0.013585 ms** | **0.019331 ms** |

---

## 6. Ownership Statement

AI tools were used as assistance for learning, code suggestions, troubleshooting, and documentation.

The student reviewed and understood the suggestions, executed the programs locally, collected the experimental data, verified the results, and performed the final analysis.

The performance values in the project were obtained from the student's actual experimental runs.
