from collections import defaultdict, deque
from collections.abc import Hashable


class Graph[V: Hashable]:
    """Directed graph stored as an adjacency list."""

    def __init__(self) -> None:
        # Each key is a vertex; its value is the list of vertices it points to.
        self.graph: defaultdict[V, list[V]] = defaultdict(list)

    def add_edge(self, u: V, v: V) -> None:
        """Add an edge from u to v."""
        self.graph[u].append(v)

    def nodes(self) -> list[V]:
        """Every vertex, including those that only appear as an edge's target."""
        seen = list(self.graph)
        for targets in list(self.graph.values()):
            for v in targets:
                if v not in seen:
                    seen.append(v)
        return seen

    def bfs(self, start: V) -> list[V]:
        """Return vertices in breadth-first order from start.

        Uses a set for visited vertices, so it works for any hashable vertex
        (not only small integers) and for vertices that only appear as the
        target of an edge. A deque gives O(1) dequeues.
        """
        visited = {start}
        queue = deque([start])
        traversal_order: list[V] = []

        while queue:
            node = queue.popleft()
            traversal_order.append(node)
            for neighbour in self.graph.get(node, []):
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

        return traversal_order
