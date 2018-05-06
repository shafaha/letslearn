import sys
def minimumLoss(price):
    # Complete this function
    loss=10000000000000
    for i in range(0,len(price)-1):
        for j in range(i+1,len(price)):
            if price[i] > price[j]:
                print(price[i],price[j])
                loss = min(loss,price[i] -price[j])
    return loss

if __name__ == "__main__":
    n = int(input().strip())
    price = list(map(int, input().strip().split(' ')))
    result = minimumLoss(price)
    print(result)