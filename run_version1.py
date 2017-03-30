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
import json
from splitR_version1 import * #CURRENT VERSION
from optimum_partition_for_Q import *


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
#--------------------------------------
#    Write json data
#--------------------------------------
def write(file_name,data):
    with open (file_name, 'w') as f:
        json.dump(data,f)
#--------------------------------------


print('Rules', R)
print('--------------------------------------------------')
# Separate R into its connected components
all_connected_sets = extract_connected_sets( R )

print('All connected sets : ')
for i in range (len(all_connected_sets)): print(i,all_connected_sets[i])

write('all_connected_sets.json', all_connected_sets)

# Separate the connected components into
# lonly rules and connected components
# with more than one rule
[ lonly_rules, lonly_rules_indexes, connected_rules, connected_rules_indexes ] = connected_and_lonly_rules( all_connected_sets )


print('lonly rules: ', lonly_rules)
print('lonly rules indexes: ', lonly_rules_indexes)
write('lonly_rules.json', lonly_rules)
write('lonly_rules_indexes.json',lonly_rules_indexes)
#print('connected rules: ', connected_rules)
#write('connected_rules.json', connected_rules)
#print('connected rules indexes: ', connected_rules_indexes)
write('connected_rules_indexes.json', connected_rules_indexes)


#Create the optimim partition for each connected component with more than one rule
optimum_partitions = extract_optimum_partitions( connected_rules )
write( 'optimum_partitions.json', optimum_partitions )

#Put again all the rules together
#rules = put_rules_together( optimum_partitions, lonly_rules )
#print('Set of rules from which inference rules can be derived: ')


#Check that there are no intersections among the resulting rules
#adjacent_matrix( rules )

