# -*- coding: utf-8 -*-
from adjacent_matrix import *
#from create_partitions_from_connected_component import *
from function_to_create_subsets import *
from create_rules import *
from functions_to_calculate_the_volume_of_a_partition import *
#from intersection_of_rules import *
#from generate_edges import *
from break_edges import *
from tree import *
from compare_partitions_volumes import *

#--------------------------------------------
#    This function takes a set of rules and
#    returns the partition with higher volume
#--------------------------------------------
def optimum_partition(Q):
    [d, leafs] = tee(Q)
    if leafs != []:
        return max_volume(leafs)
    else:
        if d != {}:
            return d['1,1']
        else:
            return False #There is no partition to do. Probably the connected set has the same class.

"""
Example:

connected_rules = [
    [(5, 4, 'B'), ((1, 2, 3, 8, 11), (4, 6), 'A'), ((9, 12), 5, 'C')],
    
    [((6, 9), 11, 'A'), (8, (10, 14), 'A')],
     
    [(12, (10, 13), 'B'), ((11, 13), (11, 13), 'D')]
    ]

Q = [(5, 4, 'B'), ((1, 2, 3, 8, 11), (4, 6), 'A'), ((9, 12), 5, 'C')]
optimum_partition(Q)


Q = [((6, 9), 11, 'A'), (8, (10, 14), 'A')]
optimum_partition(Q)


Q = [(12, (10, 13), 'B'), ((11, 13), (11, 13), 'D')]
optimum_partition(Q)
"""










