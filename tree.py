# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 18:21:03 2017

@author: ivan
"""

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
    print(i)
    for j in i.children:
        print(j)
    

d = {}
P = cut(Q)
t = Tree('*')
for i in range(len(P)):
    d[str(i)] = P[i] 
    t.add_child(Tree(str(i)))


    

Q
t = Tree('*')
new_nodes = True

while new_nodes == True:
    new_nodes = False
    p = cut(Q)
    childrens = len(p)
    for i in range(childrens):
        print(p[i])
        t.add_child( Tree(str(i),[ Tree(p[i]) ] ) )

t.children[0].children


t = Tree('*')
import random
for i in range(5):
    if random.randint(1,4)%2 ==0:
        t.add_child(Tree(str(i),[Tree('a')]))
