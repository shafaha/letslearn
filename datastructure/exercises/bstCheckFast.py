from treesap1 import tree
'''Fast checking of the validity of bst'''

def bst_check(node,lower,upper):
    if node == None:
        return True
    if node.data <=lower  or node.data> upper:
        return False
    elif node.left ==None and node.right != None:
        if bst_check(node.right, node.data, upper):
            return True
        return False
    elif node.left != None and node.right == None:
        if bst_check(node.left, lower,node.data):
            return True
        return False
    else:
        if bst_check(node.left,lower,node.data) and bst_check(node.right,node.data,upper):
             return True
    return False

t=tree(12)
t.add(16)
t.add(77)
t.add(5)
t.inorder()
t.data = 5
print(bst_check(t,-10000,+10000))
