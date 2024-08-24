from collections import defaultdict

class Graph:
    def __init__(self):
        # Initialize an empty default dictionary to store the adjacency list.
        # Each key in the dictionary is a vertex, and the corresponding value is a list of adjacent vertices.
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        # Always ensure the adjacency list for node u is initialized and append v
        self.graph[u].append(v)

    def bfs(self, start):
        # Create a list to keep track of visited vertices, initialized to False.
        visited = [False] * (max(self.graph) + 1)
        queue = []  # Initialize an empty queue for BFS.
        traversal_order = []

        # Mark the start vertex as visited and enqueue it.
        queue.append(start)
        visited[start] = True

        while queue:
            # Dequeue a vertex from the queue and add it to the traversal order
            node = queue.pop(0)
            traversal_order.append(node)

            # Get all adjacent vertices of the dequeued vertex.
            # If an adjacent vertex hasn't been visited, mark it visited and enqueue it.
            for i in self.graph[node]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

        return traversal_order
