# -*- coding: utf-8 -*-
"""

Given a set of rules R = [R1, R2, . . . , Rn]

Such that R = R* U R'

R* = set of lonley rules

R' = set of connected rule sets (with more than one element)


The function all_connected_sets()

recibes R and creates a list of connected sets (of any number of elements)

the function connected_and_lonly_rules(all_connected_sets)

takes all_connected_sets and returns R* and R'

"""


#--------------------------------------------------------------------------------------
#     Given two rules in the following format                                    ------

#     R1 = ( (1, 2, 3, 8, 11), (4, 6), 'A')                                      ------
#     R2 = ( (9,12),            5,     'C')                                      ------

#     The function " intersection " returns                                      ------
#     True if the rules intersect each other and                                 ------
#     False if they do not intersect                                             ------

#     Two rules intersect each other if the intervals formed with the minimum and  ----
#     maximum values of the sets located at each parameter i intersect each other  ----
#--------------------------------------------------------------------------------------

#Given a tuple, integer or float returns the maximum and minimum values
def interval(element):
    if type(element)==int:
        minimum = element
        maximum = element
    elif type(element)==float:
        minimum = element
        maximum = element
    else:
        minimum = min(element)
        maximum = max(element)
    #print('min,max',minimum,maximum)
    return (minimum,maximum)

#interval(7)
#min_max((1,3,6))

#Check if two intervals, defined through its minimum and maximum values,
#intersect each other
def interval_intersection(int1, int2):
    if ( (int1[0]<= int2[0] <= int1[1]) or (int1[0]<= int2[1] <= int1[1]) ):
        return True
    elif ( (int2[0]<= int1[0]<= int2[1]) or (int2[0]<= int1[1] <= int2[1]) ):
        return True
    else:
        return False
#interval_intersection( (1,11), (9,12) )
#interval_intersection( (2,5), (1,11) )
        
        
# NOTE that this function returns the INTERSECTION DISREGARDING THE CLASS
        
#Given two rules Returns true if they intersect each other
def intersection(rule1, rule2):
    intersection = True
    for i in range( len(rule1) - 1 ):
        if interval_intersection( interval(rule1[i]), interval(rule2[i]) ) == False:
            intersection = False
    return intersection
"""
tests

Example 1:
( (1, 2, 3, 8, 11), (4, 6), 'A'),
( (9,12),            5,     'C'),
(     5,             4,     'B'),
( (2,5),             7,     'D')

intersection( ( (2,5),             7,     'D'), ( (1, 2, 3, 8, 11), (4, 6), 'A') )
intersection ( (5, 4,'B'), ( (1, 2, 3, 8, 11), (4, 6), 'A'))
intersection( ( (1, 2, 3, 8, 11), (4, 6), 'A'), ( (9,12),            5,     'C'), )
intersection((     5,             4,     'B'),( (2,5),             7,     'D'))
intersection(( (9,12),            5,     'C'),(     5,             4,     'B'),)

Example2:
intersection(  ( (9, 12), 5, 'C'),( (10, 10.5 ), 4, 'B') )
intersection(  ( (9, 12), 5, 'C'),( (10, 10.5 ), 5, 'B') )

Example3:
intersection(((1,4),3,'A'), (2,(1,4),'A'))
intersection(((1, 4), 3, 'A'), (4, (3, 6), 'A'))

"""



#---------------------------------------------------------------
#  1. Select a random rule from R and eliminate it from the base
#  2. search for intersections of rule with Ri for Ri in R
#  store those intersections in Q
#  3. R = R\Q
#----------------------------------------------------------------

#..............................................................
#Take a random rule r from R
#   R = R \ rule
import random
def select_random_rule(R):
	rule = random.choice(R)
	R.remove(rule)		
	return(rule,R)
#...............................................................
#...............................................................
#Given a rule r and a rule base R
#search for intersections between R and r
def search_intersections(rule, R):
    I = []    
    for Ri in R:
        #print(Ri)
        if intersection(rule, Ri) == True:
            #print('TRUE')
            I.append(Ri)
            #R.remove(Ri)
    #Remove the rules with intersection from R
    for Ri in I:
        R.remove(Ri)
    I.append(rule)
    return [I,R]
"""
R = [
(   2,  (1,4), 'A'),
(   4,  (3,6), 'A'),
( (4,7),  7,   'A')
]
search_intersections(  ((1,4), 3, 'A') ,R)

R = [
(2,(3,5),'A'),
(3,(3,5),'A'),
(4,(3,5),'A'),
(5,(3,5),'A'),
(6,(3,5),'A'),
(7,(3,5),'A')
]
search_intersections(((1,8), 4, 'A'), R)

"""

#Second version of the function ------
#  returns Q the convex set
#          and
#  R = R the rule base \ Q

def Qi(R):
    Q = [ ]
    # 1 Select random rule, R = R\rule
    [rule, R] = select_random_rule(R)
    #2 Search for rules that intersect rule (I), R = R\I
    [ I  , R] = search_intersections(rule, R)
    Q = Q + [ I[-1] ]
    del I[-1]
    #print('I:', I, 'R:', R, 'Q', Q)
    
    intersections_found = True
    while intersections_found == True:
        intersections_found = False
        I_temp = []
        for r in I:
            [i, R] = search_intersections(r, R)
            Q = Q + [ i[-1] ]
            del i[-1]
            if len(i) > 0:
                intersections_found = True
            I_temp = I_temp + i
            #print(I_temp)
        I = I_temp
    #print('I:', I, 'R:', R, 'Q', Q)
    return [Q, R]
