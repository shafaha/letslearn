n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
mnm = min(b)
mxm=  max(b)
A={}
B={}
for i in range(mnm,mxm+1):
    A[i] = 0
    B[i] = 0
for i in b:
    B[i] += 1
for i in a:
    A[i] += 1
for i in range(mnm,mxm+1):
    if A[i] != B[i]:
        print(i,end=" ")