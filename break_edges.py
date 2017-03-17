# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 16:25:56 2017

@author: ivan
"""

from adjacent_matrix import *
from create_partitions_from_connected_component import *

from function_to_create_subsets import *
from create_rules import *

from functions_to_calculate_the_volume_of_a_partition import *

from intersection_of_rules import *

from generate_edges import *

Q = [
        ( (1,2,3,8,11), (4,6), 'A'),
        (       (9,12),     5, 'C'),
        (            5,     4,'B')    
    ]
   
matrix = adjacent_matrix(Q)
edges = generate_edges(matrix)
edges = simplify_edges(edges)

for i in edges:
    print(i)
    print(i[0])

partitions(( (1,2,3,8,11), (4,6), 'A'),(       (9,12),     5, 'C'))

partition_volume([[(1, 2, 3, 8, 11), (4,), 'A'],
  [(9, 12), (5,), 'C'],
  [(1, 2, 3, 8, 11), (6,), 'A']])

intersection(( (1,2,3,8,11), (4,6), 'A'),(       (9,12),     5, 'C'))