#!/bin/python3


def isValid(s):
    array = [0]*26
    for i in s:
        array[ord(i)-97] += 1
   mx= max(array)
   val = 0
   c1=0
   for i in range(26):
       if array[i] != 0:
           c1 += 1
           if array[i] != mx:
               val = array[i]
      
    
    
    
    

s = input().strip()
result = isValid(s)
print(result)
