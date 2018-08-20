from builtins import input
import sys

temp = input()
ch = []
ch = temp.split(" ")

if len(ch) < 1 or len(ch) > 5:
    sys.exit()

for counter in range(0,len(ch)):
    for counter2 in range(counter,len(ch)-1):
    if ch[counter] == ch[counter+1]:
        sys.exit()

