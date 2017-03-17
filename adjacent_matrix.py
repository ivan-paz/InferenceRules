# -*- coding: utf-8 -*-
from intersection_of_rules import *

"""
R = [
( (1, 2, 3, 8, 11), (4, 6), 'A'),
( (9,12),            5,     'C'),
(     5,             4,     'B'),
( (2,5),             7,     'D')
]
"""
def adjacent_matrix(R):
    graph = {}
    for i in range( len(R) ):
        graph[str(i)] =  [ ]    
        for j in range( len(R) ):
            if ( i != j ) and intersection ( R[i], R[j] ) == True:
                #print(R[i], R[j])
                old = graph[str(i)]
                new = old + [str(j)]
                graph[str(i)] = new
    return graph

#   adjacent_matrix(R)

"""
in this graph
R0 is connected with R1 and R2
R1 is connected with R0
R2 is connected with R0
R3 has no connections
"""
"""
graph = {}

for i in range( len(R) ):
    graph[str(i)] =  [ ]
    for j in range( len(R) ):
        if ( i != j ) and intersection ( R[i], R[j] ) == True:
            #print(R[i], R[j])
            old = graph[str(i)]
            new = old + [str(j)]
            graph[str(i)] = new
print(graph)
"""