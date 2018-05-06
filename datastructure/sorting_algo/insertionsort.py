from math import ceil

size= int(input("eneter the size of array: "))
array = input("enter the array: ")

array = list(map(int,array.split()))
newarray = [array[0]]
for j in range(1,size):
   pos = j
   for i in range(j):
       if newarray[i] > array[j]:
           pos=i
           break
   newarray= newarray[:pos]  +  [array[j]] + newarray[pos:]
   print(newarray)

