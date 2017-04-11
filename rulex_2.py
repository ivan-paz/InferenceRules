# -*- coding: utf-8 -*-

#---------------------------------------------------------------
#                              rulex                       -----
#---------------------------------------------------------------
# Format    parameter_values  | class risk_parameter
# preset = (  1,        1,      'A',  1    )


"""
presets = (
(1, 1,'A',1),
(1, 2,'A',1),
(1, 3,'A',1),
(1, 4,'B',1)
)
"""
"""
presets = (
(1, 1,'A',1),
(2, 1,'A',1),
(1, 3,'A',1),
(1, 4,'B',1),
(1,11,'A',1),
(1,12,'A',1) )
"""


# input presets in tuple format -> output -> rules tuple format
def rulex(presets):
    i = -1
    for preset_1 in presets:
        #print('preset_1: ',preset_1)
        i = i + 1
        j = -1
        for preset_2 in presets:
            j = j + 1
            if( (preset_1 and preset_2) != None):
                if is_compressible(preset_1,preset_2) != False:
                    dictionary = is_compressible(preset_1,preset_2)
                    #print('dictionary',dictionary)
                    if dictionary != False:
                        rule = build_rule(preset_1, dictionary)
         #               print('rule: ', rule)
                        #delete rules preset_1 and preset_2 and app rule
                        lst = list(presets)
                        if rule not in lst:
                            lst.append(rule)
                            lst[i] = None
                            lst[j] = None
                            presets = tuple(lst)
                        #print(presets)
    #eliminate redundant
    rules = clear_Nones(presets)
    rules = non_redundant(rules)
    rules = clear_Nones(rules)
    print(rules)
    return rules

#rulex(presets)
#---------------------------------------------------------------------------
#         is_compressible takes as inputs two presets and if they are   ----
#                 compressible returns a dictionary                     ----
#                        index -> value                                 ----
#     with the index in wich the presets are different and the values   ----
#---------------------------------------------------------------------------
def is_compressible(preset_1, preset_2):
    dictionary = {}
    if preset_1 == preset_2:
        return dictionary
    for i in range( len(preset_1) - 1 ):
        if(preset_1[i] != preset_2[i]):
#            print('preset 1 and 2 ', preset_1[i],preset_2[i])
            dictionary[i] = set( [ preset_1[i], preset_2[i] ] )
    #print(dictionary)
    if bool(dictionary):
        if len(dictionary) <= preset_1[-1] and  preset_1[-2]== preset_2[-2]:
            return dictionary
        else:
            return False
#----------------------------------------------------------------------------
"""
#                   tests
# if preset_1 == preset_2 returns empty dictionary
is_compressible( (1, 1,'A',1),(1, 1,'A',1) )
#Out: {}
# return dict with index -> different values
is_compressible( (1, 2,'A',1),(1, 1,'A',1) )
#Out: {1: {1, 2}}
is_compressible( (1, (1,2),'A', 1), (1, 11, 'A', 1) )
#Out: {1: {(1, 2), 11}}
is_compressible( (1, 1,'A',1),(1, 1,'B',1) )
#Out: False
is_compressible( (1, 1,'A',1),(2, 3,'A',1) )
#Out: False
is_compressible( (1, 1,'A',2),(2, 3,'A',1) )
#Out:  {0: {1, 2}, 1: {1, 3}}
"""
#-------------------------------------------------------------------------
#                   Build rule receives (preset_1, dictionary)        -----
#                         return produced rule                       -----
#-------------------------------------------------------------------------
def build_rule(preset_1, my_dict):
    for element in my_dict:
        my_tuple = ()
        for value in my_dict[element]:
            if(type(value) == tuple):
                for i in value: my_tuple = my_tuple + (i,)
            else:
                    my_tuple = my_tuple + (value,)
        temp = []
        for i in my_tuple:
            if i not in temp:
                temp.append(i)
        temp.sort()
        my_tuple = tuple(temp)
        #Check for contradictions to create the rule if risk > 1
        lst = list(preset_1)
        lst[element]=my_tuple
        preset_1 = tuple(lst)
    return preset_1
