# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 10:33:38 2017

@author: ivanpaz
"""
from operator import itemgetter
#-------------------------------------------------------------------
#Calculate the volume of an individual parameter
# volume = | max - min |
def parameter_volume(parameter):
    if type(parameter) == int or type(parameter)==float:
        maximum = parameter
        minimum = parameter
    else:
        minimum = min(parameter)
        maximum = max(parameter)
    volume = abs(maximum - minimum)
    return volume
#parameter_volume(5)
#parameter_volume((11,13,16))
#-------------------------------------------------------------------
#Function to calculate the volume of a rule
def rule_volume(rule):
    volume = []
    dimension = 0
    for parameter in range(0,len(rule) -1 ):
        parameter_contribution = parameter_volume(rule[parameter])
        if parameter_contribution != 0:
            dimension = dimension + 1
            volume = volume + [parameter_contribution]
            #print('volume:',volume)
    volume = sum(volume)
    return [volume,dimension]
#rule_volume((12, (10, 13), 'B'))
#-------------------------------------------------------------------
# Function that recibes an array with the [volume,dimension] for a set of rules
# and return the global [volume,dimension] for each dimension
def sum_equal_dimensions(volumes):
    total_volumes_and_dimensions = []
    while len(volumes) > 0:
        temporal = volumes[0]
        volumes.remove(temporal)
        for element in volumes:
            if temporal[1] == element[1]:
                temporal[0] = temporal[0] + element[0]
                volumes.remove(element)
        total_volumes_and_dimensions = total_volumes_and_dimensions + [temporal]
    return total_volumes_and_dimensions
#sum_equal_dimensions( [ [4.0, 2], [3.0, 1], [1.0, 1]  ] )
#sum_equal_dimensions([[3.0, 1], [4.0, 2], [1.0, 1]])
#-------------------------------------------------------------------
#Function that takes an array of arrays and sort them by its second entrance
#from operator import itemgetter

def sort_volumes(volumes):
    volumes = sorted(volumes,key=itemgetter(1))
    return volumes
#sort_volumes([[4.0, 1], [4.0, 2]])
#sort_volumes([[4.0, 2], [4.0, 1]])
#-------------------------------------------------------------------
#Function to calculate the volume of a set of rules
# For each rule in the set
    #calculate its volume
#retur the sum of the volumes
def partition_volume(rules):
    volumes = []
    for rule in rules:
        volume = rule_volume(rule)
        volumes = volumes + [volume]
    volumes = sum_equal_dimensions(volumes)
    volumes = sort_volumes(volumes)
    return volumes
#partition_volume([(12, (10, 13), 'B'), ((11, 13), (11, 13), 'D'), ((12,13),10,'B')])







