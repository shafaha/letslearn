from math import ceil
a=list(map(int,input().split()))

l = len(a)
if l%2 == 1:
    a.append(100000);l+=1

def Merge(array, p, q, r):
    ax1 = array[p:q+1] + [1000000000]
    ax2 = array[q+1:r+1] + [1000000000]
    k = 0
    j = 0
    print(p,q+1,r+1)
    for i in range(p, r+1):
        if ax1[k] >= ax2[j]:
            array[i] = ax2[j]
            j += 1
        else:
            array[i] = ax1[k]
            k += 1
    print(array[p:r+1])
def MergeSort( array, p, r):
    if p < r:
        q = ((p + r) // 2)
        MergeSort(array, p, q)
        MergeSort(array, q + 1, r)
        Merge(array, p, q, r)

#MergeSort(a,0,l-1)
#print(a)
def Partition(array,p,r):
    pivot=array[r]
    i=p-1
    for j in range(p,r):
       if array[j] < pivot:
           i+=1
           swap = array[i]
           array[i] = array[j]
           array[j] = swap
    swap = array[i+1]
    array[i+1] = pivot
    array[r] = swap
    return i+1
def QuickSort(array,p,r):
    if p < r:
        q=Partition(array,p,r)
        QuickSort(array,p,q-1)
        QuickSort(array,q+1,r)



QuickSort(a,0,l-1)
print(a)
