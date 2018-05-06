
'''
array = list(map(int,input()))
l = len(array)
for i in range(0,l-(l%2),2):
    if array[i] >array[i+1]:
        swap = array[i]
        array[i] = array[i+1]
        array[i+1] = swap
'''
def merger(a,i,j,l1,l2,width):
    b=[]
    print(i,j,l1,l2,width)
    while True:
        if a[i] > a[j]:
            b.append(a[j])
            j += 1
        else:
            b.append(a[i])
            i += 1
        #print(i,j)
        if j > l2 or i > l1:
            break
    if i < l1+1:
        b = b + a[i:l1+1]
    elif j < l2+1:
        b = b + a[j:l2+1]
    return b
def auxilary(a):
    k=1
    while k < len(a):
       for i in range(0,len(a),2*k):
           if i+2*k > len(a):
               a[i:len(a)] = merger(a, i, i + k, i + k - 1, i + 2 * k - 1, 2 * k)
           else:
               a[i:i+2*k] = merger(a,i,i+k,i+k-1,i+2*k-1,2*k)
           print(a[i:i+2*k])
       k*=2





a=[1,1,1,2,2,2,6,6]
auxilary(a)
