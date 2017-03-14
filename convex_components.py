"""

Given a set of rules R
select a random rule and find all rules that intersect with it
then for each rule that intersects it
find all its intersections
repeat this process until no new intersections are found

To reduce, at each step the size of R and to avoid double comparisons,
when a rule is selected
it is eliminated from R

"""
from intersection_of_rules import *
from random_rule_intersections_and_difference import *

def convex_set(R):
    convex_set = [ ]
    index = 0
    [Q, R] = random_rule_with_intersections(R)
    print('set: ', Q, "\n", 'R : ', R)
    convex_set.append(Q)
    if len(convex_set[index])>1: #if rule has intersect with other rule   
        for rule in convex_set[index]:
            [Q, R] = search_intersections(rule,R)
            convex_set.append(Q)
        index = index + 1
    #print('R',R)
    #print('convex set: ',convex_set)
    #Put all intersections into a single array
    convex_set = collect_intersections(convex_set)
    return(convex_set, R)
#convex_set(R)

def collect_intersections(array):
    convex_set = []
    for i in array:
        for j in i:
            if j not in convex_set:
                convex_set.append(j)
    return convex_set
    
  

"""
specific cases to test the convex set function

"""
#-------------------------  TEST 1 -----------------------
# Example 1
R = [
( (1, 2, 3, 8, 11), (4, 6), 'A'),
( (9,12),            5,     'C'),
(     5,             4,     'B'),
( (2,5),             7,     'D')
]
convex_set(R)    
#---------------------------------------------------------------
# Example 2
R = [
( (1, 2, 3, 8, 11), (4, 6), 'A'),
( (9,12),            5,     'C'),
(     5,             4,     'B'),
( (2,5),             7,     'D'),

( (12),            (10,13), 'B'),
((11,13),          (11,13),      'D')
]
#Example 3
R = [((1,3),6,'A'),(2,(4,8),'A')]




#-------------------------  TEST 2 -----------------------
R = [
#convex1
( (1, 2, 3, 8, 11), (4, 6), 'A'),
(     5,             4,     'B'),
( (9,12),            5,     'C'),
#convex2
( (2,5),             7,     'D'),
#convex3
( (12),            (10,13), 'B'),
( (11,13),          (11,13),'D'),
#convex4
(   8,             (10,14), 'A'),
(  (6,9),            11,    'A')
]
convex_set(R)  
#-------------------------  TEST 3 -----------------------
R = [
((1,3), 1, 'A'),
(2, (1,4), 'A'),
((1,4), 3, 'A'),
(4, (3,6), 'A'),
((3,5), 6, 'A'),
(5,(6,8), 'A'),
((4,7), 7, 'A')
]
convex_set(R)
#
#
#
"""
Function that takes R and return all convex sets
"""
def extract_convex_sets(R):
    convex_sets = []
    while len(R) > 0:
        [set_convex, R] = convex_set(R)
        print(set_convex)
        convex_sets.append(set_convex)
    return convex_sets

extract_convex_sets(R)













