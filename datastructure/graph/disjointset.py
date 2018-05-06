class DisjointSet:
    def __init__(self,size,array=[0],rank=[0]):
        self.size = size+1 
        self.array=array
        self.rank = rank
    def makeset(self):
        for i in range(self.size):
            self.array.append(i+1)
            self.rank.append(0)
    def union(self,u,v):
        x = self.findset(u)
        y = self.findset(v)
        if self.rank[x] > self.rank[y]:
            self.array[y] = x
            if self.rank[x] <=self.rank[y] + 1:
                self.rank[x] = self.rank[y] + 1
        else:
            self.array[x] = y
            if self.rank[y] <=self.rank[x] + 1:
                self.rank[y] = self.rank[x] + 1
    def findset(self,u):
        print(u)
        if self.array[u] == u:
            return u
        x=self.findset(self.array[u])
        self.array[u] = x
        return x
    def printer(self):
        print(self.array)
        print(self.rank)
        for i in range(self.size):
            print("%d  <- %d"%(i+1,self.array[i]))
            
'''a= [0,1,1,1,1,2,3,5,0,0,0,11,11,11,12]
b=  [0,3,2,1,0,1,0,0,0,0,0,2,1,0,0]
ds1 = DisjointSet(15,a,b)
ds1.printer()
ds1.union(7,14)
print(ds1.findset(14))
ds1.printer()'''