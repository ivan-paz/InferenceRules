# -*- coding: utf-8 -*-
"""
The function "create possible orders"
recibes a list with rules and returns the different orders (trees) of the rules indexes
in which the rules can be arranged for cutting

Created on Sat Mar 11 19:01:00 2017
@author: ivan
"""
import itertools
#import math

#This function creates a list with the elements of a tuple
def put_in_list(x):
    _list = []
    for i in x:
        comb = []
        for j in i:
            comb.append(j)
        _list.append(comb)
    return _list

def set_difference(s,combination):
    set_difference = s - set(combination)
    return set_difference

def create_possible_orders(T):
    trees = []
    rule_set_size = len(T)
    #   s = set(range( 1 ,  rule_set_size +1 ))   to see the printed values
    s = set(range( 0 ,  rule_set_size ))  #The first argument is the starting counting point
    
    #combinations_size = int((math.factorial(rule_set_size) / ( 2 * math.factorial(rule_set_size - 2))))
    #permutations_size = int( math.factorial(rule_set_size) / ( rule_set_size - (rule_set_size - 2) )   )    
 
    #Create combinations
    _combinations = put_in_list(itertools.combinations(s, 2))
    for i in _combinations:
        difference = set_difference(s,i)
        #print(i,difference)
        _permutations = put_in_list(itertools.permutations(difference, len(difference)))
        for j in _permutations:
            tree = []
            tree = tree + i
            tree = tree + j
            print(tree)
            trees.append(tree)
    return trees
"""
Examples
T = [(1,1,'A'),(2,1,'B'),(1,2,'A'),(1,3,'A')]

T = [(1,1,'A'),(2,1,'B'),(1,2,'A')]

create_possible_orders(T)

"""