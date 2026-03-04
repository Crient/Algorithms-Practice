# LAB 6 – Depth First Search and Breadth First Search

GECHLENG LIM <br>
COMP2350: ALGORITHMS

This program implements two fundamental graph traversal algorithms: Depth First Search (DFS) and Breadth First Search (BFS). The graph is represented using an adjacency list where each vertex stores a list of its neighboring vertices. Starting from a given vertex, the algorithms explore the graph while ensuring that each vertex is visited only once.

Depth First Search explores the graph by going as deep as possible along a branch before backtracking. In this implementation, a stack is used to manage the traversal order. The starting vertex is pushed onto the stack, and during each iteration a vertex is popped and marked as visited. Any unvisited neighbors are then pushed onto the stack, allowing the algorithm to continue exploring deeper paths before returning to earlier vertices.

Breadth First Search works differently by exploring the graph level by level. Instead of a stack, BFS uses a queue. The starting vertex is placed into the queue, and during each step the vertex at the front of the queue is removed and processed. All unvisited neighboring vertices are then added to the queue, ensuring that vertices closer to the start are explored before moving further away.

Both DFS and BFS run in Θ(|V| + |E|) time when the graph is represented using an adjacency list, since each vertex and edge is processed at most once.

One challenge in this lab was understanding how the choice of data structure affects the traversal behavior of the algorithm. Although DFS and BFS both visit all reachable vertices, the stack in DFS causes deeper exploration first, while the queue in BFS results in a level by level traversal. Implementing a visited set was also important to prevent revisiting vertices and to avoid infinite loops in graphs that contain cycles.

This lab helped reinforce how graph traversal algorithms work in practice and how simple data structures like stacks and queues can significantly change the behavior of an algorithm.

## Sample Output

### DFS Traversal starting from 'a'

Output:<br>
a d c f b e

### BFS Traversal starting from 'a'

Output:<br>
a c d e f b