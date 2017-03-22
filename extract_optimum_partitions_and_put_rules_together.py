# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 17:34:23 2017

@author: ivanpaz
"""
from optimum_partition_for_Q import *

def extract_optimum_partitions(connected_rules):
    optimum_partitions = []
    for q in connected_rules:
        opt = optimum_partition(q)
        if opt == False:
            optimum_partitions.append(q)
        else:
            optimum_partitions.append(opt)
    return optimum_partitions
#-------------------------------------------------------------------------
def put_rules_together(optimum_partitions,lonly_rules):
    rules = []
    for partition in optimum_partitions:
        for rule in partition:
            rules.append(rule)
    for rule in lonly_rules:
        rules.append(rule)
    return rules
#-----------------------------------------------------------------------
