from math import ceil
def binarysearch(a,val):
    lower = 1
    upper = len(a)-1
    if val< a[lower]:
        return lower-1
    if val > a[upper]:
        return upper+1
    while upper > lower:
        print(upper,lower)
        middle = ceil((upper+lower)/2)
        if middle == upper:
            break
        if a[middle] > val:
            upper = middle
        else:
            lower = middle

    return upper
def bn(array,x,upper,lower):
    print(upper,lower)
    if upper - lower <= 1:
       return upper
    middle=(upper + lower)//2
    if array[middle] > x:
             return bn(array,x,middle,lower)
    else:
            return bn(array,x,upper,middle)


print(bn([0,10,15,20,22, 25 ,26, 28],18,7,0))