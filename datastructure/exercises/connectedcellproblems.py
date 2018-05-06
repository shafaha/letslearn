
'''connected cell problems in the square boolean matrix'''
n = int(input())
g={}
for i in range(n):
   g[i]=list(map(int,input().split()))


def dfs(i,j):
    if i>=n or j>=n or g[i][j] == 0 or i<0 or j<0:
        return 0
    g[i][j] = 0
    return dfs(i+1,j) + dfs(i,j+1) +dfs(i+1,j-1)+dfs(i+1,j+1) + 1
m=0
for i in range(n):
    for j in range(n):
        if g[i][j] == 1:
            m=max(m,dfs(i,j))
print(m)