#----------------------------------------------------------------------------
"""
#                   tests
# if empty dictionary returns preset_1
my_dict = {}
preset_1 = (1, 1,'A',1)
build_rule(preset_1,my_dict)
#Out: (1, 1, 'A', 1)
# if dict return preset_1 with tuples at indexes of the different keys of dict
my_dict = {1: {1, 2}}
preset_1 =(1, 2,'A',1)
build_rule(preset_1,my_dict)
#Out: (1, (1, 2), 'A', 1)
my_dict = {1: {(1, 2), 11}}
preset_1 = (1, (1,2),'A', 1)
build_rule(preset_1,my_dict)
#Out: (1, (1, 2, 11), 'A', 1)
my_dict = {0: {1, 2}, 1: {1, 3}}
preset_1 = (1, 1,'A',2)
build_rule(preset_1,my_dict)
#Out:  {0: {1, 2}, 1: {1, 3}}
"""
#---------------------------------------------------------------------------
def clear_Nones(tuple_type):
    temp = []
    for i in tuple_type:
        if i!=None:
            temp.append(i)
    return temp
"""
# test
tuple_type = (None, None, None, (1, 4, 'B', 1), (1, (1, 2), 'A', 1), None, (1, (1, 2, 3), 'A', 1))
clear_Nones(tuple_type)
#Out: [(1, 4, 'B', 1), (1, (1, 2), 'A', 1), (1, (1, 2, 3), 'A', 1)]
"""
#---------------------------------------------------------------------------
#              Eliminates rules that are contained in other rules        ---
#                                                                        ---
#---------------------------------------------------------------------------
def non_redundant(rules):
    counter = -1
    for rule1 in rules:
        counter = counter + 1
        for rule2 in rules:
            if rule2 != None and rule2 != rule1:
                contained = 0
                boolean = [(rule1 == rule2) for rule1, rule2 in zip(rule1,rule2)]
#                print(boolean)
                trues = sum(boolean)
                for i in range(len(boolean)):
                    if boolean[i] == False:
 #                       print(rule1, rule2)
                        set1 = build_set(rule1[i])
                        set2 = build_set(rule2[i])
                        if set1.issubset(set2):
                            contained = contained + 1
                if trues + contained == len(rule1):
                    rules[counter] = None
    return rules

"""
# test
non_redundant([(1, 4, 'B', 1), (1, (1, 2), 'A', 1), (1, (1, 2, 3), 'A', 1)])
#Out: [(1, 4, 'B', 1), None, (1, (1, 2, 3), 'A', 1)]
non_redundant([ (1, 4, 'B', 1),(1, 1, 'A', 1),(1, (1, 2, 3), 'A', 1)])
#Out: [(1, 4, 'B', 1), None, (1, (1, 2, 3), 'A', 1)]
non_redundant([ (1, (1,2), 1, 'A', 1),(1, 1, (1, 2, 3), 'A', 1)])
#Out: [(1, (1, 2), 1, 'A', 1), (1, 1, (1, 2, 3), 'A', 1)]
"""
#--------------------------------------------------------------
def build_set(i):
    if type(i)==tuple:
        _set = set()
        for j in i:
            _set.add(j)
    else:
        _set = set([i])
    return _set
"""
#test
build_set(1)
#Out: {1}
build_set((1,2,3))
#Out: {1, 2, 3}
""" 

#non_redundant([ (1, 4, 'B', 1), (1, (1,2), 'A',1), (1, (1,2,3),'A',1)])
# Test
"""
presets = (
(1, 1,'A',1),
(2, 1,'A',1),
(1, 3,'A',1),
(1, 4,'B',1),
(1,11,'A',1),
(1,12,'A',1) )

rulex(presets)
"""
#   ----------------------------------------------------------------------   #
"""
import json
def read(file_name):
    with open(file_name) as json_data:
        file_content = json.load(json_data)
        return file_content

def write(file_name,data):
    with open (file_name, 'w') as f:
        json.dump(data,f)
#--------------------------------------
presets = read('new_set.json')
presets = [
[[1,3] ,2,'A',1],
[2,2,'A',1]
]
new_set = rulex(presets)
"""
