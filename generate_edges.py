def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))

    return edges


graph = {'1': ['0'], '0': ['1', '2'], '3': [], '2': ['0']}


print(generate_edges(graph))
