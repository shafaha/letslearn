import numpy as np
import pandas as pd
from sklearn import datasets
import math
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
def xpose(l,v):
    t=[]
    for i in l:
        if i == v:
            t.append(1)
        else:
            t.append(0)
    return t
def normalizer(x):
    if x< .9:
        return 0 
    else:
        return 1
def classifier(i,j):
    theta_old=np.zeros((5,1),np.float32)
    train_x,test_x,train_y,test_y=train_test_split(i,j,test_size=0.25)
    for i in range(1000):
        t=np.matrix(list(map(lambda x: 1/(1 + math.e **(-x)) , np.array(train_x * theta_old))))
        #print(t.shape)
        theta_new=theta_old  - .0001*((train_x.T) * (t - train_y))
        #print(theta_new.shape,train_y.shape,t.shape)
        theta_old=theta_new
    t=list(map(lambda x: 1/(1 + math.e **(-x)) , np.array(test_x * theta_new)))
    prediction=np.array(list(map(normalizer,t)))
    print(accuracy_score(test_y,prediction))
    
iris=datasets.load_iris()
feat=pd.DataFrame(iris.data)
lab=iris.target
s=pd.DataFrame(np.ones((150,1),np.float32))
feat=pd.concat([s,feat],ignore_index=True,axis=1)

train_x=np.matrix(feat)
cls0=np.array(xpose(lab,0)).reshape((150,1))
cls1=np.array(xpose(lab,1)).reshape((150,1))
cls2=np.array(xpose(lab,2)).reshape((150,1))
cls3=np.array(xpose(lab,3)).reshape((150,1))
classifier(train_x,cls0)
classifier(train_x,cls1)
classifier(train_x,cls2)
classifier(train_x,cls3)


#print(np.matrix((df)))