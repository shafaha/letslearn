import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC 
from sklearn.linear_model import  LogisticRegression
from sklearn.utils import shuffle
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf
import matplotlib.pyplot as plt
#read datasets

def PredictionSklearn(data,target):
    data,target = shuffle(data,target,random_state = 415)
    train_x,test_x,train_y,test_y  =train_test_split(data,target,test_size = .1)
    cls = LogisticRegression()
    cls.fit(train_x,train_y)
    prediction = cls.predict(test_x)
    print(accuracy_score(prediction,test_y))
def OneHotEncoding1(y):
    uni = np.unique(y)
    count = len(uni)
    vec = np.array([0]*count)
    m={}
    for i in range(count):
        vec[i] = 1
        m[uni[i]] = vec.copy()
        vec[i] = 0
    return y.map(m)
def OneHotEncoding2(y):
    le = LabelEncoder()
    le.fit(y)
    label = le.transform(y)
    #above three line of coding beautifull convert categorical
    
    count = len(label)
    unique_count = len(np.unique(label))
    target = np.zeros((count,unique_count))
    target[np.arange(count),label] =1
    print(target)
    return target
    
def ReadData():
    df= pd.read_csv('input/mine_rock.csv',names = np.arange(61))
    data = df[np.arange(60)]
    target = df[60]
    target = OneHotEncoding2(target)
    
    #newd =np.vstack((target,df[60]))
    #print(newd)
    return (data,target)

X,Y = ReadData()
X,Y = shuffle(X,Y,random_state = 1)
train_x,test_x,train_y,test_y = train_test_split(X,Y,test_size = 0.1,)

#Defining Important Parameter for the classification

learning_rate = 0.03
training_epochs = 1000
cost_history = np.empty(shape=[1],dtype = float)
n_dim = X.shape[1]
print("n_dim",n_dim)
n_class =2
model_path = './model'

#defining the number of hidden layer
n_hidden_1 = 60
n_hidden_2 = 60
n_hidden_3 = 60
n_hidden_4 = 60
 
x= tf.placeholder(tf.float32,[None,n_dim])
W = tf.Variable(tf.zeros([n_dim,n_class]))
b = tf.Variable(tf.zeros([n_class]))
y_ = tf.placeholder(tf.float32,[None,n_class])
def multilayer_perceptron(x,weight,baises):
    layer_1 = tf.add(tf.matmul(x,weight['h1'],baises['b1']))
    layer_1 = tf.nn.sigmoid(layer_1)
    layer_2 = tf.add(tf.matmul(layer_1,weight['h2'],baises['b2']))
    layer_2 = tf.nn.sigmoid(layer_2)
    layer_3 = tf.add(tf.matmul(layer_2,weight['h3'],baises['b3']))
    layer_3 = tf.nn.sigmoid(layer_3)
    layer_4 = tf.add(tf.matmul(layer_3,weight['h4'],baises['b4']))
    layer_4 = tf.nn.relu(layer_4)
    
    out_layer = tf.matmul(layer_4,weight['out'] + baises['out'])
    return out_layer
weight = {
        'h1':tf.Variable(tf.truncated_normal([n_dim,n_hidden_1])),
        'h2':tf.Variable(tf.truncated_normal([n_hidden_1,n_hidden_2])),
        'h3':tf.Variable(tf.truncated_normal([n_hidden_2,n_hidden_3])),
        'h4':tf.Variable(tf.truncated_normal([n_hidden_3,n_hidden_4])),
        'out':tf.Variable(tf.truncated_normal([n_hidden_4,n_class]))
        
            }
baises =  {
        'b1':tf.Variable(tf.truncated_normal([n_hidden_1])),
        'b2':tf.Variable(tf.truncated_normal([n_hidden_2])),
        'b3':tf.Variable(tf.truncated_normal([n_hidden_3])),
        'b4':tf.Variable(tf.truncated_normal([n_hidden_4])),
        'out':tf.Variable(tf.truncated_normal([n_class]))
        }
init = tf.global_variables_initializer()
saver =   tf.train.Saver()
y = multilayer_perceptron(x,weight,baises)
cost_function = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=y,labels=y_))
training_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost_function)
sess = tf.Session()
sess.run(init)
mse_history = []
accuracy_history = []

for epochs in range(training_epochs):
    sess.run(training_step,feed_dict = {x:train_x,y_:train_y})
    cost = sess.run(cost_function,feed_dict={x:train_x,y_:train_y})
    cost_history = np.append(cost_history,cost)
    correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(y_,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
    #print('Accuracy: ',(sess.run(accuracy,feed_dict={xx:test_x,y_:test_y})))
    pred_y = sess.run(y,feed_dict={x:test_x})
    mse = tf.reduce_mean(tf.squared(pred_y - test_y))
    mse_=sess.run(mse)
    mse_history.append(mse_)
    accuracy = (sess.run(accuracy,feed_dict={x:train_x,y_:train_y}))
    accuracy_history.append(accuracy)
    print('epoch : ',epochs,' - cost: ',cost,' - Mse: ',mse_,'- train accuracy',accuracy)
    
save_path = saver.save(sess,model_path)
print('Model saved in file: %s'%save_path)
plt.plot(mse_history,'r')
plt.show()
plt.plot(accuracy_history)
    







