# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 16:25:56 2017

@author: ivan
"""
from adjacent_matrix import *
#from create_partitions_from_connected_component import *
from function_to_create_subsets import *
from create_rules import *
from functions_to_calculate_the_volume_of_a_partition import *
#from intersection_of_rules import *
from generate_edges import *

def exclude_current_edge(edge,edges):
    temp = copy.deepcopy(edges)
    temp.remove(edge)
    return temp
"""
Q = [
        ( (1,2,3,8,11), (4,6), 'A'),
        (       (9,12),     5, 'C'),
        (            5,     4,'B')    
    ]
"""    
    
def cut(Q):
    matrix = adjacent_matrix(Q)
    edges = generate_edges(matrix)
    edges = simplify_edges(edges)
    for i in range(len(edges)): edges[i] = sorted(edges[i])
    edges = sorted(edges, key = operator.itemgetter(1))
  
    P = [ ]
    for edge in edges:
        print('breaking',edge)
        temp_P = [ ]
        #print( Q[ int(edge[0]) ], Q[ int(edge[1]) ] )
        temp_P = temp_P + partitions( Q[ int(edge[0]) ], Q[ int(edge[1]) ]  )
        #print(temp_P)
        clone_Q = copy.deepcopy(Q)
        clone_Q.remove(Q[int(edge[0])])
        clone_Q.remove(Q[int(edge[1])])
        #print('clone_Q', clone_Q)
        
        for p in temp_P:
            for x in clone_Q:
                p.append(x)
            #print('p: ',p)
            P.append(p)#########  Eliminate levels Rompe la herarquia
    return P
#   P = cut(Q)



"""
#           PROVES

Q = [((6, 9), 11, 'A'), (8, (10, 14), 'A')]
cut(Q)
matrix
edges
edges = simplify_edges(edges)
for i in range(len(edges)):
    edges[i] = sorted(edges[i])
    edges = sorted(edges, key = operator.itemgetter(1))
edges

partitions(Q[0],Q[1])
#---------------------------------
def cut(Q):
    matrix = adjacent_matrix(Q)
    edges = generate_edges(matrix)
    edges = simplify_edges(edges)
    for i in range(len(edges)): edges[i] = sorted(edges[i])
    edges = sorted(edges, key = operator.itemgetter(1))
  
    P = [ ]
    for edge in edges:
        print('breaking',edge)
        temp_P = [ ]
        #print( Q[ int(edge[0]) ], Q[ int(edge[1]) ] )
        if partitions( Q[ int(edge[0]) ], Q[ int(edge[1]) ]  ) != False:
            temp_P = temp_P + partitions( Q[ int(edge[0]) ], Q[ int(edge[1]) ]  )
        #print(temp_P)
            clone_Q = copy.deepcopy(Q)
            clone_Q.remove(Q[int(edge[0])])
            clone_Q.remove(Q[int(edge[1])])
        else:
            P = False
        #print('clone_Q', clone_Q)
        if P != False:
            for p in temp_P:
                for x in clone_Q:
                    p.append(x)
                #print('p: ',p)
                P.append(p)#########  Eliminate levels Rompe la herarquia
        else:
            P = Q
    return P
#   P = cut(Q)
"""







"""


def iterate(Q):
    conjuntos = cut(Q)
    
    nuevos_conjuntos = []
    flag = True
    while flag == True:
        flag = False
        for conjunto in conjuntos:
            temp = cut(conjunto)
            print(temp)
            for i in temp:
                print('iiiii: ', i)
                if i != []:
                    flag = True
                    nuevos_conjuntos.append(i)
            print('nuevos conjuntos',nuevos_conjuntos)
        conjunto = nuevos_conjuntos

iterate(Q)


#Q is a connected set


Q = [
        ( (1,2,3,8,11), (4,6), 'A'),
        (       (9,12),     5, 'C'),
        (            5,     4,'B')    
    ]
