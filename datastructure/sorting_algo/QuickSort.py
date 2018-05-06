a=list(map(int,input().split()))
l = len(a)
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