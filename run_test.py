

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


# Consider the following rule base: (Add here the rule base for the proves)
R = [( (1,2,3,8,11), (4,6), 'A'), (5, 4, 'B'), ( (9,12), 5, 'C')]
"""
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
"""

print('Rules test 1')
print_list(R)
print('--------------------------------------------------')
# Separate R into its connected components
all_connected_sets = extract_connected_sets( R )
print('All connected sets : ')
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

