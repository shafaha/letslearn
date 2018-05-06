import numpy as np
from sklearn.cross_validation import train_test_split 
from sklearn import datasets
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

'''doing simple linear_regression'''

'''this is batch gradient descent'''
dataframe=datasets.load_iris()
data=np.matrix(dataframe.data)
result=np.matrix(dataframe.target).T
train_x,test_x,train_y,test_y=train_test_split(data,result,test_size=.25)
scaler=StandardScaler()
scaler.fit(train_x)
print(train_x.shape)
#train_x=scaler.transform(train_x).reshape(train_x.shape)
print(train_x.shape)
#test_x=scaler.transform(test_x)

def normalizer(predict,normalization):
    for i in np.array(predict):
        if i[0] > 2.7:
              normalization.append(3)
        elif i[0] > 1.7:
              normalization.append(2)
        elif i[0] > 0.7:
              normalization.append(1)
        elif i[0] > -0.5:
              normalization.append(0)
        else:
            normalization.append(10)
    
def batch_gradient():
    theta_old=np.zeros((4,1),np.float32)
    for i in range(1000):
        theta_new=theta_old - .0001*(train_x.T)*(train_x*theta_old - train_y)
        theta_old=theta_new
        

    predict=test_x*theta_old
    normalization=[]
    normalizer(predict,normalization)
    prediction=np.array(normalization)
    print(prediction)
    #df=pd.Series(predict.reshape(30,1))
    accuracy=accuracy_score(test_y,prediction)
    print("score of batch_gradient_descent: ",accuracy)
    print(theta_new)
batch_gradient()
'''let look at normalization equation proble
   normal_equation=inv(x'*x)*x'*y
'''
def normal_gradient_descent():
    theta_normal=((train_x.T*train_x).getI())*(train_x.T)*train_y
    predict=test_x*theta_normal
    normalization=[]
    normalizer(predict,normalization)
    prediction=np.array(normalization)
    accuracy=accuracy_score(test_y,prediction)
    print("theta_norma:",theta_normal)
    print("normal_gradient_descent_accuracy: ",accuracy)
normal_gradient_descent()

'''Using the linear regression module'''
clf=LinearRegression()
scaler=StandardScaler()
scaler.fit(train_x)
train_x=scaler.transform(train_x)
test_x=scaler.transform(test_x)
clf.fit(train_x,train_y)
prediction=clf.predict(test_x)
print(clf.coef_.T)
normalization=[]
normalizer(prediction,normalization)
print(accuracy_score(test_y,normalization))