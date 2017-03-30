#---------------------------------------------------------------
#
#   This script recives a new instance and modify accordingly the existent rule base
#
#----------------------------------------------------------------

#  When a new instance "new_instance" comes,
#  in order to adjust only what is necessary we proceed as follows:

#  1. Find which of the original connected sets are intersected by the new instance.
#  2. Separate those sets and keep the rules that come from the others.

import json
from splitR_version1 import *  #  CURRENT VERSION  #
from optimum_partition_for_Q import *


# Function to read a json file ---------------------
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
def new( new_pattern, all_connected_sets ):
    indexes_of_intersected_sets = [ ]
    intersected_sets = []
    index_counter = -1
    for connected_set in all_connected_sets:
        index_counter += 1
        include_set = False
        for rule in connected_set:
            print(new_pattern, rule)
            intersects = intersection(new_pattern, rule)
            print(intersects)
            if intersects == True:
                include_set = True
                print(index_counter)
        if include_set == True:
            indexes_of_intersected_sets.append(index_counter)
            intersected_sets.append(connected_set)
    return [intersected_sets,  indexes_of_intersected_sets]


#   NEW INSTANCE 
pattern = ( 2, 5, 'A' )

[ intersected_sets,  indexes_of_intersected_sets ] = new( pattern, all_connected_sets)

#Create new set with the new pattern + its intersections
def pattern_plus_intersections(pattern, intersected_sets):
        new_set = []
        for intersected_set in intersected_sets:
            for rule in intersected_set:
                new_set.append(rule)
        new_set.append(pattern)
        return new_set

print(pattern_plus_intersections(pattern, intersected_sets) )

#------------------------------------------------------------------------------------
#
#                           Exclude from optimim partitions
#                           the indexes_of_intersected_sets
#                           keep the rest of the partitions
#------------------------------------------------------------------------------------
optimum_partitions = read('optimum_partitions.json')
optimum_partitions_indexes = read('connected_rules_indexes.json')  #  They share indexes
lonly_rules = read('lonly_rules.json')
lonly_rules_indexes = read('lonly_rules_indexes.json')

#  compare the indexes of optimum partitions (partitions for the connected rules)  and lonly rules
#  with the indexes of the intersected sets
#  if they match eliminate the entrance either in optimim_partitions of in lonly_rules
#  return a final set without the excluded sets
def keep_partitons(optimum_partitions, optimum_partitions_indexes, lonly_rules, lonly_rules_indexes, indexes_of_intersected_sets):
    keep = []











