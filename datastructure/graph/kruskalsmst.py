from collections import defaultdict
from disjointset import DisjointSet
d = defaultdict(list)
vertex  = int(input('enter the number of vertices: '))
Edges  = int(input('enter the number of edegs: '))

X=DisjointSet(vertex)
X.makeset()
X.printer()
ed=[]
edges = defaultdict(list)
for i in range(Edges):
    x,y,w=list(map(int,input().split()))
    edges[x].append((w,y))
    edges[y].append((w,x))
    ed.append((w,x,y))

auxillary = sorted(ed)
graph=defaultdict(list)

for i in auxillary:
    w,u,v=i
    print(w,u,v)
    if X.findset(u) != X.findset(v):
        graph[u].append((v,w))
        graph[v].append((u,w))
        X.union(u,v)
    
    
print(graph)
