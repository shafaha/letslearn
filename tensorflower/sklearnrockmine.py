import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.utils import shuffle
def ReadData():
    a=np.array([[1,2],[3,4],[5,6]])
    df= pd.read_csv('input/mine_rock.csv',names = np.arange(61))
    data = df[np.arange(60)]
    d={'R':1,'M':-1}
    target = df[60]
    target = target.map(d)
    #target = mean_normalizer(target.map(d))
    
    data = mean_normalizer(data)
    return data,target
    
    
def mean_normalizer(data):
    dmean=np.mean(data,axis = 0)
    dmax = np.max(data,axis = 0)
    dmin = np.min(data,axis = 0)
    dval =  data-dmean
    sigma = dmax - dmin
    required = dval/sigma
    return required

data,target = ReadData()
data,target = shuffle(data,target,random_state = 0)
print(data.shape,target.shape)
train_x,test_x,train_y,test_y = train_test_split(data,target,test_size = .1,random_state = 414)
clf = SVC()

clf.fit(train_x,train_y)
prediction = clf.predict(test_x) 
print(accuracy_score(prediction,test_y))
