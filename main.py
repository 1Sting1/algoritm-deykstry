from graph import Graph
from deykstra import Deykstra

def read_graph_from_file(file_path):
    graph = Graph()
    with open(file_path, 'r') as file:
        for line in file:
            src, tgt, weight = map(int, line.split())
            graph.add_edge(src, tgt, weight)
    return graph

def main():
    file_path = '1000.txt'
    graph = read_graph_from_file(file_path)

    start_vertex = int(input("Введите первую вершину: "))
    end_vertex = int(input("Введите последнюю вершину: "))
    dijkstra = Deykstra(graph)

    shortest_paths, previous_nodes = dijkstra.find_shortest_paths_with_trace(start_vertex)

    path = []
    current = end_vertex
    while current is not None:
        path.append(current)
        current = previous_nodes[current]
    path = path[::-1]
    if end_vertex in shortest_paths:
        print("\nКратчайший путь:")
        for i in range(len(path) - 1):
            print(f"От {path[i]} до {path[i + 1]}, Расстояние: {graph.get_edge_weight(path[i], path[i + 1])}")
        print(f"\nОт {start_vertex} до {end_vertex}: {shortest_paths[end_vertex]}")
    else:
        print(f"\nОт {start_vertex} до {end_vertex} не найден.")

if __name__ == '__main__':
    main()