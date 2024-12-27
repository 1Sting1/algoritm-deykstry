

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, src, tgt, weight):
        if src not in self.graph:
            self.graph[src] = []
        if tgt not in self.graph:
            self.graph[tgt] = []
        self.graph[src].append((tgt, weight))
        self.graph[tgt].append((src, weight))

    def get_neighbors(self, node):
        return self.graph.get(node, [])

    def get_edge_weight(self, src, tgt):
        for neighbor, weight in self.graph.get(src, []):
            if neighbor == tgt:
                return weight
        return None
