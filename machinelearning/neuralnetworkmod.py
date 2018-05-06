from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
bc=datasets.load_breast_cancer()
data=bc.data
target=bc.target
train_x,test_x,train_y,test_y=train_test_split(data,target,test_size=.25)
scaler=StandardScaler()
scaler.fit(train_x)
train_x=scaler.transform(train_x)
test_x=scaler.transform(test_x)
perceptron=MLPClassifier(solver='lbfgs',alpha=0.001,hidden_layer_sizes=(5,5) , random_state = 1)
perceptron.fit(train_x,train_y)

prediction=(perceptron.predict(test_x))

print("bais:")
print(perceptron.intercepts_)
print("accuracy_score: ",accuracy_score(prediction,test_y))