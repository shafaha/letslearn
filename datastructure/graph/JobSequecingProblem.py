#statement
'''Given an array of Jobs where every job has deadline and associated profit if the job is finished
accompolishment of job require same amount of time 
how to maximize the profit
'''

nomjobs = int(input("enter the number of jobs: "))
jobs=[]
for i in range(nomjobs):
    deadline,profit = list(map(int,input().split()))
    jobs.append((profit,deadline))

s= sorted(jobs,reverse = True)
print(s)
order={}
for i in s:
    t=i[1]-1
    while t>=0:
        if order.get(t) == None:
            order[t] = i[0]
            break
        t-=1
print(order)
