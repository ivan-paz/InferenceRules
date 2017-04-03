


#-----------------------------------------------------------------
#         1.  Recibe a new unseen pattern (or rule).
#         2.  Find out which connected sets of rules it intersects.
#         3.  Apply rulex to the set formed by the new pattern and its intersections.
#         4.  Apply cut to to the resulting set to find the best partition (greatest volume).
#-----------------------------------------------------------------
from new_instance import *

pattern = [ 2, 5, 'A']


# when processing new patterns first call rulex and then break
pattern = [ 5, 5, 'B']
new_rule_base = process_new_pattern( pattern )


