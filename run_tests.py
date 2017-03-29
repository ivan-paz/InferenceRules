# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 11:15:44 2017

@author: ivan
"""

# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
#        This script takes a rule base R
#        in which rules have the following form:
#     values paramater 1   values param 2       class
#        ( (9,12),                  5,           'C'),
#
#   Then, function all_connected_sets separates the rules into connected (intersected) components
#   Those components are separated in those with only one rule: lonly_rules
#   and those with more than one rule: connected_rules
#
#   Then, for each set in connected_rules the function extract_optimum_partition
#   breaks each set fo rules in such a way that, if the intervals between the maximum and minumum
# values of each parameter for each rule are consider as valid intervals for the class of the rule
#    there would not be contradictions between the rules
#-----------------------------------------------------------------------
from splitR import *
from optimum_partition_for_Q import *

def print_list(some_list):
    for i in some_list:
        print(i)

# Consider the following rule base:
R = [
#connected 1
( (1, 2, 3, 8, 11), (4, 6), 'A'),
(     5,             4,     'B'),
( (9,12),            5,     'C'),
#connected 2

( (2,5),             7,     'D'),

#connected 3
(20,                 20,    'D'),

#connected 4
( (12),            (10,13), 'B'),
( (11,13),          (11,13),'D'),
#connected 5
(   8,             (10,14), 'A'),
(  (6,9),            11,    'A')
]
print('Rules test 1')
print_list(R)
print('--------------------------------------------------')
# Separate R into its connected components
all_connected_sets = extract_connected_sets( R )
print('all connected sets : ')
print_list(all_connected_sets)
#Separate the connected components into lonly rules and connected components
#with more than one rule
[ lonly_rules, connected_rules ] = connected_and_lonly_rules( all_connected_sets )
#Create the optimim partition for each connected component with more than one rule
optimum_partitions = extract_optimum_partitions( connected_rules )
#Put again all the rules together
rules = put_rules_together( optimum_partitions, lonly_rules )
print('Set of rules from which inference rules can be derived: ')
for rule in rules:
    print(rule)
#Check that there are no intersections among the resulting rules
adjacent_matrix( rules )


# Test 2
print('Test 2')
R = [
        ((1,2,3,8,11),(4,6),'A'),
        (5,4,'B')
        ]
all_connected_sets = extract_connected_sets(R)
print_list(all_connected_sets)
[lonly_rules, connected_rules] = connected_and_lonly_rules(all_connected_sets)
print(lonly_rules,connected_rules)
optimum_partitions = extract_optimum_partitions(connected_rules)
print(optimum_partitions)

#----------------------------------------------------------
#         Test 3
#    Intersection of two rules of the same class
#    with another rule of different class
#----------------------------------------------------------


print( ' Test  3 ' )
R = [
        ((6,10),(4,6),'A'),
        (    8, (3,7),'A'),
        ((7,12),   5, 'B')
        ]
all_connected_sets = extract_connected_sets(R)

[lonly_rules, connected_rules] = connected_and_lonly_rules(all_connected_sets)


optimum_partitions = extract_optimum_partitions( connected_rules )

print_list( optimum_partitions)

#Detailed view
[  d,leafs  ] = tee(R)

for i in leafs:
    print(partition_volume(i))



#root = cut(R)
"""
Out[6]: 
[[[(6,), (4, 6), 'A'],
  [(7,), 5, 'B'],
  [(10,), (4, 6), 'A'],
  [(12,), 5, 'B'],
  (8, (3, 7), 'A')], # Branch 1
 [[(6, 10), (4,), 'A'],
  [(7, 12), (5,), 'B'],
  [(6, 10), (6,), 'A'],
  (8, (3, 7), 'A')], #Branch 2
 [[(7,), 5, 'B'],
  [(8,), (3, 7), 'A'],
  [(12,), 5, 'B'],
  ((6, 10), (4, 6), 'A')], #Branch 3
 [[8, (3,), 'A'],
  [(7, 12), (5,), 'B'],
  [8, (7,), 'A'],
  ((6, 10), (4, 6), 'A')] #Branch 4
  ]
"""

branch1 = cut([[(6,), (4, 6), 'A'],
  [(7,), 5, 'B'],
  [(10,), (4, 6), 'A'],
  [(12,), 5, 'B'],
  (8, (3, 7), 'A')])
#  []
branch2 = cut(
 [[(6, 10), (4,), 'A'],
  [(7, 12), (5,), 'B'],
  [(6, 10), (6,), 'A'],
  (8, (3, 7), 'A')])
  
branch21 = cut([[(7,), (5,), 'B'],
  [(8,), (3, 7), 'A'],
  [(12,), (5,), 'B'],
  [(6, 10), (4,), 'A'],
  [(6, 10), (6,), 'A']])
#  []
branch22 = cut([[8, (3,), 'A'],
  [(7, 12), (5,), 'B'],
  [8, (7,), 'A'],
  [(6, 10), (4,), 'A'],
  [(6, 10), (6,), 'A']])

branch3 = cut ( [[(7,), 5, 'B'],
  [(8,), (3, 7), 'A'],
  [(12,), 5, 'B'],
  ((6, 10), (4, 6), 'A')])
branch31 = cut([[(6,), (4, 6), 'A'],
  [(7,), 5, 'B'],
  [(10,), (4, 6), 'A'],
  [(8,), (3, 7), 'A'],
  [(12,), 5, 'B']])
  
branch32= cut([[(6, 10), (4,), 'A'],
  [(7,), (5,), 'B'],
  [(6, 10), (6,), 'A'],
  [(8,), (3, 7), 'A'],
  [(12,), 5, 'B']])

branch4 = cut([[8, (3,), 'A'],
  [(7, 12), (5,), 'B'],
  [8, (7,), 'A'],
  ((6, 10), (4, 6), 'A')])

branch41 = cut([[(6,), (4, 6), 'A'],
  [(7,), (5,), 'B'],
  [(10,), (4, 6), 'A'],
  [(12,), (5,), 'B'],
  [8, (3,), 'A'],
  [8, (7,), 'A']])

branch42 = cut([[(6, 10), (4,), 'A'],
  [(7, 12), (5,), 'B'],
  [(6, 10), (6,), 'A'],
  [8, (3,), 'A'],
  [8, (7,), 'A']])