"""             
#-------------------------  TEST 1 -----------------------
R = [
((1,3), 1, 'A'),

(2, (1,4), 'A'),
((1,4), 3, 'A'),
(4, (3,6), 'A'),

((3,5), 6, 'A'),
(5,(6,8), 'A'),
((4,7), 7, 'A')
]
Qi(R)

#-------------------------  TEST 2 -----------------------
R = [
#convex1
( (1, 2, 3, 8, 11), (4, 6), 'A'),
(     5,             4,     'B'),
( (9,12),            5,     'C'),
#convex2
( (2,5),             7,     'D'),
#convex3
( (12),            (10,13), 'B'),
( (11,13),          (11,13),'D'),
#convex4
(   8,             (10,14), 'A'),
(  (6,9),            11,    'A')
]
Qi(R)  
#-------------------------  TEST 3 -----------------------

R = [
((1,3), 1, 'A'),

(2, (1,4), 'A'),
((1,4), 3, 'A'),
(4, (3,6), 'A'),

((3,5), 6, 'A'),
(5,(6,8), 'A'),
((4,7), 7, 'A'),

(12, (1,6), 'A'),
((9,13), 3, 'A')
]
Qi(R)
"""
#---------------------------------------------------------
#  Modified functions with indexes for the connected sets
#---------------------------------------------------------
def extract_connected_sets(R):
    connected_sets = []
    while len(R) > 0:
        [set_connected, R] = Qi(R)
        connected_sets.append(set_connected)
    return connected_sets

def connected_and_lonly_rules( all_connected_sets ):
    lonly_rules = []
    lonly_rules_indexes = []
    connected_rules = []
    connected_rules_indexes = []
    counter = -1
    for s in all_connected_sets:
        counter = counter + 1
        if len(s) == 1:
            lonly_rules = lonly_rules + s
            lonly_rules_indexes.append( counter )
        else:
            connected_rules.append(s)
            connected_rules_indexes.append(  counter )
    return [ lonly_rules, lonly_rules_indexes, connected_rules, connected_rules_indexes ]

"""
#-------------------------  TEST  -----------------------
R = [
#convex1
( (1, 2, 3, 8, 11), (4, 6), 'A'),
(     5,             4,     'B'),
( (9,12),            5,     'C'),
#convex2
( (2,5),             7,     'D'),
#convex3
( (12),            (10,13), 'B'),
( (11,13),          (11,13),'D'),
#convex4
(   8,             (10,14), 'A'),
(  (6,9),            11,    'A')
]
all_connected_sets = extract_connected_sets(R)
            
[ lonly_rules, connected_rules ] = connected_and_lonly_rules(all_connected_sets)
print(lonly_rules)
print(connected_rules)

"""


#   Proves to see if the function "intersection" can be used to find possible rules formation
#   with a new instance
#print(interval(5))
#print(interval(4))
#print(interval(11))
#print(interval_intersection(interval(5),interval(5)))

#--------------------------------------------------------------------------------------------
#    Intersection: All parameters of the new instance intersect the intervals formed by
#    the (min and max) values of an existing rule.
#
#    Possible rule formation: The new instance would have formed a rule with another instance.
#---------------------------------------------------------------------------------------------
def intersection_or_possible_rule_formation( new_pattern, rule, risk ):
    intersection = True
    for i in range( len(rule) - 1 ):
        if interval_intersection( interval(new_pattern[i]), interval(rule[i]) ) == False:
            intersection = False
    #return intersection
    possible_rule_formation = False
    lenght = len(rule) -1
    
    if new_pattern[-1] == rule[-1]:
        different_parameters = 0
        for i in range( len(rule) -1 ):
            if new_pattern[i] != rule[i]:
                different_parameters += 1
        if different_parameters <= risk:
            possible_rule_formation = True
    # Return True if either new_patterns intersects a rule or
    # if it would have created a rule (by calling rulex) with another instance or rule
    if intersection == True or possible_rule_formation == True:
        return True
    else:
        return False

#     Test to see if this really works
#res = intersection_or_possible_rule_formation([1, 2, 'A'], [2,2,'A'], 1)
#res = intersection_or_possible_rule_formation( [ 1, 2, 'A'], [2, 2, 'B'], 1)
#print(res)



#--------------------------------------------------------------------------------------
#     Function " intersection_with_new_pattern( pattern, rule ) "
#     This function call functions
#     1. interval
#     2. interval_intersection
#     and returns True (meaning the pattern and the rule intersect each other)
#     if one of its parameters intersect
#--------------------------------------------------------------------------------------
 
#def intersection_with_new_pattern( new_pattern, rule):
#    intersection = False
#    for i in range( len(rule) -1 ):
#        if interval_intersection( interval(new_pattern[i]), interval(rule[i]) ) == True:
#            intersection = True
#    return intersection
#print( intersection_with_new_pattern( (5,4,'B'), (5,11,'B') ) )

#print( intersection( (5, 4,'B'), (5, 11,'B') ) )





