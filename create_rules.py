"""
Function that take two rules (R1, R2)
if class R1 != class R2
for each parameter, if partition is possible
create the resulting partition
it returns an array with the partition of each parameter.
"""

# import the necessary functions
from function_to_create_subsets import *
import copy
"""

"""
def condition(t1, t2):
    #Ckeck if t1 and t2 intersect
    set1 = set()
    set2 = set();
    if type(t1) == int or type(t1)== float:
        set1.add(t1)
    else:
        for x in t1: set1.add(x)
    if type(t2) == int or type(t2)== float:
        set2.add(t2)
    else:
        for y in t2: set2.add(y)
    if len(set1.intersection(set2)) != 0:
        return True
    else:
        return False
#condition( (4,6), 4 )
#condition((1,2,3,8,11),(9,12))

def rules_form_subsets(subsets, i, R1, R2):
    rules = [ ]
    R1 = list(R1)
    R2 = list(R2)
    for j in range(len(subsets)):
        if j%2 != 0:
            #print(subsets[j],subsets[j-1])
            if subsets[j] == 0:
                rule = copy.deepcopy(R1)
                rule[i] = tuple(subsets[ j - 1 ])
                rules = rules + [rule]
            else:
                rule = copy.deepcopy(R2)
                rule[i] = tuple(subsets[ j - 1 ])
                rules = rules + [rule]
    return rules
#rules_form_subsets([[1, 2, 3], 0, [5], 1, [8, 11], 0], 0, R1, R2)

def partitions(R1, R2):
    partitions = [ ]
    if R1[-1] != R2[-1]:
        for i in range(len(R1) - 1 ):
            #print(R1[i],R2[i])
            if condition(R1[i],R2[i]) == False:
                subsets = create_subsets(R1[i],R2[i])
                rules = rules_form_subsets(subsets, i, R1, R2)
                partitions = partitions + [rules]
        return partitions
    else:
        return False

#R1 = ( (1,2,3,8,11), (4,6), 'A' )
#R2 = ( 5, 4, 'B')
#partitions( R1, R2 )



#R1 = ((9,12), 5, 'C')
#R2 = ( (1,2,3,8,11), (4,6), 'A' )
#partitions( R1, R2 )
