from collections import deque
#------------------------------
#Graph representation using adjacency list
#------------------------------
graph = {
   'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],

    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],

    'H': ['P', 'Q'],
    'I': ['R', 'S'],
    'J': ['T', 'U'],
    'K': ['V', 'W'],

    'L': ['X', 'Y'],
    'M': ['Z', 'AA'],
    'N': ['AB', 'AC'],
    'O': ['AD', 'AE'],

    'P': ['AF'],
    'Q': ['AG'],
    'R': ['AH'],
    'S': ['AI'],
    'T': ['AJ'],
    'U': ['AK'],
    'V': ['AL'],
    'W': ['AM'],

    'X': ['AN'],
    'Y': ['AO'],
    'Z': ['AP'],
    'AA': ['AQ'],
    'AB': ['AR'],
    'AC': ['AS'],
    'AD': ['AT'],
    'AE': ['AU'],

    'AF': [],
    'AG': [],
    'AH': [],
    'AI': [],
    'AJ': [],
    'AK': [],
    'AL': [],
    'AM': [],
    'AN': [],
    'AO': [],
    'AP': [],
    'AQ': [],
    'AR': [],
    'AS': [],
    'AT': [],
    'AU': []
}

#-----------------------------------
# Breadth First Search (BFS) implementation
#-----------------------------------

def bfs(graph, start,goal):
    queue = deque([start])
    visited = set() 
    nodes_expanded = 0

    while queue:
        current_node = queue.popleft()

        if current_node in visited:
            continue

        visited.add(current_node)
        nodes_expanded += 1

        if current_node == goal:
            return True, nodes_expanded

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append(neighbor)  

    return False, nodes_expanded

#-----------------------------------
# Depth First Search (DFS) implementation
#-----------------------------------

def dfs(graph, start, goal):
    stack = [start]
    visited = set()
    nodes_expanded = 0

    while stack:
        current_node = stack.pop()

        if current_node in visited:
            continue

        visited.add(current_node)
        nodes_expanded += 1

        if current_node == goal:
            return True, nodes_expanded

        for neighbor in reversed(graph[current_node]):
            if neighbor not in visited:
                stack.append(neighbor)

    return False, nodes_expanded