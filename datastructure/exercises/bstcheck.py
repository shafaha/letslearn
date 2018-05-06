from treesap1 import tree

def right_min(node):
    while node != None:
        if node.left != None:
            node = node.left
        else:
            break
    return node.data
def left_max(node):
    while node !=None:
        if node.right != None:
            node = node.right
        else:
            break
    return node.data

def bst_check(node):
    if node.left == None and node.right == None:
        return True
    elif node.left ==  None and node.right !=  None:
         if bst_check(node.right) and node.data < right_min(node.right) :
             return True
         else:
             return False
    elif node.right ==  None and node.left != None:
        if bst_check(node.left) and node.data >= left_max(node):
            return True
        else:
            return False
    else:
        if bst_check(node.left) and bst_check(node.right) and node.data >= left_max(node.left) and node.data<right_min(node.right):
            return True
        else:
            return False

t=tree(12)
t.add(35)
t.add(186)
t.add(11)
t.data = 10
print(bst_check(t))