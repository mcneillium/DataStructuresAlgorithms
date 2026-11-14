from collections import defaultdict, deque


class Graph:
    """Directed graph stored as an adjacency list."""

    def __init__(self):
        # Each key is a vertex; its value is the list of vertices it points to.
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        """Add an edge from u to v."""
        self.graph[u].append(v)

    def bfs(self, start):
        """Return vertices in breadth-first order from start.

        Uses a set for visited vertices, so it works for any hashable vertex
        (not only small integers) and for vertices that only appear as the
        target of an edge. A deque gives O(1) dequeues.
        """
        visited = {start}
        queue = deque([start])
        traversal_order = []

        while queue:
            node = queue.popleft()
            traversal_order.append(node)
            for neighbour in self.graph.get(node, []):
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

        return traversal_order
