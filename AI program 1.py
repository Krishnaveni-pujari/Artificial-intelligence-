from collections import deque


class Graph:
    def __init__(self):
        # Dictionary to store the adjacency list
        self.graph = {}

    def add_edge(self, u, v):
        # Add an edge to the graph (directed)
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)

    def bfs(self, start_node):
        """Breadth-First Search Traversal"""
        visited = set()
        # Use deque for O(1) popleft operations
        queue = deque([start_node])
        visited.add(start_node)

        print("BFS Traversal: ", end="")
        while queue:
            current = queue.popleft()
            print(current, end=" ")

            # Enqueue all unvisited neighbors
            for neighbor in self.graph.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        print()

    def dfs(self, start_node):
        """Depth-First Search Traversal (Wrapper)"""
        visited = set()
        print("DFS Traversal: ", end="")
        self._dfs_recursive(start_node, visited)
        print()

    def _dfs_recursive(self, node, visited):
        """Helper method for DFS recursion"""
        visited.add(node)
        print(node, end=" ")

        # Recursively visit all unvisited neighbors
        for neighbor in self.graph.get(node, []):
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)


# --- Driver Code to Test the Implementation ---
if __name__ == "__main__":
    # Initialize the graph object
    g = Graph()

    # Construct a sample graph
    #      A
    #     / \
    #    B   C
    #   /   / \
    #  D   E   F
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'E')
    g.add_edge('C', 'F')

    # Execute algorithms starting from node 'A'
    g.bfs('A')
    g.dfs('A')