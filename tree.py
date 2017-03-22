# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 18:21:03 2017

@author: ivan

Q = [
        ( (1,2,3,8,11), (4,6), 'A'),
        (       (9,12),     5, 'C'),
        (            5,     4,'B')    
    ]
"""
from break_edges import *
#----------------------------------------------------
#   a = np.array([(5, 4, 'B'), ((1, 2, 3, 8, 11), (4, 6), 'A'), ((9, 12), 5, 'C')], dtype = object)
import numpy as np
def shape(a):
    a = np.array(a,   dtype = object) # dtype = object
    return(a.shape)
#----------------------------------------------------
#  ORIGINAL WORKING FUNCTION
def tee(q):
    tree_leafs = []
    i = 0
    d = {}
    leafs = True
    while leafs == True:
        j = 0
        leafs = False
        if len(shape(q)) == 1:
            print('Case1 ' , q)
            temp1 = []
            
            i = i + 1
            
            for element in q:    
                temp = cut(element)
                
                
                for k in temp:
                    j = j + 1
                    d[str(i)+ ',' +str(j)] = k
                    
                
                temp1 = temp1 + temp
                if temp != []:
                    leafs = True
                else:
                    new_leaf = element
                    print('LEAF: ', element)
                    tree_leafs.append(new_leaf)
                    
            temp = temp1
            q = temp ###
        else:
            print('Case2', q)
            temp = cut(q)
            leafs = True
            q = temp
            
            i = i + 1
            for k in q:
                j = j + 1
                d[str(i)+ ',' +str(j)] = k
            
    return [d, tree_leafs]

#Q = [((6, 9), 11, 'A'), (8, (10, 14), 'A')]
#Q = [(12, (10, 13), 'B'), ((11, 13), (11, 13), 'D')]
#d  = tee(Q)
#[d, leafs] = tee(Q)
    
#for leaf in leafs:
#    print(leaf)
#----------------------------------------------------------------------------
"""




"""


"""
def tee(q):
    leafs = True
    while leafs == True:
        leafs = False
        if len(shape(q)) == 1:
            temp1 = []
            for element in q:
                temp = cut(element)
                print('ADDING: ', temp)
                temp1 = temp1 + temp
                if temp != []:
                    leafs = True
            temp = temp1
            q = temp ###
            print('Case1 ' , q)
        else:
            temp = cut(q)
            leafs = True
            q = temp
            print('Case2', q)
    return leafs          
tee(Q)




class Tree(object):
    "Generic tree node."
    def __init__(self, name='root', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

#    *
#   /|\
#  1 2 +
#     / \
#    3   4
t = Tree('*', [Tree('1', [Tree('1,1')]),
               Tree('2'),
               Tree('3', [ Tree('3,1'),
                           Tree('3,2') ])])
for i in t.children:
    print(i.children)
t.add_child([Tree('11'),[Tree('1')]])

def tee(q):
   
    t = Tree('*')
    leafs = True
    while leafs == True:
        i = 0
        j = 0
        leafs = False
        if len(shape(q)) == 1:
            print('Case1 ' , q)
            temp1 = []
            for element in q:    
                temp = cut(element)
                
                for k in temp:
                    j = j + 1
                    t.add_child([Tree(str(k))])
                
                temp1 = temp1 + temp
                if temp != []:
                    leafs = True
            temp = temp1
            q = temp ###
        else:
            print('Case2', q)
            temp = cut(q)
            leafs = True
            q = temp
            
            for k in q:
                i = i + 1
                d[str(i)+str(j)] = k
            
    return [d,k] 
d  = tee(Q)

"""