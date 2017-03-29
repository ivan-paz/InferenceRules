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

# Function to read a json file
def read(file_name):
    with open(file_name) as json_data:
        file_content = json.load(json_data)
        return file_content

# Read files with all_connected_sets and their indexes
all_connected_sets = read('all_connected_sets.json')
indexes_all_connected_sets = read('indexes_connected_sets.json')

#for i in all_connected_sets: print(i)

#Find wich of the original connected_sets are intersected by the new instance
def new( new_pattern, all_connected_sets, indexes_all_connected_sets):
    indexes_of_intersected_sets = [ ]
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
    return indexes_of_intersected_sets

# I need two thinks
# which sets are removed from the original

matrices = new( (2, 5,'A'), all_connected_sets, indexes_all_connected_sets)
print(matrices)




"""
with open('strings.json') as json_data:
    d = json.load(json_data)
    print(d)
"""
