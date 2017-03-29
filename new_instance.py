#---------------------------------------------------------------
#
#   This script recives a new instance and modify accordingly the existent rule base
#
#----------------------------------------------------------------

#  When a new instance "new_instance" comes,
#  in order to adjust only what is necessary we proceed as follows:

#  1. Find which of the original connected sets is intersected by the new instance.
#  2. Separate those sets and keep the rules that come from the others.

import json
from splitR import *
from optimum_partition_for_Q import *

#   Read all_connected_sets and indexes_all_connected sets
def read(file_name):
    with open( file_name) as json_data:
        t = json.load(json_data)
	print(t)

read(



def new(instance, all_connected_sets, indexes_all_connected_sets):
	print('do nothing')






"""
with open('strings.json') as json_data:
    d = json.load(json_data)
    print(d)
"""
