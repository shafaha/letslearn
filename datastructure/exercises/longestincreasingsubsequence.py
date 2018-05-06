
'''longest increasing subsequenc via dynamic programming'''
array = list(map(int,input().split()))
ax=[1]*(len(array))
for i in range(0,len(array)):
    for j in range(i+1,len(array)):
        if array[j] >= array[i]:
            ax[j] = max(ax[j],ax[i] +1)
    print(ax,array[i])

print(max(ax))