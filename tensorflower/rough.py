from queue import PriorityQueue

q = PriorityQueue(maxsize = 100)

#we will beprovoded with a weight matrix

d={0:[(1,1),(7,4),(6,5)],
   1:[(1,2),(4,5)],
   2:[(2,5),(1,3)],
   3:[],
   4:[(2,3)],
   5:[(3,4),(2,3)]}


q.put((0,0))
dist  = [5000]*6
dist[0] = 0
parent=[0]*6
while not q.empty():
    w,v = q.get()
    for i in d[v]:
        x,y = i
        #print(x,y)
        if dist[y]> (x+w):
            parent[y] = w+x            
            dist[y] = w+x
            q.put((w+x,y))
print(dist)
print()
    

