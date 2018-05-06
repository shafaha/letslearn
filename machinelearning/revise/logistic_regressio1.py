from sklearn import datasets
import numpy as np
from sklearn.cross_validation import train_test_split 

iris = datasets.load_iris()
import math
#multi class classification
def deriver(prediction):
    for i in range(len(prediction)):
        if prediction[i] >0.5:
              prediction[i] = 1
        elif prediction[i] <0.5:
             prediction[i] = 0
        else:
             prediction[i] = 10
    return prediction
def find_accuracy(prediction,test_y):
          accuracy=0
          for i in range(len(prediction)):
              if prediction[i ] == test_y[i,0]:
                    accuracy+=1
          accuracy = accuracy*100/len(prediction)
          return accuracy
def mean_normalizer(data):
    data = np.hsplit(data,5)
    for i in range(1,5,1):
        data[i]=(data[i]-np.mean(data[i]))/(np.max(data[i]) - np.min(data[i]))
    data = np.hstack((data[0],data[1],data[2],data[3],data[4]))
    return data
def classA():
    iris  = datasets.load_iris()
    data = (iris.data)
    data= np.hstack((np.ones((150,1),dtype = np.float32),data))
    data =data.reshape(150,5)
    target = iris.target
    result = np.ones((150,),dtype = np.float32)
    for i in range(len(target)):
        if target[i] == 0:
            result[i] = 1
        else:
            result[i] = 0
    result = result.reshape(150,1)
    train_x,test_x,train_y,test_y = train_test_split(data,result,test_size = .15) 
    train_x = np.matrix(train_x)
    train_y = np.matrix(train_y)
    test_x= np.matrix(test_x)
    test_y = np.matrix(test_y)
    x=100
    theta_old= np.zeros((5,1) ,dtype = np.float32)
    for i in range(x):
        m=theta_old.copy()
        m[0,0]  = 0
        
        t = np.matrix(list(map(lambda x:1/(1+math.e**(-x[-1,0])),train_x * theta_old ))).T
        theta_new = theta_old - .001 * ((train_x.T)*(t-train_y) + 100 * m ) 
        if i == (x-1):
            break
        theta_old =theta_new.copy()
    prediction =list(map(lambda x:1/(1+math.e**(-x[-1,0])),test_x * theta_old  - 1000*m)) 
    #print(prediction)
    prediction = deriver(prediction)
    accuracy = find_accuracy(prediction,test_y)
    print(test_y.shape,len(prediction))
    print(test_y.T,prediction)
    print(theta_old)
    print(theta_new)
    print(accuracy)
    
#classA()
    
def classB():
    iris  = datasets.load_iris()
    data = (iris.data)
    data= np.hstack((np.ones((150,1),dtype = np.float32),data))
    data =data.reshape(150,5)
    data = mean_normalizer(data)
    target = iris.target
    result = np.ones((150,),dtype = np.float32)
    for i in range(len(target)):
        if target[i] == 1:
            result[i] = 1
        else:
            result[i] = 0
    result = result.reshape(150,1)
    train_x,test_x,train_y,test_y = train_test_split(data,result,test_size = .15) 
    train_x = np.matrix(train_x)
    train_y = np.matrix(train_y)
    test_x  = np.matrix(test_x)
    test_y  = np.matrix(test_y)
    x=100
    theta_old= np.zeros((5,1) ,dtype = np.float32)
    for i in range(x):
        m=theta_old.copy()
        m[0,0]  = 0
        
        t = np.matrix(list(map(lambda x:1/(1+math.e**(-x[-1,0])),train_x * theta_old ))).T
        theta_new = theta_old - .0001 * ((train_x.T)*(t-train_y) -100*m ) 
        if i == (x-1):
            break
        theta_old =theta_new.copy()
    prediction =list(map(lambda x:1/(1+math.e**(-x[-1,0])),test_x * theta_new)) 
    print(prediction)
    prediction = deriver(prediction)
    accuracy = find_accuracy(prediction,test_y)
    print(test_y.shape,len(prediction))
    print(test_y.T,prediction)
    print(theta_old)
    print(theta_new)
    print(accuracy)
classB()
