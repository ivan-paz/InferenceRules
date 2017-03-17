# -*- coding: utf-8 -*-
"""
Function that recibes a couple of lists
labeled with different class. For example :

lists          class
(1,2,3,8,11) -> 0
(5)          -> 1

and returns tuples separated by the classes

in the example :

(1,2,3) -> 0
(5)     -> 1
(8,11)  -> 0

"""
#  create list with format [element, class]
def create_labels(_list,_class):
    labels = list()
    if type(_list) == int or type(_list) == float:
        labels = labels + [[_list,_class]]
    else:
        for element in _list:
            pair = [element,_class]
            labels = labels  + [pair]
    return labels
#  create_labels((1,2,3,8,11),0)
#---------------------------------------------------------------------
#-------------------------------------------------------------------------------
import operator
def create_sets(_list1,_list2):
    list1 = create_labels(_list1, 0)
    list2 = create_labels(_list2, 1)
    one_list = list1 + list2
    sorted_list = sorted(one_list, key = operator.itemgetter(0))
    return sorted_list
#      create_sets((1,2,3,8,11),(5,6,9))
 
def subsets(a):
    zero = []
    #one =  []
    temp = []
    
    if a[0][1] == 0:
        classe = 0
    else:
         classe = 1
    for ele in a:
        #print(ele)
        
        if ele[1] == classe:
            temp = temp + [ ele[0] ]
            #print('ele',ele,'temporal',temp)
        else:
            #print('different class')
            #if classe == 0:
            #   zero = zero + [temp]
            #else:
            #     one = one + [temp]
            zero = zero + [temp,classe]
            classe = ele[1]
            temp = []
            temp = temp + [ele[0]]
    zero = zero + [temp,classe]
    return zero

#EXAMPLES
#a = [(1, 0), (2, 0), (3, 0), (5, 1), (8, 0),(9,0)]
#subsets(a)
#subsets([(1, 0), (2, 0), (3, 0), (5, 1), (8, 0)])
#subsets([(1, 0), (2, 0), (3, 0), (5, 1), (8, 0), (9, 1), (11, 0)])
#subsets([(1, 0), (2, 0), (3, 0), (5, 1), (6, 1), (8, 0), (9, 1), (11, 0)])  

def create_subsets(set1_class1,set2_class2):
    ordered_list = create_sets(set1_class1,set2_class2)
    list_of_subsets = subsets(ordered_list)
    return list_of_subsets
#      create_subsets( (1,2,3,8,11), (5))



