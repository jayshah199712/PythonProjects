
from builtins import input
import sys

# defining all the lists
two = ['A', 'B', 'C']
three = ['D', 'E', 'F']
four = ['G', 'H', 'I']
five = ['J', 'K', 'L']
six = ['M', 'N', 'O']
seven = ['P', 'Q', 'R', 'S']
eight = ['T', 'U', 'V']
nine = ['W', 'X', 'Y', 'Z']

# Get the literals input
literals = []
temp = input()
literals = (list(str(temp)))

if len(literals) < 1 or len(literals) > 40:
    sys.exit()

print(literals)





