from collections import deque

# =========================================================
# COMP-2350 - Lab 6
# Graph Traversal Algorithms: DFS and BFS
# ---------------------------------------------------------
# Instructions:
# You MUST implement:
#   1) Depth-First Search (DFS)
#   2) Breadth-First Search (BFS)
#
# Do NOT use any built-in graph libraries.
# You may use Python built-in data structures (list, set, deque).
#
# Submit:
#   - Completed Python file
#   - Output screenshot
#   - Answers to the reflection questions at the bottom
# =========================================================


# ---------------------------------------------------------
# Graph Representation (Adjacency List)
# ---------------------------------------------------------

graph = {
    'a': ['c', 'd'],
    'b': ['f'],
    'c': ['a', 'd', 'e', 'f'],
    'd': ['a', 'c'],
    'e': ['c'],
    'f': ['b', 'c'],
    'g': ['h'],
    'h': ['g', 'i', 'j'],
    'i': ['h'],
    'j': ['h']
}


# =========================================================
# Part 1: Depth-First Search (DFS)
# =========================================================

def dfs(graph, start):

    visited = set()
    stack = []
    
    stack.append(start)

    while len(stack) > 0:

        vertex = stack.pop()

        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    stack.append(neighbor)

    return visited

# =========================================================
# Part 2: Breadth-First Search (BFS)
# =========================================================

def bfs(graph, start):

    visited = set()
    queue = deque()

    queue.append(start)

    while len(queue) > 0:

        vertex = queue.popleft()

        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return visited

# =========================================================
# Part 3: Testing
# =========================================================

if __name__ == "__main__":
    print("DFS Traversal starting from 'a':")
    dfs(graph, 'a')

    print("\nBFS Traversal starting from 'a':")
    bfs(graph, 'a')

# =========================================================
# Reflection Questions (Answer in comments below)
# =========================================================

# 1) What is the time complexity of DFS using an adjacency list?
# Θ(|V| + |E|). We visit each vertex once, and we scan each adjacency list once,
# so total work is proportional to vertices plus edges.

# 2) What is the time complexity of BFS using an adjacency list?
# Θ(|V| + |E|). Same reasoning: each vertex is visited once, and each edge is
# considered while exploring neighbors.

# 3) What would the complexity be if we used an adjacency matrix?
# Θ(|V|^2) for both DFS and BFS, because for each vertex you may need to scan an
# entire row of the matrix (V entries) to find its neighbors.

# 4) When would you prefer BFS over DFS?
# When you want the shortest path in an unweighted graph (minimum number of edges),
# or when you want level-by-level traversal.

# 5) When would you prefer DFS over BFS?
# When you want to explore deeply, do backtracking, detect cycles, find connected
# components, or do things like topological sorting on directed acyclic graphs.