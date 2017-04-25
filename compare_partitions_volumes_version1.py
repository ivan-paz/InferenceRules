# -*- coding: utf-8 -*-
"""

Function that takes a set of sets of rules, each one corresponding
to a different partition of an original connected set

e.g set1, set2, set3 . . .

and return the set (partition) with greater "volume".


"""
from functions_to_calculate_the_volume_of_a_partition import *
from copy import deepcopy

#-------------------------------------------------------------
# This function takes a volume
# e.g [[0,0],[6,1],[3,1],[4,2]]
# (where in each [i,j] i is the "volume" and j the "dimension")
# and sum the entrances of same dimension
# in the example the result would be: [[0,1],[9,1],[4,2]]
#-------------------------------------------------------------
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


#-----------------------------------------------------------------
#       Version Poker of Volumes (or other desired property)
#-----------------------------------------------------------------

#-----------------------------------------------
# Function "compare" takes two single volumes
# that could have different volume and dimension
# [volume1, dimension1] [volume2, domension2]
# and returns the maximum considering volume
# and dimension.
#-----------------------------------------------
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

#-------------------------------------------------
#  This function takes two volumes (one beguins being the
#  winner and the other the contendent) that may have
#  different dimensions e.g [[0,0],[2,1],[2,4]] and [[3,1],[1,4]]
#  and returns:
#  1  if the winner has the bigger volume.
#  2  if the contendent has the bigger volume.
#  3  if they are tie .
#  They fight to see which one winns.
#-------------------------------------------------
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
#print(fight([[0,0],[1,2]],[[0,0]]))

#   POKER FUNCTION       
#   Best candidate
def max_volume(rule_sets):
    volumes = []  # SPECIFIC PROPERTY TO MAXIMIZE
    for rule_set in rule_sets:
        volume = partition_volume(rule_set)
        volume = simplify_volume(volume)
        volumes.append(volume)
    #COPIES
    print('Partitions volumes :', volumes)
    volumes_copy = deepcopy(volumes)
    vol_copy2 = deepcopy(volumes)
    
    winner = volumes[0]
    for i in range(1, len(volumes) ):

        winner = deepcopy(winner)
        
        contendent = volumes[i]
        print('WINN', winner, 'CONTEN', contendent)
        result = fight(winner, contendent)
        # print('winner contendent', winner,contendent)
        print('ganador', result)
        winner = result
        #if result == vol_copy2[i-1]: #winner:
         #   winner = vol_copy2[i-1]  #winner
       # elif result == vol_copy2[i]: #contendent:
        #    winner = vol_copy2[i]    #contendent
        #else:
         #   winner = vol_copy2[i-1]  #winner
        print('selection according to winner', winner)
    #print('VOLUMES  copy ', volumes_copy)
    index_of_partition_with_max_volume = volumes_copy.index(result)
    return rule_sets[ index_of_partition_with_max_volume ]

#-------------------------------------------------------------
#              Some tests for the function
#-------------------------------------------------------------

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
