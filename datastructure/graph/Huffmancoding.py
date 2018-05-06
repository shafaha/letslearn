from queue import PriorityQueue

q = PriorityQueue(maxsize = 1000)

#here i considered that
class Tree:
    def __init__(self,value,count,left = None,right = None):
        self.value = value
        self.count = count
        self.left = left
        self.right = right
def printer(root):
        if root != None:
            printer(root.left)
            print(root.value,root.count)
            printer(root.right)
t=[]
charnoms = int(input())
for i in range(charnoms):
    c,cou = input().split()
    q.put((int(cou),Tree(c,int(cou))))

while not q.empty():
    cou1,node1 = q.get()
    if q.empty():
        root = node1
        break
    cou2,node2=q.get()
    print(cou1,node1.value,cou2,node2.value)
    node =  Tree(node1.value+node2.value,cou1+cou2,node1,node2)
    q.put((cou1+cou2 , node))
#printer(root)