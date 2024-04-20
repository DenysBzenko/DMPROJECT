import random

class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.adj_list = {}
        self.vertices = set()
        self.weights = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = set()
            self.vertices.add(vertex)

    def add_edge(self, u, v, weight=None):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj_list[u].add(v)
        if weight is not None:
            self.weights[(u, v)] = weight
        if not self.directed:
            self.adj_list[v].add(u)
            if weight is not None:
                self.weights[(v, u)] = weight

    def generate_random_graph(self, n, delta, weighted=False, max_weight=10):
        self.adj_list = {}
        self.vertices = set()
        self.weights = {}

        for i in range(n):
            self.add_vertex(i)

        max_edges = n * (n - 1) // 2 if not self.directed else n * (n - 1)
        num_edges = int(max_edges * delta)

        edges_added = 0
        while edges_added < num_edges:
            u = random.randint(0, n - 1)
            v = random.randint(0, n - 1)
            if u != v and (v, u) not in self.weights and (u, v) not in self.weights:
                weight = random.randint(1, max_weight) if weighted else None
                self.add_edge(u, v, weight)
                edges_added += 1

    def display_graph(self):
        matrix = self.adjacency_matrix()
        print("Adjacency Matrix:")
        for row in matrix:
            print(row)
        print("\nAdjacency List:")
        for vertex, neighbors in self.adj_list.items():
            if self.weights:
                print(f"{vertex}: {[f'{n} (weight={self.weights[(vertex, n)]})' for n in neighbors]}")
            else:
                print(f"{vertex}: {list(neighbors)}")

    def adjacency_matrix(self):
        n = len(self.vertices)
        vertices = list(sorted(self.vertices))
        index = {vertices[i]: i for i in range(n)}
        matrix = [[0] * n for _ in range(n)]

        for i, v in enumerate(vertices):
            for neighbor in self.adj_list[v]:
                matrix[i][index[neighbor]] = 1
                if not self.directed:
                    matrix[index[neighbor]][i] = 1

        return matrix

# Usage example for a weighted directed graph
graph = Graph(directed=False)
graph.generate_random_graph(10, 0.3, weighted=True)
graph.display_graph()
