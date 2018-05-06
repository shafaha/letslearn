from math import ceil

s1 = sorted(list(map(int,input().split())))
s2 = sorted(list(map(int,input().split())))
n = len(s1)
def bn(array,x,upper,lower):
    #print(upper,lower)
    if upper - lower <= 1:
        if x**array[lower] > array[lower]**x:
            return lower
        return upper
    middle=ceil((upper + lower)//2)
    if array[middle]**x < x**array[middle]:
             return bn(array,x,middle,lower)
    else:
            return bn(array,x,upper,middle)

for i in range(n):
    print(s1[i],bn(s2, s1[i],n-1, 0))
