
s1 = input()
s2 = input()
t=[]
for i in range(len(s1)+1):
    t.append([0]*(len(s2) + 1))

for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if s1[i-1] == s2[j-1]:
            t[i][j] = t[i-1][j-1] + 1
        else:
            t[i][j] = max(t[i-1][j],t[i][j-1])
print(t[len(s1)][len(s2)])