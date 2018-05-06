

class Queue:
    def __init__(self,maxsize = 50):
        self.maxsize = maxsize
        self.length = 0
        self.array = []
    def put(self,value):
        self.array.append(value)
        self.length += 1
    def top(self):
        if len(self.array)>0:
            return self.array[0]
        else:
            return None
    def get(self):
        if self.length >0:
            x= self.array[0]
            self.length -= 1
            if self.length == 0:
                self.array = []
            else:
                self.array = self.array[1:]
            return x
        else:
            return None
        x=self.array[0]
        self.array = self.array[1:]
        return x
    def empty(self):
        return self.length == 0
    def printer(self):
        print(self.array,self.length)
q=Queue()
q.put(12)
q.put(13)
q.put(14)
print(q.top())

