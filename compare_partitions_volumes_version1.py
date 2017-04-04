# -*- coding: utf-8 -*-
"""
Function that takes a set of sets of rules

e.g set1, set2, set3 . . .

and return the one with greater "volume"

"""
from functions_to_calculate_the_volume_of_a_partition import *
from copy import deepcopy

#def simplify_volume(volume):
 #   simplified = [ ]
  #  for i in volume:
   #     current = deepcopy(i)
    #    print('current',current)
     #   for j in volume:
      #      print('j',j)
       #     print('i,j:',i,j)
        #    if ( i != j ) and ( current[1] == j[1] ):
        #        current[0] = current[0] + j[0]
        #if current not in simplified:
        #    simplified = simplified + [current]
    #return simplified

def simplify_volume(volume):
    simplified = [ ]
    for i in range(len(volume)):
        current = deepcopy(volume[i])
        for j in range(len(volume)):
            if ( i != j ) and ( current[1] == volume[j][1] ):
                current[0] = current[0] + volume[j][0]
        if current not in simplified:
            simplified = simplified + [current]
    return simplified
#simplify_volume([[0, 0], [15, 1], [3, 1]])
#simplify_volume([[0, 0], [6, 1], [3, 1], [4, 2]])     
#simplify_volume([[0, 0], [4, 1], [4, 1]])

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
def max_of_entrance(list_same_volume_entrance, indexes):
    maximum = max(list_same_volume_entrance)
    #print('MAXIMUM',maximum)
    index_of_the_maximum = list_same_volume_entrance.index(maximum)#take the index of the first maximum 
    # this is the place to take all indexes and made a decsition
    #
    unique = 0
    for i in list_same_volume_entrance:
        if maximum > i:
            unique = unique + 1
    if unique == len(list_same_volume_entrance) - 1:
        index = list_same_volume_entrance.index(maximum)
        return index
    else:
        return index_of_the_maximum
#max_of_entrance([[4, 2], [4, 2], [4, 2]])
#max_of_entrance([[4, 1], [4, 1], [9, 1]])


#Compare volumes returns the index of the maximum volume
def compare_volumes(volumes_same_dimension,indexes,longitude):
    position = longitude
    for i in range(longitude):
        #print(position)
        position = position - 1
        array = take_entrance(volumes_same_dimension, position)
        #print(position, array)
        habemus_maximum = max_of_entrance(array, indexes)
        #print('habemus_maximum', habemus_maximum)
        if habemus_maximum != False:
            index_of_maximum_volume = habemus_maximum
            return indexes[habemus_maximum]
    return False
                               
#compare_volumes([[[0, 0], [4, 1], [4, 2]], [[0, 0], [4, 1], [4, 2]], [[0, 0], [9, 1], [4, 2]]], [0, 2, 3], 3)  
#compare_volumes([[[0, 0], [8, 1]], [[0, 0], [12, 1]], [[0, 0], [13, 1]], [[0, 0], [4, 1]], [[0, 0], [12, 1]], [[0, 0], [4, 1]], [[0, 0], [13, 1]]],[0, 1, 2, 3, 4, 5, 6],2)
"""
def max_volume(rule_sets):
    volumes = []
    for rule_set in rule_sets:
        volume = partition_volume(rule_set)
        volume = simplify_volume(volume)
        volumes.append(volume)
    print('volumes :', volumes)

    longitude = max_len(volumes)
    #print('longitude: ', longitude)    
    
    candidates = []
    indexes = []
    for i in range(len(volumes)):
        v = volumes[i]
        if len(v) == longitude:
            candidates.append(v)
            indexes.append(i)
    #print('candidates', candidates, 'indexes', indexes)
    index_of_partition_with_maximum_volume = compare_volumes(candidates,indexes,longitude)
    
    if index_of_partition_with_maximum_volume != False:
        return rule_sets[index_of_partition_with_maximum_volume]
    else:
        #     What to do????? THE RESULT DEPEND OF A RANDOM CHOISE !!!!!!!
        return rule_sets[0]
"""

#---------------------------------------------------
#   Version poker of volumes
#
def compare(vol1,vol2):
    if vol1[1] > vol2[1]:
        return 1
    elif vol1[1] < vol2[1]:
        return 2
    elif vol1[0] > vol2[0]:
        return 1
    elif vol1[0] < vol2[0]:
        return 2
    else:
        return 3

#print(compare([4,1],[3,1]))

def fight(winner, contendent):
    winner_copy = deepcopy(winner)
    contendent_copy = deepcopy(contendent)
    
    hand1 = winner[-1]
    hand2 = contendent[-1]
    result = 3

    while result == 3 and len(winner) > 0 and len(contendent) > 0:
        hand1 = winner[-1]
        del winner[-1]
        hand2 = contendent[-1]
        del contendent[-1]
        result = compare(hand1, hand2)
        if result == 1:
            return winner_copy
        if result == 2:
            return contendent_copy
        if result == 3:
            result = 3
    if result == 3:
        return winner_copy
    else:
        return result
