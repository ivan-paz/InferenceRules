# -*- coding: utf-8 -*-
"""
Function that recibes two lists of numbers of different class
For example :
lists          class
{1,2,3,8,11} -> 0
{5}          -> 1

and returns separate lists with no intersection

in the example :

{1,2,3} -> 0
{5}     -> 1
{8,11}  -> 0

"""
def dictionary(_list,_class):
    dictionary = dict()
    if type(_list) == int or type(_list) == float:
        dictionary[_list]= _class
    else:
        for element in _list:
            dictionary[element] = _class
    return dictionary
#dictionary((1,2,3,8,11),0)



#---------------------------------------------------------------------
# 
def subsets(a):
    zero = []
    one =  []
    temp = []
    
    if a[0][1] == 0:
        classe = 0
    else:
         classe = 1
    
    for ele in a:
        print(ele)
        
        if ele[1] == classe:
            temp = temp + [ ele[0] ]
            print('ele',ele,'temporal',temp)
        else:
            print('different class')
            #if classe == 0:
            #   zero = zero + [temp]
            #else:
            #     one = one + [temp]
            zero = zero + [temp,classe]
            classe = ele[1]
            temp = []
            temp = temp + [ele[0]]
    zero = zero + [temp,classe]
    return [zero]


a = [(1, 0), (2, 0), (3, 0), (5, 1), (8, 0),(9,0)]

subsets(a)

subsets([(1, 0), (2, 0), (3, 0), (5, 1), (8, 0)])
subsets([(1, 0), (2, 0), (3, 0), (5, 1), (8, 0), (9, 1), (11, 0)])
subsets([(1, 0), (2, 0), (3, 0), (5, 1), (6, 1), (8, 0), (9, 1), (11, 0)])

           
           
#-------------------------------------------------------------------------------
import operator
def create_sets(_list1,_list2):
    dict1 = dictionary(_list1,0)
    dict2 = dictionary(_list2,1)
    _dictionary  = dict(dict1, ** dict2)
    sorted_dictionary = sorted( _dictionary.items(), key = operator.itemgetter(0) )
    print(sorted_dictionary)

create_sets((1,2,3,8,11),(5,6,9))

