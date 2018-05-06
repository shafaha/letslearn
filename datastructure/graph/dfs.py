from collections import defaultdict
d=defaultdict(list)
vertex = int(input('enter the number of vertex: '))
edges=int(input("enter the number of edges: "))

def DFS(i,traversed,d,s,parent,length):
    traversed[s] = 1
    
    length[s]=i
    i+=1
    
    for j in d[s]:
        if traversed[j] == 0:
            parent[j] = s
            DFS(i,traversed,d,j,parent,length)

for i in range(edges):
    x,y = list(map(int,input().split()))
    d[x].append(y)
    d[y].append(x)
vertex +=1
traversed=[0]*vertex
parent=[0]*vertex
length=[0] * vertex
DFS(0,traversed,d,1,parent,length)
print(parent)
print(length)