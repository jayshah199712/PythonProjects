from builtins import input
import sys

N = int(input())
if N < 1 or N > 1000:
    sys.exit()
s = " "
flag=0
for i in range(1,N+1):
    flag=0
    if(i%2==0):
        flag=1
        s="Codility"
    if(i%3==0):
        flag=1
        s="Test"
    if(i%5==0):
        flag=1
        s="Coders"
    if(i%2==0 and i%3==0):
        flag=1
        s="CodilityTest"
    if(i%2==0 and i%5==0):
        flag=1
        s="CodilityCoders"
    if(i%3==0 and i%5==0):
        flag=1
        s="TestCoders"
    if(i%2==0 and i%3==0 and i%5==0):
        flag=1
        s="CodilityTestCoders"
    if(flag==1):
        print(s)
    else:
        print(i)



