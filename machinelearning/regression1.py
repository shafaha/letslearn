from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
lr= LinearRegression()

import numpy as np
iris=datasets.load_iris()
data=iris.data
target=np.matrix(iris.target).reshape(150,1)

#data = np.hstack((np.ones((150,1),dtype=np.float32),data))
mean=np.mean(data,axis=0)
mx=np.max(data,axis = 0)
mn= np.min(data,axis = 0)
data  = np.matrix([(i - mean)/(mx -mn) for i in data],dtype = np.float32).reshape(data.shape)
data = np.hstack((np.ones(target.shape,dtype=np.float32),data))
theta_old = np.zeros((5,1),dtype = np.float32)
theta_new = theta_old.copy()
train_x,test_x,train_y,test_y = train_test_split(data,target,test_size= .15)
for i in range(1000):
    dh = train_x.T*(train_x*theta_new - train_y)
    theta_new[0,0] = theta_old[0,0]-.0001*(dh[0,0])
    theta_new[1:,:] = theta_old[1:,:] - .0001*(dh[1:,:] + 0*(theta_old[1:]))
    theta_old = theta_new.copy()

def reformer_accuracy(predict,test_y):
    count=0
    for i in range(predict.shape[0]):
        if predict[i,0] > 2.5:
              predict[i,0] = 3
        elif predict[i,0] > 1.5:
              predict[i,0] = 2
        elif predict[i,0] > 0.5:
              predict[i,0] = 1 
        else:
            predict[i,0]=0
        
        if predict[i,0] == test_y[i,0]:
            count+=1
    return count
predict = test_x * theta_old 
accuracy = reformer_accuracy(predict,test_y)
print(np.hstack((predict,test_y)))

print(accuracy*100/23)


    