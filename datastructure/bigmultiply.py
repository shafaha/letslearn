num1 = list(map(int,input()))[::-1]
num2=  list(map(int,input()))[::-1]

def sum(num1,num2):
    carry = 0
    new = []
    for i in range(min(len(num1), len(num2))):
        carry, x = (num1[i] + num2[i] + carry) // 10, (num1[i] + num2[i] + carry) % 10
        new.append(x)
    if len(num1) > len(num2):
        for i in range(len(num2), len(num1)):
            carry, x = (num1[i] + carry) // 10, (num1[i] + carry) % 10
            new.append(x)
    else:
        for i in range(len(num1), len(num2)):
            carry, x = (num2[i] + carry) // 10, (num2[i] + carry) % 10
            new.append(x)
    print("l: ",new);
    new.append(carry)
    return new
new=[]
intermediate=[]
for i in range(len(num2)):
    carry=0
    new=[]
    for j in range(len(num1)):
        carry, x = (num1[i] * num2[i] + carry) // 10, (num1[i] * num2[i] + carry) % 10
        new.append(x)
    if carry !=0:
       new.append(carry)
    print(new)
    if i>0:
       intermediate=[0] + intermediate
    intermediate=sum(intermediate,new)
    #print(intermediate)

print(intermediate)