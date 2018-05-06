import numpy as np

key = "HFKFLJH"
key = list(set(list(key)))
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mat= key + [i for i in alpha if i not in key]
mat = [i for i in mat if i != 'J']
mat = np.array(mat).reshape(5,5)
print(mat)
def finder(c,mat):
    for i in range(5):
        for j in range(5):
            if mat[i][j] == c:
                return (i,j)
message = input("enter your messaye: " ).upper()
message = [i for i in message if i != " "]
if len(message) %2 == 1: 
    message.append('P')
print(message)
print(len(message))
enc = []

for i in range(0,len(message),2):
        print(i,enc)
        i1,j1 = finder(message[i+0],mat)
        i2,j2 = finder(message[i+1],mat)
        if i1 == i2:
            enc.append(mat[i1][(j1+1)%5])
            enc.append(mat[i1][(j2 + 1)%5])
        elif j1 == j2:
            enc.append(mat[(i1 + 1)%5][j1])
            enc.append(mat[(i2 + 1)%5][j2])
        else:
            enc.append(mat[i1][j2])
            enc.append(mat[i2][j1])
print(np.array(enc))