def cut(Q):
    matrix = adjacent_matrix(Q)
    edges = generate_edges(matrix)
    edges = simplify_edges(edges)
    for i in range(len(edges)): edges[i] = sorted(edges[i])
    edges = sorted(edges, key = operator.itemgetter(1))
    
    P = [ ]
    for edge in edges:
        print('breaking',edge)
        temp_P = [ ]
        #print( Q[ int(edge[0]) ], Q[ int(edge[1]) ] )
        temp_P = temp_P + partitions( Q[ int(edge[0]) ], Q[ int(edge[1]) ]  )
    
        other_edges = exclude_current_edge(edge,edges)
        x = [ ]
        for edge1 in other_edges:
                x.append( Q[ int(edge1[1]) ] )
                #print('x',x)
                
        for item in temp_P:
            for rule in x:
                item.append(rule)
            P.append(item)
    return P

P = cut(Q)  #   return all possible cut of the conected rules.
#  first branch
Q = [[(1, 2, 3, 8), (4, 6), 'A'],
  [(9,), 5, 'C'],
  [(11,), (4, 6), 'A'],
  [(12,), 5, 'C'],
  (5, 4, 'B')]
  
Q = [[(1, 2, 3), (4, 6), 'A'], [(5,), 4, 'B'], [(8,), (4, 6), 'A']]
#-----------------------------------------------------------------------------

#For each cut

n = [
  [(1, 2, 3, 8), (4, 6), 'A'],
  [(9,), 5, 'C'],
  [(11,), (4, 6), 'A'],
  [(12,), 5, 'C'],
  (5, 4, 'B')
  ]
def separate(n):
    matrix = adjacent_matrix(n)
    independent_rules = [ ]
    values = matrix.values()

    indexes = []
    for i in values:
        if len(i)>0:
            for j in i:
                indexes.append(int(j))

    for i in range(len(n)):
        if i not in indexes:
            independent_rules.append(n[i])
    for i in independent_rules:
        n.remove(i)
    return [n,independent_rules]


1) 

P[2]

[new, independent_rules] = separate([[(1, 2, 3), (4, 6), 'A'],
 [(5,), 4, 'B'],
 [(8, 11), (4, 6), 'A'],
 ((9, 12), 5, 'C')])
new = [[(8, 11), (4, 6), 'A'], ((9, 12), 5, 'C')]

independent_rules = [[(1, 2, 3), (4, 6), 'A'], [(5,), 4, 'B']]

new = cut([[(8, 11), (4, 6), 'A'], ((9, 12), 5, 'C')])
new

[
[[(8,), (4, 6), 'A'], [(9,), 5, 'C'], [(11,), (4, 6), 'A'],[(12,), 5, 'C']],
 [[(8, 11), (4,), 'A'], 
 [(9, 12), (5,), 'C'], [(8, 11), (6,), 'A']]
  ]

[new, independent_rules] = separate(new)




Q = [
        ( (1,2,3,8,11), (4,6), 'A'),
        (       (9,12),     5, 'C'),
        (            5,     4,'B')    
    ]
    

P = cut(Q)
new = P[2]

I = []
while len(new) > 0:
    [new,independent_rules] = separate(new)
    I.append(independent_rules)
    new = cut(new)
I
#----------------------------------------------------

Q = [
        ( (1,2,3,8,11), (4,6), 'A'),
        (       (9,12),     5, 'C'),
        (            5,     4,'B')    
    ]

def all_partitions(Q):
    P = cut(Q)
    for p in P:
        new = copy.deepcopy(p)
        print('new: ', new)
        I = []
        while len(new)>0:
            [new, independent_rules] = separate(new)
            I.append(independent_rules)
            new = cut(new)
            print(I)
all_partitions(Q)



#Given a tuple, integer or float returns the maximum and minimum values
def interval(element):
    if type(element)==int:
        minimum = element
        maximum = element
    elif type(element)==float:
        minimum = element
        maximum = element
    elif type(element)==str:
        minimum = float(element)
        maximum = float(element)
    else:
        temp = []
        for i in a:
            temp.append(float(i))
        element = temp
        minimum = min(element)
        maximum = max(element)
    #print(minimum,maximum)
    return (minimum,maximum)

interval(('1','4'))




partitions(( (1,2,3,8,11), (4,6), 'A'),(       (9,12),     5, 'C'))
partition_volume([[(1, 2, 3, 8, 11), (4,), 'A'],
  [(9, 12), (5,), 'C'],
  [(1, 2, 3, 8, 11), (6,), 'A']])
intersection(( (1,2,3,8,11), (4,6), 'A'),(       (9,12),     5, 'C'))
"""