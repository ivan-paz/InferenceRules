#---------------------------------------------------------------
#
#   This script contains the functions to
#   receive a new pattern and modify
#   according the existent rule base.
#
#   To avoid unnecessary processing,
#   the function " intersected_connected_sets "
#   find which of the original connected sets
#   are intersected by the new pattern.
#   
#  Those connected sets together with the new pattern
#  form a " new (connected) set" which will be cut
#  following the maximum volume heuristic
#
#  The resulting rule base is build with the partition
#  of the new connected_set + the partitions comming from
#  the not_intersected connected sets.
#
#----------------------------------------------------------------

import json
from splitR_version1 import *  #  CURRENT VERSION  #
from optimum_partition_for_Q import *


# Read a json file ---------------------
def read(file_name):
    with open(file_name) as json_data:
        file_content = json.load(json_data)
        return file_content
#---------------------------------------------------
# Read files with all_connected_sets and their indexes
all_connected_sets = read('all_connected_sets.json')
#indexes_all_connected_sets = read('indexes_connected_sets.json')
#for i in all_connected_sets: print(i)


# Find wich of the original connected_sets are intersected by the new instance
# get its indexes
def intersected_connected_sets( new_pattern, all_connected_sets ):
    indexes_of_intersected_sets = [ ]
    intersected_sets = []
    index_counter = -1
    for connected_set in all_connected_sets:
        index_counter += 1
        include_set = False
        for rule in connected_set:
            #print(new_pattern, rule)
            intersects = intersection(new_pattern, rule)
            #print(intersects)
            if intersects == True:
                include_set = True
                #print(index_counter)
        if include_set == True:
            indexes_of_intersected_sets.append(index_counter)
            intersected_sets.append(connected_set)
    return [intersected_sets,  indexes_of_intersected_sets]


#   NEW INSTANCE 
#pattern = ( 2, 5, 'A' )

#[ intersected_sets,  indexes_of_intersected_sets ] = intersected_connected_sets( pattern, all_connected_sets)

#Create new set with the new pattern + its intersections
def pattern_plus_intersections(pattern, intersected_sets):
        new_set = []
        for intersected_set in intersected_sets:
            for rule in intersected_set:
                new_set.append(rule)
        new_set.append(pattern)
        return new_set

#print('This is the set to cut : ' )
#new_set = pattern_plus_intersections(pattern, intersected_sets)
#print(new_set)

#print('This is the set without inconsistencies among the rules: ')
#new_set = optimum_partition( new_set )
#print(new_set)

#------------------------------------------------------------------------------------
#                           Exclude from optimim partitions
#                           the indexes_of_intersected_sets
#                           keep the rest of the partitions
#------------------------------------------------------------------------------------
optimum_partitions = read('optimum_partitions.json')
optimum_partitions_indexes = read('connected_rules_indexes.json')  #  They share indexes
lonly_rules = read('lonly_rules.json')
lonly_rules_indexes = read('lonly_rules_indexes.json')

#print('------------------')
#print('indexes of intersected sets :  ' , indexes_of_intersected_sets)
#print('optimum_partitions_indexes',optimum_partitions_indexes)
#print('lonly_rules_indexes', lonly_rules_indexes)


#  compare the indexes of optimum partitions (partitions for the connected rules) and lonly rules
#  with the indexes of the intersected sets
#  if they match, eliminate the entrance either in the optimim_partitions of in the lonly_rules
#  return as final set {lonly_rules, optimum_partitions}\{elements_at_indexes_of_intersected_rules}
def remaining_partitions(optimum_partitions, optimum_partitions_indexes, lonly_rules, lonly_rules_indexes, indexes_of_intersected_sets):
    kept_partitions = []
    kept_lonly = []

    for i in range( len(optimum_partitions_indexes) ):
        index = optimum_partitions_indexes[i]
        flag = index in indexes_of_intersected_sets
        if flag == False:
            kept_partitions = kept_partitions + optimum_partitions[i]

    for i in range( len(lonly_rules_indexes) ):
        index = lonly_rules_indexes[i]
        flag = index in indexes_of_intersected_sets
        if flag == False:
            kept_lonly.append(lonly_rules[i])
    return [ kept_partitions, kept_lonly]

#print( 'REMAINING PARTITIONS : ')

#not_intersected = remaining_partitions(optimum_partitions, optimum_partitions_indexes, lonly_rules, lonly_rules_indexes, indexes_of_intersected_sets)
#print(not_intersected)

#---------------------------------------------------------------
#    The resulting rule base incorporating the new parrern
#    is the set { remaining_partitions U new_set }
#
#---------------------------------------------------------------
def not_intersected_union_new_set(not_intersected, new_set):
    union = []
    for i in not_intersected:
        for j in i: union = union + j
    for i in new_set:
        union.append(i)
    return union
#print('result: ')
#print( not_intersected_union_new_set(not_intersected, new_set) )

#-----------------------------------------------------------------
#
#           PROCESS  ---   NEW  ---  PATTERN
#
#-----------------------------------------------------------------
def process_new_pattern(pattern):
    all_connected_sets = read('all_connected_sets.json')
    [intersected_sets, indexes_of_intersected_sets] = intersected_connected_sets(pattern, all_connected_sets)
    new_set = pattern_plus_intersections(pattern,intersected_sets)
    new_set = optimum_partition( new_set)
    
    optimum_partitions = read('optimum_partitions.json')
    optimum_partitions_indexes = read('connected_rules_indexes.json')
    lonly_rules = read('lonly_rules.json')
    lonly_rules_indexes = read('lonly_rules_indexes.json')

    not_intersected = remaining_partitions(optimum_partitions, optimum_partitions_indexes, lonly_rules, lonly_rules_indexes,indexes_of_intersected_sets)
    
    new_rule_base = not_intersected_union_new_set(not_intersected,new_set)
    return new_rule_base

#  pattern = ( 2,  5,  'A' )
#  print('new rule base: ', process_new_pattern(pattern))










