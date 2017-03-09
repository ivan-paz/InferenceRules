# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 10:29:19 2017
@author: ivanpaz
Given two rules in the following format

( (1, 2, 3, 8, 11), (4, 6), 'A'),  ( (9,12),            5,     'C')

The function " intersection " returns
True if the rules intersect each other and
False if they do not intersect

Two rules intersect each other if the intervals formed with the min and max
values for the sets located at each parameter i intersect each other 
"""
#...............................................................
#Given two rules return False if they have the same class
def sameClass(rule1,rule2):
	class1 = rule1[-1]
	class2 = rule2[-1]
	if class1 != class2:
		return False
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
    #print(minimum,maximum)
    return (minimum,maximum)
#interval(7)
    #min_max((1,3,6))

#Check if two intervals intersect each other
def interval_intersection(int1, int2):
    if ( (int1[0]<= int2[0] <= int1[1]) or (int1[0]<= int2[1] <= int1[1]) ):
        return True
    elif ( (int2[0]<= int1[0]<= int2[1]) or (int2[0]<= int1[1] <= int2[1]) ):
        return True
    else:
        return False
#interval_intersection( (1,11), (9,12) )
#interval_intersection( (2,5), (1,11) )

#Given two rules Returns true if they intersect each other
def intersection(rule1, rule2):
    intersection = True
    if sameClass(rule1,rule2)==False:
    #For each set S calculate the minimum and maximum
        for i in range(len(rule1) - 1):
            if interval_intersection( interval(rule1[i]), interval(rule2[i]) )==False:
                intersection = False
    else:
        intersection = False
    return intersection 


"""
Examples:
( (1, 2, 3, 8, 11), (4, 6), 'A'),
( (9,12),            5,     'C'),
(     5,             4,     'B'),
( (2,5),             7,     'D')

intersection( ( (2,5),             7,     'D'), ( (1, 2, 3, 8, 11), (4, 6), 'A') )

intersection ( (5, 4,'B'), ( (1, 2, 3, 8, 11), (4, 6), 'A'))

"""
























