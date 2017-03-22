# -*- coding: utf-8 -*-
"""
Function that takes a set of sets of rules

e.g set1, set2, set3 . . .

and return the one with greater "volume"

"""
from functions_to_calculate_the_volume_of_a_partition import *
from copy import deepcopy

def simplify_volume(volume):
    simplified = [ ]
    for i in volume:
        current = deepcopy(i)
        for j in volume:
            if (i!=j) and (i[1] == j[1]):
                current[0] = current[0] + j[0]
        if current not in simplified:
            simplified = simplified + [current]
    return simplified       

#simplify_volume([[0, 0], [15, 1], [3, 1]])
#simplify_volume([[0, 0], [6, 1], [3, 1], [4, 2]])        

def max_len(volumes):
    max_len = 0
    for v in volumes:
        current_len = len(v)
        if current_len > max_len:
            max_len = current_len
    return max_len

def take_entrance(volumes,position):
    array = []    
    for v in volumes:
        array.append(v[position])
    return array
#take_entrance([[[0, 0], [4, 1], [4, 2]], [[0, 0], [4, 1], [4, 2]], [[0, 0], [9, 1], [4, 2]]], 0)

"""
this function find if there is one maximum or
if there are two partitions with the same volume
"""
def max_of_entrance(list_same_volume_entrance):
    maximum = max(list_same_volume_entrance)
    unique = 0
    for i in list_same_volume_entrance:
        if maximum > i:
            unique = unique + 1
    if unique == len(list_same_volume_entrance) - 1:
        index = list_same_volume_entrance.index(maximum)
        return index
    else:
        return False
#max_of_entrance([[4, 2], [4, 2], [4, 2]])
#max_of_entrance([[4, 1], [4, 1], [9, 1]])


def compare_volumes(volumes_same_dimension,indexes,longitude):
    position = longitude
    for i in range(longitude):
        #print(position)
        position = position - 1
        array = take_entrance(volumes_same_dimension, position)
        #print(position, array)
        habemus_maximum = max_of_entrance(array)
        if habemus_maximum != False:
            index_of_maximum_volume = habemus_maximum
            return indexes[habemus_maximum]
    return False
                               
#compare_volumes([[[0, 0], [4, 1], [4, 2]], [[0, 0], [4, 1], [4, 2]], [[0, 0], [9, 1], [4, 2]]], [0, 2, 3], 3)    

def max_volume(rule_sets):
    volumes = []
    for rule_set in rule_sets:
        volume = partition_volume(rule_set)
        volume = simplify_volume(volume)
        volumes.append(volume)
    #print(volumes)
    longitude = max_len(volumes)
    #print(longitude)
    
    candidates = []
    indexes = []
    for i in range(len(volumes)):
        v = volumes[i]
        if len(v) == longitude:
            candidates.append(v)
            indexes.append(i)
    #print(candidates,indexes)
    index_of_partition_with_maximum_volume = compare_volumes(candidates,indexes,longitude)
    
    if index_of_partition_with_maximum_volume != False:
        return rule_sets[index_of_partition_with_maximum_volume]
    else:
        #     What to do????? THE RESULT DEPEND OF A RANDOM CHOISE !!!!!!!
        return rule_sets[0]
        
#
        #max_volume(leafs)

"""
leafs = [

[[(1, 2, 3), (4, 6), 'A'], [(5,), 4, 'B'], [(8,), (4, 6), 'A'], [(9,), 5, 'C'], [(11,), (4, 6), 'A'], [(12,), 5, 'C']],
[[(1, 2, 3), (4,), 'A'], [(5,), 4, 'B'], [(8, 11), (4,), 'A'], [(9, 12), (5,), 'C'], [(1, 2, 3, 8, 11), (6,), 'A']],
[[(8,), (4, 6), 'A'], [(9,), 5, 'C'], [(11,), (4, 6), 'A'], [(12,), 5, 'C'], [(1, 2, 3), (4, 6), 'A'], [(5,), 4, 'B']],
[[(8, 11), (4,), 'A'], [(9, 12), (5,), 'C'], [(8, 11), (6,), 'A'], [(1, 2, 3), (4, 6), 'A'], [(5,), 4, 'B']]

]
"""