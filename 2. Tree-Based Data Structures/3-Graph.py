from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    # Adding a node to the graph
    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    # Removing a node from the graph
    def remove_node(self, node):
        if node in self.graph:
            del self.graph[node]
            for key in self.graph:
                if node in self.graph[key]:
                    self.graph[key].remove(node)

    # Adding an edge between two nodes
    def add_edge(self, node1, node2):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)

    # Removing an edge between two nodes
    def remove_edge(self, node1, node2):
        if node1 in self.graph and node2 in self.graph:
            if node2 in self.graph[node1]:
                self.graph[node1].remove(node2)
            if node1 in self.graph[node2]:
                self.graph[node2].remove(node1)

    # Checking if two nodes are connected
    def are_connected(self, node1, node2):
        return node2 in self.graph[node1]

    # Finding the neighbors of a node
    def neighbors(self, node):
        return self.graph[node]

    # Traversing the graph (depth-first search)
    def dfs(self, start):
        visited = set()
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                stack.extend(self.graph[node])
        return visited

    # Traversing the graph (breadth-first search)
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                queue.extend(self.graph[node])
        return visited

    # Finding the shortest path between two nodes
    def shortest_path(self, start, end):
        visited = set()
        queue = deque([(start, [start])])
        while queue:
            node, path = queue.popleft()
            if node not in visited:
                visited.add(node)
                for neighbor in self.graph[node]:
                    if neighbor == end:
                        return path + [neighbor]
                    queue.append((neighbor, path + [neighbor]))

    # Finding the connected components of the graph
    def connected_components(self):
        visited = set()
        components = []
        for node in self.graph:
            if node not in visited:
                component = self.dfs(node)
                components.append(component)
                visited.update(component)
        return components

    # Checking if the graph is cyclic
    def is_cyclic(self):
        visited = set()
        stack = []
        for node in self.graph:
            if node not in visited:
                if self._is_cyclic(node, visited, stack):
                    return True
        return False

    def _is_cyclic(self, node, visited, stack):
        visited.add(node)
        stack.append(node)
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                if self._is_cyclic(neighbor, visited, stack):
                    return True
            elif neighbor in stack:
                return True
        stack.remove(node)
        return False

    # Getting all nodes or edges
    def get_nodes(self):
        return list(self.graph.keys())

    def get_edges(self):
        edges = []
        for node, neighbors in self.graph.items():
            for neighbor in neighbors:
                edges.append((node, neighbor))
        return edges

    # Getting the number of nodes or edges
    def num_nodes(self):
        return len(self.graph)

    def num_edges(self):
        return sum(len(neighbors) for neighbors in self.graph.values()) // 2

    # Checking if a graph is empty
    def is_empty(self):
        return not self.graph

    # Clearing a graph
    def clear(self):
        self.graph.clear()

    # Copying a graph
    def copy(self):
        new_graph = Graph()
        new_graph.graph = self.graph.copy()
        return new_graph

    # Merging two graphs
    def merge(self, other_graph):
        for node, neighbors in other_graph.graph.items():
            for neighbor in neighbors:
                self.add_edge(node, neighbor)

    # Converting a graph to an array or vice versa
    def to_array(self):
        return list(self.graph.items())

    @classmethod
    def from_array(cls, array):
        graph = cls()
        for node, neighbors in array:
            graph.graph[node] = neighbors
        return graph

    # Sorting nodes or edges by a given property
    def sort_nodes(self, key=None, reverse=False):
        return sorted(self.graph.keys(), key=key, reverse=reverse)

    def sort_edges(self, key=None, reverse=False):
        return sorted(self.get_edges(), key=key, reverse=reverse)

    # Finding the maximum or minimum node or edge
    def max_node(self, key=None):
        return max(self.graph.keys(), key=key)

    def min_node(self, key=None):
        return min(self.graph.keys(), key=key)

    def max_edge(self, key=None):
        return max(self.get_edges(), key=key)

    def min_edge(self, key=None):
        return min(self.get_edges(), key=key)

    # Finding the average of all nodes or edges
    def avg_node(self, key=None):
        return sum(self.graph.keys(), key=key) / len(self.graph)

    def avg_edge(self, key=None):
        return sum(self.get_edges(), key=key) / len(self.get_edges())
