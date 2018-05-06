from sklearn import datasets
import numpy as np
from sklearn.cross_validation import train_test_split 
import pandas as pd
iris = datasets.load_iris()
import regresion1

def deriver(x):
    t=[]
    for i in x:
        if i > 2.8:
            i=3
        elif i>1.8 :
            i=2
        elif i>0.8:
            i=1
        else:
            i=0
        t.append(i)
    return t
def find_accuracy(prediction,test_y):
          accuracy=0
          for i in range(len(prediction)):
              if prediction[i ] == test_y[i]:
                    accuracy+=1
          accuracy = accuracy*100/len(prediction)
          return accuracy
def mean_regularization(data):
    data = np.hsplit(data,5)    
    for i in range(1,5):
        m = np.mean(data[i])
        difference = np.max(data[i]) - np.min(data[i])
        #print(m,np.max(data[i]),np.min(data[i]))
        data[i] = (data[i] - m)/difference
    data  =np.hstack((data[0],data[1],data[2],data[3],data[4]))
    return data
def mean_regularization_x(data):   
        m = np.mean(data)
        difference = np.max(data) - np.min(data)
        #print(m,np.max(data[i]),np.min(data[i]))
        data = (data - m)/difference
        return data
def batch_gradient_descent():
    data = iris.data
    data = np.hstack((np.ones((150,1),dtype = np.float32),data))
    result = iris.target
    train_x,test_x,train_y,test_y = train_test_split(data,result,test_size = .25)
    train_x=mean_regularization(train_x)
    train_y  = mean_regularization_x(train_y)
    train_x= np.matrix(train_x)
    train_y = np.matrix(train_y).T
    test_x= np.matrix(test_x)
    test_y =np.matrix(test_y).T
    theta_old= np.zeros((5,1),dtype = np.float32)
    x=500
    print(train_x.shape,train_y.shape,test_x.shape,test_y.shape)
    #theta_new =np.zeros((5,1),dtype = np.float32) 
    for i in range(x):
         t =theta_old.copy()
         t[0,0] = 1
         theta_new  = theta_old -.0001*((train_x.T) *(train_x * theta_old - train_y) +30*(t))
         if i == x-1:
             break
         theta_old= theta_new.copy()
    print("regularized: ")
    print(theta_new)
    print(theta_old)
    prediction = test_x * theta_old
    #print(prediction)
    prediction = deriver(prediction)
    accuracy = find_accuracy(prediction,test_y)
    print("regularized: ",accuracy)
batch_gradient_descent()
regresion1.batch_gradient_descent()
regresion1.using_module()