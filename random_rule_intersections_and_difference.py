# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 11:13:52 2017

@author: ivanpaz

1. Select a random rule from R and eliminate it from the base
2. search for intersections of rule with Ri for Ri in R
store those intersections in Q
3. R = R\Q

"""
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






#     functions below . . . . may become depreciated
     
    
    
    
    
"""    
#Take a random rule from R
    # R = R\rule
    # Q = all Ri in R that intersect rule
    #R = R\Q
def random_rule_with_intersections(R):
    if R!=[]:
        [rule,R] = select_random_rule(R)
        [Q,R] = search_intersections(rule,R)
        return [Q, R]
"""
"""
R = [
( (1, 2, 3, 8, 11), (4, 6), 'A'),
( (9,12),            5,     'C'),
(     5,             4,     'B'),
( (2,5),             7,     'D')
]
random_rule_with_intersections(R)
"""













