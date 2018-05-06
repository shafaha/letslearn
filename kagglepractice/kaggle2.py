import pandas as pd
import numpy as np
from sklearn.svm import SVC 
#from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
#ss = StandardScaler()
from sklearn.cross_validation import train_test_split


df = pd.read_csv('input/titanic_train.csv')
df.fillna({'Age':np.mean(df.Age)},inplace=True)
col1 = np.where(df.Sex == 'female',2,1)

indata  = pd.DataFrame({'Fare':np.sqrt(df.Fare),                        
                      'Age' : df.Age,
                      'Sex' : col1*col1})
target =np.where(df.Survived == 1,1,0)


train_x,test_x,train_y,test_y = train_test_split(indata,target,test_size = 0.2)



clf = SVC()

#clf = LogisticRegression(solver='newton-cg',max_iter = 1000)
clf.fit(indata,target)
predicted = clf.predict(test_x)
print(accuracy_score(predicted,test_y))
test_df = pd.read_csv('input/titanic_test.csv')
test_df.fillna({'Age':np.mean(test_df.Age)},inplace=True)
col1 = np.where(test_df.Sex == 'female',2,1)
outdata  = pd.DataFrame({'Fare':test_df.Fare,
                      'Age' : test_df.Age,
                      'Sex' : col1})

outdata.fillna({'Fare':np.mean(outdata.Fare)},inplace = True)
print(outdata.isnull().any())

predicted = clf.predict(outdata)
output  = pd.DataFrame({'PassengerId': test_df.PassengerId,
                        'Survived':np.where(predicted == 2,1,0)})
output.to_csv('output/testoutput.csv',header=True,index = False)



