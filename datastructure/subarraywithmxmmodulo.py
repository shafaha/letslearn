


a = list(map(int,input().split()))
val = int(input())
i = 0
j = 0
s=0
m = 0
while j<len(a):
    print(m,s)
    if s+a[j] < val:
        s+=a[j]
        m = s
    else:
        if (s + a[j])%val < s%val:
            if (s - a[i] +a[j])%val > s%val:
                s= s - a[i] + a[j]
                i+=1

        m = max(m,s%val)
    j+=1
print(m)