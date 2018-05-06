#!/bin/python3

import sys


n = int(input().strip())
genes = input().strip().split(' ')
health = list(map(int, input().strip().split(' ')))

s = int(input().strip())
min=10000000000
max=0
for a0 in range(s):
    first,last,d = input().strip().split(' ')
    first=int(first)
    last=int(last)
    d=str(d)
    sum=0
    for i in range(first,last+1):
        f=1
        j=0
        while f>-1:
            print("helloc",f)
            f = d.find(genes[i], j)

            if f > -1:
                sum+=health[i]
                j=f+1
    if sum >= max:
        max=sum
    if min >= sum:
        min=sum
    #first,last,d = [int(first),int(last),str(d)]
    # your code goes here
print(min,max)
