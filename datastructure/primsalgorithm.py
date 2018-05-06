from collections import defaultdict

class PriorityQueue:
   def __init__(self,size):
       self.size = size
       self.valid=[True]*(self.size + 1)
       self.array=[]
       for i in range(1,self.size+1):
           self.array.append([100000,i])
   def get(self):
       mnm=100000;index=0
       for i in range(len(self.array)):
          if self.array[i][0] < mnm:
               mnm = self.array[i][0]
               index=i
       print(len(self.array),index)
       mnm = self.array[index]
       del self.array[index]
       self.valid[index] = False
       return mnm
   def printer(self):
       for i in self.array:
           print(i,i[0])
   def update(self,i,val):
       if self.array[i][0] >val:
           self.array[i]=[val,i]
   def validator(self,i):
       return self.valid[i]
   def set(self,i):
       self.array[i] = [0,i]
   def empty(self):
       if len(self.array) ==1:
           return 1


def loop_finder(parent,vertex):
    xer = [True] * (vertex+1)
    i=1
    x=1
    while True:
        x+=1
        if xer[i] == True:
            xer[i] = False
        else:
            return True
        i=parent[i]
        if x== vertex:
             return False
g=defaultdict(list)
vertex=int(input())
edges = int(input())
q=PriorityQueue(vertex)
for i in range(edges):
    x,y,w=list(map(int,input().split()))
    g[x].append((w,y))
    g[y].append((w,x))

q.set(1)
cost=0
s=[]
parent = [-1]*(vertex+1)
while not q.empty():
    w,x=q.get()
    s.append(x)
    cost += w
    for i in g[x]:
        w,y = i
        if q.validator(y):
            q.update(i[1],w)
            parent[y] = x

print(s)
print(parent)
print(loop_finder(parent,vertex))
