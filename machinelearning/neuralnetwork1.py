from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
import numpy as np
lr = LinearRegression()
iris=datasets.load_iris()
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
def using_module():
          data = iris.data
          target = iris.target
          train_x,test_x,train_y,test_y=train_test_split(data,target,test_size = .15)
          lr.fit(train_x,train_y)
          print("using_module_coeff: ",lr.coef_)
          prediction= lr.predict(test_x)

          prediction = deriver(prediction)
          accuracy=find_accuracy(prediction,test_y)
          print("accuracy_by_module: ",accuracy)
def batch_gradient_descent():
    data = np.matrix(iris.data)
    data = np.hstack((np.zeros((150,1),dtype = np.float32),data))
    target = np.matrix(iris.target).reshape(150,1)
    train_x,test_x,train_y,test_y = train_test_split(data,target,test_size = 0.25)
    theta_old= np.matrix(np.zeros((5,1),dtype = np.float32))
    print(theta_old.shape)
    
    for i in range(1000):
        theta_new =theta_old - .0001*(train_x.T)*(train_x * theta_old - train_y)
        theta_old= theta_new
    #print(theta_new.shape,test_y.shape,test_x.shape)
    print("batch_gradient_descent: ",theta_old)
    prediction =test_x.dot(theta_new) 
    #print(prediction)
    prediction = deriver(prediction)
    test_y= (np.array(test_y.ravel()))
    #print(test_y[0])
    accuracy = find_accuracy(prediction,test_y[0])
    print("batch_gradient_descent_accuracy: ",accuracy)
def normal_equation():
    data =np.matrix( iris.data)
    target= np.matrix(iris.target).reshape(150,1)
    data = np.hstack((np.ones((150,1),dtype = np.float32),data))
    train_x,test_x,train_y,test_y = train_test_split(data,target,test_size = .15)
    print(train_x.shape,train_y.shape)
    theta = (((train_x.T) * train_x).getI()) * train_x.T *train_y 
    print("normal_equation_theta: ",theta)
    prediction = test_x * theta
    prediction = deriver(prediction)
    test_y = np.array(test_y.ravel())
    accuracy = find_accuracy(prediction,test_y[0])
    print("accuracy of normal_equation:",accuracy)
    
batch_gradient_descent()
normal_equation()
using_module()
    
    