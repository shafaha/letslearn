from collections import defaultdict
from queue import Queue
'''I AM GOING TO IMPLEMENT Breadth First Traversal TRAVERSAL BASICALLY'''
g = defaultdict(list)
q=Queue(maxsize=50)
number_of_vertex=int(input("number of vertex: "))
number_of_edges = int(input("enter the number of vertex: "))
for i in range(number_of_edges):
    j,k = list(map(int,input().strip().split()))
    g[k].append(j)
    g[j].append(k)


def breadthfirst(g,traversed):

    while not q.empty():
        x=q.get()
        print(x,end=" ")
        for i in g[x]:
            if traversed[i] == 0:
                q.put(i)
                traversed[i] = traversed[x] + 1


q.put(1)
traversed=[0] * (number_of_vertex +1)
traversed[1] = 1
breadthfirst(g,traversed)
print(max(traversed))