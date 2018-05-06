import numpy as np
import sklearn.cross_validation as scv 
l=50
a=np.hstack(((np.random.rand(l,1) ),(np.random.rand(l,1) )))
label=[]
for i in a:
    if i[0] >.5 and i[1] <.5:
        label.append(1)
    elif i[0]<.5 and i[1] >.5:
        label.append(1)
    else:
        label.append(0)
a= np.matrix(a).reshape(50,2)
theta_list=[np.matrix(np.zeros((3,2),dtype = np.float32)),np.matrix(np.zeros((3,1),dtype = np.float32))]

t=[a,[],[]]
label = np.matrix(label).reshape(50,1)
def bot(y,x):
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i,j] = x[i,j] * y[i,j]
    
for i in range(10):
    for j in range(1,3):
        a=t[j-1].copy()
        a=np.hstack((np.ones((50,1),dtype = np.float32),t[j-1]))
        t[j] = a*theta_list[j-1]
        for k in range(t[j].shape[0]):
            for l in range(t[j].shape[1]):
                  t[j][k,l] =1/(1 + np.e**t[j][k,l])
        
    #print(t[2])
    output =list(map(lambda x: 1/(1 + np.e**(-x[0,0])),t[2]))
    print(output)
    for i in output:
        if i >=0.5:
            i=1
        else:
            i=0    
    output = np.matrix(output).reshape(50,1)
    delta=[[],[],[]]
    delta[2] = output - label
    for i in range(1,0,-1):  
        x=t[j].copy()
        x=1-x
        bot(t[j],x)
        delta[j] = (delta[2]*theta_list[1][1:].T)
        bot(x,delta[j])
    
    D=
    for i in range(1,3):
        d[]
    break