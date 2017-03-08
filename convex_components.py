"""
General description


"""

#..............................................................
#Specific example
R = [
( (1, 2, 3, 8, 11), (4, 6), 'A'),
( (9,12),            5,     'C'),
(     5,             4,     'B'),
( (2,8),             8,     'B')
]
#..............................................................
#Take a random rule r from R
#   R = R \ r
import random
def select_random_rule(R):
	rule = random.choice(R)
	R.remove(rule)		
	return(rule,R)
#...............................................................
#Given a rule r and a rule base R
#search for intersections between R and r
def search_intersections(R):
    [rule,R] = select_random_rule(R)
    print(rule,R)
    
search_intersections(R)



#...............................................................
#Given two rules return False if they have the same class
def sameClass(rule1,rule2):
	class1 = rule1[-1]
	class2 = rule2[-1]
	if class1 != class2:
		return False
#Given a tuple, integer or float returns the maximum and minimum values
def min_max(element):
	if type(element)==int:
		minimum = element
		maximum = element
	elif type(element)==float:
		minimum = element
		maximum = element
	else:
		minimum = min(element)
		maximum = max(element)
	return (minimum,maximum)
	#print(min_max(3))
#min_max((1,3,6))

#Check if two sets intersect
def interval_intersection(int1, int2):
    if ( (int1[0]<= int2[0] <= int1[1]) or (int1[0]<= int2[1] <= int1[1]) ):
        return True
interval_intersection( (1,11), (9,12) )

#Given two rules Returns true if they intersect each other
def intersect(rule1, rule2):
    if sameClass(rule1,rule2) == False:
        #For each set S calculate the minimum and maximum
        for i in range(len(rule1) - 1):
            #print(min_max(rule1[i]))
            #print(min_max(rule2[i]))
        #Check if if Sets intersect each other
            return interval_intersection( min_max(rule1[i]), min_max(rule2[i]) )
        
#intersect(( (1, 2, 3, 8, 11), (4, 6), 'A'),  ( (9,12),            5,     'C'))









