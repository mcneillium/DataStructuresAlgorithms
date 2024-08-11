from collections import defaultdict

# The Graph class represents a directed graph using an adjacency list.
class Graph:
    def __init__(self):
        # Initialize an empty default dictionary to store the adjacency list.
        # Each key in the dictionary is a vertex, and the corresponding value is a list of adjacent vertices.
        self.graph = defaultdict(list)

    # This method adds an edge from vertex u to vertex v in the graph.
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # This method performs a breadth-first search (BFS) starting from the given start vertex.
    def bfs(self, start):
        # Create a list to keep track of visited vertices, initialized to False.
        visited = [False] * (max(self.graph) + 1)
        queue = []  # Initialize an empty queue for BFS.

        # Mark the start vertex as visited and enqueue it.
        queue.append(start)
        visited[start] = True

        while queue:
            # Dequeue a vertex from the queue and print it.
            node = queue.pop(0)
            print(node, end=' ')

            # Get all adjacent vertices of the dequeued vertex.
            # If an adjacent vertex hasn't been visited, mark it visited and enqueue it.
            for i in self.graph[node]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

# Example usage:
if __name__ == "__main__":
    # Create a new graph.
    g = Graph()
    # Add edges to the graph.
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    # Perform BFS starting from vertex 2.
    print("BFS starting from vertex 2:")
    g.bfs(2)
