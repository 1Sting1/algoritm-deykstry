

class deykstra:
    def __init__(self, graph):
        self.graph = graph

    def find_shortest_paths_with_trace(self, start):
        distances = {node: float('inf') for node in self.graph.graph}
        distances[start] = 0
        previous_nodes = {node: None for node in self.graph.graph}
        visited = set()
        nodes = list(self.graph.graph.keys())

        while nodes:
            min_distance_node = None
            for node in nodes:
                if node not in visited:
                    if min_distance_node is None or distances[node] < distances[min_distance_node]:
                        min_distance_node = node

            if min_distance_node is None:
                break

            visited.add(min_distance_node)
            nodes.remove(min_distance_node)

            for neighbor, weight in self.graph.get_neighbors(min_distance_node):
                if neighbor not in visited:
                    new_distance = distances[min_distance_node] + weight
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        previous_nodes[neighbor] = min_distance_node

        return distances, previous_nodes