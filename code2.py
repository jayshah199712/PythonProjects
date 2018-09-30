from builtins import input
import sys
from itertools import permutations

A = int(input())
B = int(input())
s=A*"a"+B*"b"
perms = [''.join(p) for p in permutations(s)]

for item in perms:
    if "aaa" not in item and "bbb" not in item:
        print(item)
        break