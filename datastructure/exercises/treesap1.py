
'''COMPLETE TREE IMPLETENTATION'''
class tree:
    def __init__(self,data=0,left = None,right = None):
        self.data = data
        self.left = None
        self.right = None

    def add(self,data):
        temp = self
        while temp != None:
            cont = temp
            if temp.data > data:
                temp = temp.left
                if temp == None:
                    cont.left = tree(data)
                    break
            elif temp.data < data:
                temp = temp.right
                if temp == None:
                    cont.right = tree(data)
                    break
    def inorder(self):
        l=[]
        temp = self
        while True :
            if temp == None:
                temp = l.pop()
                print(temp.data,end=" ")
                temp = temp.right
            if temp !=None:
                l.append(temp)
                temp = temp.left
            if l == []:
                break
    def height(self,temp):
        if temp == None:
            return 0
        lheight = self.height(temp.left)
        rheight = self.height(temp.right)
        return max(lheight,rheight) + 1

    def search(self,val,node):
        temp = node
        parent = temp
        while True:
            parent = temp
            if val > temp.data:
                temp = temp.right
            elif temp.data >val:
                temp = temp.left


            if temp.data == val:
                return parent,temp
            if temp == None:
                return None

    @staticmethod
    def recinorder(temp):
        if temp != None:
            tree.recinorder(temp.left)
            print(temp.data)
            tree.recinorder(temp.right)
    def deleter(self,val,node):
        parent,child = self.search(val,node)
        if child ==  None:
            return "cannot be deleted"
        print(parent.data,child.data)

        if child.left == None and child.right == None:
            if parent.left == child:
                parent.left=None
            else:
                parent.right = None
            return "deleted"
        elif child.left ==None or child.right == None:
            if parent.left == child:
                if child.left == None:
                    parent.left = child.right
                else:
                    parent.left = child.left
            else:
                if child.left == None:
                    parent.right = child.right
                else:
                    parent.right = child.left
            return "deleted __"
        else:
            temp = child.right
            while temp!= None:
                if temp.left != None:
                    temp=temp.left
                else:
                    break
            child.data = temp.data
            parent,children = self.search(temp.data,child.right)
            if parent == children:
                child.right=None
            else:
                self.deleter(temp.data,child.right)
            return "deleted"


'''
t=tree(10)
t.add(20)
t.add(15)
t.add(5)
t.add(4)
t.add(7)
t.add(22)
t.add(24)
t.add(21)
t.add(23)
#traversal without using the recursion
#tree.recinorder(t)
t.inorder()
print("\n",t.height(t))
print(t.deleter(10,t))
t.inorder()'''


