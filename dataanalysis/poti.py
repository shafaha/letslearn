class tree:
    def __init__(self,z,x=None,y=None):
        self.cargo=z
        self.left=x
        self.right=y
    def __str__(self):
        return str(self.cargo)
    def add(self,value):
        temp=self
        while True:
            temp2=self
            if value > temp.cargo:
                temp=temp.right
                if temp == None:
                    temp2.right=tree(value)
                    break
            else:
                temp=temp.left
                if temp == None:
                    temp2.left=tree(value)
    def search(self,value):
        temp=self
        parent=self
        while True:
            if temp.cargo == value:
                return parent
            if temp.cargo  > value:
                parent=temp
                temp=temp.right
            else:
                parent=temp
                temp=temp.left

    def inorder(self,temp):
        if temp != None:
            self.inorder(temp.left)
            print(temp.cargo,end=" ")
            self.inorder(temp.right)



t=tree(1)
t.add(12)
t.inorder(t)