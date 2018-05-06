class tree:
    def __init__(self, val, index, left=None, right=None):
        self.val = val
        self.index = index
        self.left = left
        self.right = right

    def add(self, val, index):
        if self == None:
            self = tree(val, index)
        else:
            temp = self
            while True:
                #print("mun")
                parent = temp
                if val > temp.val:
                    temp = temp.right
                    if temp == None:
                        parent.right = tree(val, index)
                        break
                else:
                    temp = temp.left
                    if temp == None:
                        parent.left = tree(val, index)
                        break

    def finder(self, value,i):
        temp = self
        while temp != None:
           # print('londa')
            if temp.val == value :
                if temp.index != i:
                    return temp.index
                else:
                    temp = temp.left
            elif temp.val > value:
                temp = temp.left
            elif temp.val < value:
                temp = temp.right
        return None

    def inorder(self, temp):
        if temp != None:
            self.inorder(temp.left)
            print(temp.val,temp.index)
            self.inorder(temp.right)



def icecreamParlor(m, arr):
    t=tree(arr[0],0)
    for i in range(len(arr)):
        t.add(arr[i],i)
    for i in range(len(arr)):
        x= t.finder(m-arr[i],i)
        if x != None  :
            return i+1,x+1



if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        m = int(input().strip())
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = icecreamParlor(m, arr)
        print (" ".join(map(str, result)))