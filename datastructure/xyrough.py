

n= int(input())
def clear(n):
    traversed = {}
    for i in range(n):
        traversed[i] = [0] * n
    return traversed

def dontmove(x,y,mx,my,traversed,n):
    if x>n-1 or y>n-1 or x<0 or y<0 or traversed[x][y] == 1:
        return 5000
    elif x== n-1 and y==n-1:
        return 0
    traversed[x][y] =1
    t=min(dontmove(x+mx,y+my,mx,my,traversed,n),dontmove(x-mx,y+my,mx,my,traversed,n),dontmove(x+mx,y-my,mx,my,traversed,n),dontmove(x+my,y+mx,mx,my,traversed,n),dontmove(x-my,y+mx,mx,my,traversed,n),dontmove(x+my,y-mx,mx,my,traversed,n))+1
    return t
for i in range(1,n):

    for j in range(1,n):
        t = clear(n)
        c=dontmove(0,0,i,j,t,n)
        if c>=5000:
            print(-1,end=" ")
        else:
            print(c,end=" ")
    print()