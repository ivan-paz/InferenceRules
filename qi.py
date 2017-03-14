# -*- coding: utf-8 -*-
"""

    algorithm to construct an independent (convex) set Qi
    from a rule base R


"""
"""
def Qi(R):
    # 1 Select random rule, R = R\rule
    [rule, R] = select_random_rule(R)
    #2 search for rules that intersect rule (I), R = R\I
    [ I  , R] = search_intersections(rule, R)
    I = [I]
    #print('I:', I, 'R:', R)
    
    intersections_found = True
    position = -1
    
    while intersections_found == True:
        
        intersections_found = False
        position = position + 1
        
        I_temp = []
        for r in I[position]:
            print('Iposition',position,I[position])
            #print(r)            
            [i, R] = search_intersections(r,R)
            print(i,R)
            
            
            if len(i) > 1:
                intersections_found = True
            
            I_temp = I_temp + i
            #print('I_temp',I_temp, i)
        I = I + [I_temp]
        #devuelve solo el último conjunto********************!!!!!!!!
    print('I: ',I)
    print('--------------------------------------')
    print('R',R)
    return [I[-1],R]
"""

#----------------------------------------------------------------

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

#------------------

def extract_convex_sets(R):
    convex_sets = []
    while len(R) > 0:
        [set_convex, R] = Qi(R)
        print(set_convex)
        convex_sets.append(set_convex)
    return convex_sets
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
extract_convex_sets(R)






















