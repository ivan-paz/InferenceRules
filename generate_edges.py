def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))

    return edges

#graph = {'0': ['1', '2'], '1': ['0'], '2': ['0']}
#print(generate_edges(graph))

def simplify_edges(edges):
    simplified_edges = [ ]
    for edge in edges:
        if ( (edge[0],edge[1]) and (edge[1],edge[0]) ) not in simplified_edges:
            simplified_edges = simplified_edges + [edge]
    return simplified_edges
    
#    simplify_edges(edges)