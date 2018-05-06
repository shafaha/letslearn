from collections import defaultdict
s=int(input("enter the number of states: "))
dt=defaultdict(list)

for i in range(s):
    print("enter the transition on input symbol a: ")
    transition=list(map(int,input().split()))
    dt[i].append(transition)
    print("enter the transition on input symbol b: ")
    transition=list(map(int,input().split()))
    dt[i].append(transition)
ndt = defaultdict(list)
ndt[0] = dt[0]
while True:
    x=0
    if ndt[0]
print(ndt)
        
    
    