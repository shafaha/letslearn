from math import ceil

size= int(input("eneter the size of array: "))
array = input("enter the array: ")

array = list(map(int,array.split()))
for j in range(size):
    pos=0
    m = array[0]
    for i in range(0,size-j):
       if array[i] >= m:
           m = array[i];pos=i
    t=array[size-j - 1]
    array[size-j-1] = m
    array[pos] = t
print(array)


