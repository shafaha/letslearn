from collections import defaultdict
from queue import Queue
'''I AM GOING TO IMPLEMENT Breadth First Traversal TRAVERSAL BASICALLY
THIS IS KIND OF DIRECTED GRAPH AT ALL
'''
g = defaultdict(list)
q=Queue(maxsize=50)
number_of_vertex=int(input("number of vertex: "))
number_of_edges = int(input("enter the number of vertex: "))
for i in range(number_of_edges):
    j,k,w= list(map(int,input().strip().split()))
    g[k].append((j,w))
    g[j].append((k,w))
def dijkstra(traversed,g):
   li=0
   while not q.empty():
       print(li)
       li+=1
       x=q.get()
       for i in g[x]:
           v,w=i
           if traversed[v] >traversed[x] + w:
              q.put(v)
              traversed[v] = traversed[x] + w
              pi[v] = x


q.put(1)
traversed=[1000] * (number_of_vertex +1)
traversed[1] = 0
pi=[0] *(number_of_vertex + 1)
dijkstra(traversed,g)

print(traversed)
print(pi)
