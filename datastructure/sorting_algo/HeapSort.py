

a=list(map(int,input().split()))
a=[0]+a
def MaxHeapify(array,i,length):
    l= 2*i
    r=2*i + 1
    largest = i
    if l<=length and a[l] > a[i]:
        largest = l
    if r<= length and a[largest] < a[r]:
        largest = r
    #print(i,largest)
    if largest != i:
        swap = a[largest]
        a[largest] = a[i]
        a[i] = swap
        MaxHeapify(array,largest,length)
def BuildMaxHeap(array):
    l = len(array)-1
    nl= l//2
    #print(nl)
    for i in range(nl,0,-1):
        MaxHeapify(array,i,l)
BuildMaxHeap(a)
def ExtractMaxHeap(array):
    x=a[1]
    l = len(array) - 1
    if l == 1:
        return array.pop()
    a[1]  = array.pop()

    MaxHeapify(array,1,l-1)
    return x
BuildMaxHeap(a)
for i in range(len(a)-1):
    print(ExtractMaxHeap(a))
