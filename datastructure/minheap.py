'''Basically i am constructing min heap'''



a=list(map(int,input().split()))
a.insert(0,0)
l=len(a)
heap = [0,a[1]]
def heapify_it(i):
    parent=i//2
    if parent< 1:
        return
    if heap[parent] > heap[i]:
        swap = heap[parent]
        heap[parent] = heap[i]
        heap[i] = swap
    heapify_it(parent)
for i in range(2,l):
    heap.append(a[i])
    heapify_it(i)
    print(heap)
print(heap)
def mover(heap,i):
    l=len(heap)-1

    while i < l:
        print("doppler")
        left = i * 2
        right = left + 1
        if right <= l:
            print("doppler")
            if heap[left] > heap[right] and heap[i] > heap[right]:
                swap = heap[right]
                heap[right] = heap[i]
                heap[i] = swap
                i=right
            elif heap[left] < heap[right] and heap[i] > heap[left]:
                swap = heap[left]
                heap[left] = heap[i]
                heap[i] = swap
                i=left
            elif heap[i] <= heap[right] and heap[i] <= heap[left]:
                break
        elif l == left:
            if heap[left] < heap[i]:
                swap = heap[left]
                heap[left] = heap[i]
                heap[i] = swap
            break
        else:
            break



def heapsort(heap):
    new=[]
    for i  in range(1,len(heap)-1):

        new.append(heap[1])
        x=heap.pop()
        heap[1] = x
        mover(heap,1)
    new.append(heap.pop())
    return new
print(heapsort(heap))
