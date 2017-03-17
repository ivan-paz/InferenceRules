"""
this function recibes a connected component Q
and creates all its possible partitions
"""
from function_to_create_subsets import *
from create_rules import *

Q = [
        ( (1,2,3,8,11), (4,6), 'A'),
        (       (9,12),     5, 'C'),
        (            5,     4,'B')    
    ]

def create_partitions(Q):
    print(Q)

create_partitions(Q)

