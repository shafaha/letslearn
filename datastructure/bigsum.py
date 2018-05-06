num1 = list(map(int,input()))[::-1]
num2=  list(map(int,input()))[::-1]
carry=0
new=[]
for i in range(min(len(num1),len(num2))):
    carry,x=(num1[i] + num2[i] + carry)//10,(num1[i] + num2[i] + carry)%10
    new.append(x)
if len(num1) > len(num2):
    for i in range(len(num2),len(num1)):
        carry, x = (num1[i]  + carry) // 10, (num1[i] + carry) % 10
        new.append(x)
else:
    for i in range(len(num1),len(num2)):
        carry, x = (num2[i]  + carry) // 10, (num2[i] + carry) % 10
        new.append(x)
new.append(carry)
print(new)