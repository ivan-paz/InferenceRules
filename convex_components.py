"""
General description
"""

#..............................................................
#Specific example
R = [
( (1, 2, 3, 8, 11), (4, 6), 'A'),
( (9,12),            5,     'C'),
(     5,             4,     'B'),
( (2,5),             7,     'D')

]

def convex_set(R):
    convex_set = [ ]
    index = 0
    [Q, R] = random_rule_with_intersections(R)
    #print('set: ', Q, "\n", 'R : ', R)
    convex_set.append(Q)
    if len(convex_set[index])>1: #if rule has intersect with other rule   
        for rule in convex_set[index]:
            [Q, R] = search_intersections(rule,R)
            convex_set.append(Q)
        index = index + 1
    #print('R',R)
    #print('convex set: ',convex_set)
    #Put all intersections into a single array
    convex_set = collect_intersections(convex_set)
    return(convex_set,'\n',R)
      
convex_set(R)

def collect_intersections(array):
    convex_set = []
    for i in array:
        for j in i:
            if j not in convex_set:
                convex_set.append(j)
    return convex_set
    
    
#Specific example
R = [
( (1, 2, 3, 8, 11), (4, 6), 'A'),
( (9,12),            5,     'C'),
(     5,             4,     'B'),
( (2,5),             7,     'D'),

( (12),            (10,13), 'B'),
((11,13),          (11,13),      'D')
]

convex_set(R)






















