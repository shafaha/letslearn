from collections import defaultdict
from queue import LifoQueue
'''I AM GOING TO IMPLEMENT Breadth First Traversal TRAVERSAL BASICALLY
THIS IS KIND OF DIRECTED GRAPH AT ALL
'''
g = defaultdict(list)
#q=LifoQueue(maxsize=50)
number_of_vertex=int(input("number of vertex: "))
number_of_edges = int(input("enter the number of vertex: "))
for i in range(number_of_edges):
    j,k = list(map(int,input().strip().split()))
    g[j].append(k)
def deapthfirst(traversed,g,i,parent):
    if traversed[i] != 0:
        return
    traversed[i] = traversed[parent] + 1
    print(i)
    for j in g[i]:
        if traversed[j] == 0:
            deapthfirst(traversed,g,j,i)
traversed=[0] * (number_of_vertex +1)
deapthfirst(traversed,g,1,1)
print(max(traversed))
print(traversed)