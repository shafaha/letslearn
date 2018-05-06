array = list(map(int,input().split()))
array=[0] + array
a=[0,array[1]]
'''____CONSTRUCTION OF HEAP____'''
def mover(i):
    p=i//2
    print(p)
    if a[p] < a[i]:
        swap = a[p]
        a[p] = a[i]
        a[i] = swap
    if p >=2:
       mover(p)

for i in range(2,len(array)):
    a.append(array[i])
    mover(i)
    print(a)
heap = a


'''___HEAP SORTING____'''
def poper(i):
    l,r=2*i,2*i + 1
    if r<len(a):
        if r > l and a[r] > a[i]:
            swap = a[r]
            a[r] = a[i]
            a[i] = swap
            sel = r
        elif r < l and a[l] > a[i]:
            swap = a[l]
            a[l] = a[i]
            a[i] = swap
            sel = l
        else:
            return
    elif r == len(a):
        if a[i] <a[l]:
            swap = a[l]
            a[l] = a[i]
            a[i] = swap
            return
        else:return
    elif r> len(a):
        return
    poper(sel)


sor=[]
k= len(a)
for i in range(1,len(a)):
    print(a[1])
    a[1] = a[k-i]
    a.pop()
    poper(1)