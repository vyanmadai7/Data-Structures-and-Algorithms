from collections import defaultdict

class Graph:
    def __init__(self, n, directed=False):
        self.n = n
        self.directed = directed
        self.adj = defaultdict(list)

    def add_edge(self, u, v, w=1):
        self.adj[u].append((v, w))
        if not self.directed:
            self.adj[v].append((u, w))