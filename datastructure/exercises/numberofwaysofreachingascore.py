'''numberof ways of reaching a score when permutation is not allowed
'''
score,num_of_moves = list(map(int,input().split()))
moves = list(map(int,input().split()))
array = [0]*(score + 1)
array[0] = 1
for i in range(num_of_moves):
    for j in range(moves[i],score+1):
        #print(array[j] - moves[i],end=" ")
        array[j] += array[j-moves[i]]
print(array)
