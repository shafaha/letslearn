
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
#accuracy score for the checking the score
iris=datasets.load_iris()
#print(iris)
#obtaining the data for the classification iris flower
'''x actually the features for the classification of the data and y actually the different spies of the flower'''
'''x=['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']'''
'''y=['setosa', 'versicolor', 'virginica']'''
x=iris.data
y=iris.target
plt.hist(x,y)
'''training the classifier and then testing for the validation'''
'''here we take decision tree for the classification'''
from sklearn.cross_validation import train_test_split
from sklearn import tree

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.5)
my_classifier_decisiontree=tree.DecisionTreeClassifier()
my_classifier_decisiontree.fit(x_train,y_train)
prediction_dtree=my_classifier_decisiontree.predict(x_test)
print(prediction_dtree)
print("accuracy_for_decisiontree: ",accuracy_score(y_test,prediction_dtree))
'''using the nearest neighbour for the classification'''
from sklearn.neighbors import KNeighborsClassifier
my_classifier_knn=KNeighborsClassifier()
my_classifier_knn.fit(x_train,y_train)
prediction_knn=my_classifier_knn.predict(x_test)

print("accuracy_for_the_knn_classifier:  ",accuracy_score(y_test,prediction_knn))
'''using the neural network'''


