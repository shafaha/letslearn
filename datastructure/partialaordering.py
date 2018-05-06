
from collections import defaultdict
from queue import Queue
'''Topological Sorting in Dag'''
g= defaultdict()
vertex= int(input("vertex: "))
edges=int(input("edges: "))
q=Queue(maxsize=100)
indeg=[0] * (vertex + 1)
for i in range(edges):
    x,y = list(map(int,input()))
    g[x].append(y)
    indeg[y] += 1
for i in range(1,vertex):
    if indeg[i] == 0:
        q.put(i)
while not q.empty():
    x=q.get()
    print(x)
    for i in g[x]:
        indeg[i] -=1
        if indeg[i] == 0:
            q.put(i)


