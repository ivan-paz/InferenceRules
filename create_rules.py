"""
Function that take two rules (R1, R2)
if class R1 != class R2
for each parameter if partition is possible
create the resulting partition
it returns an array with the partition of each parameter.
"""

# import the necessary functions
from function_to_create_subsets import *

def conditions(t1, t2):
    #condition1
    set1 = set(t1)
    set2 = set(t2)
    print(set1.intersection(set2))
conditions((4,6),4)

def partitions(R1, R2):
    if R1[-1] != R2[-1]:
        for i in range(len(R1) - 1 ):
            print(R1[i],R2[i])
            conditions(R1[i],R2[i])

R1 = ((1,2,3,8,11), (4,6), 'A' )
R2 = (5, 4, 'B')
#partitions( R1, R2 )