#print( fight( [[0,0],[5,1],[4,2]], [[10,1],[4,2]]) )

#   POKER FUNCTION       
def max_volume(rule_sets):
    volumes = []
    #indexes = []
    #index = -1
    for rule_set in rule_sets:
        #index = index + 1
        volume = partition_volume(rule_set)
        volume = simplify_volume(volume)
        volumes.append(volume)
     #   indexes.append(index)
    print('volumes :', volumes)
    volumes_copy = deepcopy(volumes)
    winner = volumes[0]

    for i in range(1, len(volumes) ):
        contendent = volumes[i]
        print(winner, contendent)
        result = fight(winner, contendent)
        print('RESULT', result)
        if result == winner:
            winner = winner
        elif result == contendent:
            winner = contendent
        else:
            winner = winner
    print('RESULT', result)
    print('VOLUMES  copy ', volumes_copy)
    index_of_partition_with_max_volume = volumes_copy.index(result)
    return rule_sets[index_of_partition_with_max_volume]

#max_part = max_volume([[[(1, 2, 3), (4, 6), 'A'], [(5,), (4, 5), 'B'], [(8,), (4, 6), 'A'], [(9,), 5, 'C'], [(11,), (4, 6), 'A'], [(12,), 5, 'C']], [[(1, 2, 3), (4,), 'A'], [(5,), (4, 5), 'B'], [(8, 11), (4,), 'A'], [(9, 12), (5,), 'C'], [(1, 2, 3, 8, 11), (6,), 'A']], [[(8,), (4, 6), 'A'], [(9,), 5, 'C'], [(11,), (4, 6), 'A'], [(12,), 5, 'C'], [(1, 2, 3), (4, 6), 'A'], [(5,), (4, 5), 'B']], [[(8, 11), (4,), 'A'], [(9, 12), (5,), 'C'], [(8, 11), (6,), 'A'], [(1, 2, 3), (4, 6), 'A'], [(5,), (4, 5), 'B']]])
#print(max_part)
#max_volume(leafs)

"""
Test1

leafs = [
[[(1, 2, 3), (4, 6), 'A'], [(5,), 4, 'B'], [(8,), (4, 6), 'A'], [(9,), 5, 'C'], [(11,), (4, 6), 'A'], [(12,), 5, 'C']],
[[(1, 2, 3), (4,), 'A'], [(5,), 4, 'B'], [(8, 11), (4,), 'A'], [(9, 12), (5,), 'C'], [(1, 2, 3, 8, 11), (6,), 'A']],
[[(8,), (4, 6), 'A'], [(9,), 5, 'C'], [(11,), (4, 6), 'A'], [(12,), 5, 'C'], [(1, 2, 3), (4, 6), 'A'], [(5,), 4, 'B']],
[[(8, 11), (4,), 'A'], [(9, 12), (5,), 'C'], [(8, 11), (6,), 'A'], [(1, 2, 3), (4, 6), 'A'], [(5,), 4, 'B']]
]
max_volume(leafs)

#--------------------------------
Test 2

max_volume(leafs)

leafs = [
[[(6,), (4, 6), 'A'],
  [(7,), 5, 'B'],
  [(10,), (4, 6), 'A'],
  [(12,), 5, 'B'],
  (8, (3, 7), 'A')],
 [[(7,), (5,), 'B'],
  [(8,), (3, 7), 'A'],
  [(12,), (5,), 'B'],
  [(6, 10), (4,), 'A'],
  [(6, 10), (6,), 'A']],
 [[8, (3,), 'A'],
  [(7, 12), (5,), 'B'],
  [8, (7,), 'A'],
  [(6, 10), (4,), 'A'],
  [(6, 10), (6,), 'A']],
 [[(6,), (4, 6), 'A'],
  [(7,), 5, 'B'],
  [(10,), (4, 6), 'A'],
  [(8,), (3, 7), 'A'],
  [(12,), 5, 'B']],
 [[(6, 10), (4,), 'A'],
  [(7,), (5,), 'B'],
  [(6, 10), (6,), 'A'],
  [(8,), (3, 7), 'A'],
  [(12,), 5, 'B']],
 [[(6,), (4, 6), 'A'],
  [(7,), (5,), 'B'],
  [(10,), (4, 6), 'A'],
  [(12,), (5,), 'B'],
  [8, (3,), 'A'],
  [8, (7,), 'A']],
 [[(6, 10), (4,), 'A'],
  [(7, 12), (5,), 'B'],
  [(6, 10), (6,), 'A'],
  [8, (3,), 'A'],
  [8, (7,), 'A']]]
  
#Check volume of independent partitions
  partition_volume([[(6,), (4, 6), 'A'],
  [(7,), 5, 'B'],
  [(10,), (4, 6), 'A'],
  [(8,), (3, 7), 'A'],
  [(12,), 5, 'B']])

"""
