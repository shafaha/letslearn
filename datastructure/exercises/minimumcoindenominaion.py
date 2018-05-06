'''Minimum num of coins required to change '''
v = int(input())
coins = list(map(int,input().split()))
pre = [0]*(v+1)
for i in coins:
    pre[i] = 1
def coinchange(v,coins,t=10000):
    if v<0:
        return -1
    elif v == 0:
        return 0
    for i in sorted(coins,reverse=True):
        x = change(v - i) + 1
        if x != 0:
            if t > x:
                t=x
    return t



def change(v):
    if pre[v] == 0:
        x=coinchange(v,coins)
        pre[v] = x
    return pre[v]
print(coinchange(v,coins))