import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import shuffle
import tensorflow as tf
def OneHotEncoding(y):
    l = len(y)
    classes = len(np.unique(y))
    Le = LabelEncoder()
    Le.fit(y)
    label = Le.transform(y)
    one = np.zeros((l,classes),dtype = np.float32)
    one[np.arange(l),label] = 1
    return one
    
def ReadData():
    df = pd.read_csv('input/mine_rock.csv',header = None)
    y = df.pop(60)
    Y = OneHotEncoding(y)
    return df,Y

X,Y = ReadData()
X,Y = shuffle(X,Y,random_state = 1)
train_x,test_x,train_y,test_y = train_test_split(X,Y,test_size=0.1,random_state = 415)
X = np.float32(X)

learning_rate = 0.03
training_epochs = 1000
cost_history = np.empty(shape=[1],dtype = float)
print(cost_history)
n_dim = X.shape[1]

hiddenlayer_1=60
hiddenlayer_2=60
hiddenlayer_3=60
hiddenlayer_4=60
n_classes=2

x= tf.placeholder(tf.float32,[None,n_dim])
W = tf.Variable(tf.zeros([n_dim,n_classes]))
b = tf.Variable(tf.zeros([n_classes]))
y_ = tf.placeholder(tf.float32,[None,n_classes])

def MultilayerPerceptron(x,weight,baises):
    layer_1 = tf.add(tf.matmul(x,weight['h1']),baises['b1'])
    layer_1 = tf.nn.sigmoid(layer_1)
    
    layer_2 = tf.add(tf.matmul(layer_1,weight['h2']),baises['b2'])
    layer_2 =  tf.nn.sigmoid(layer_2)
    
    layer_3 = tf.add(tf.matmul(layer_2,weight['h3']),baises['b3'])
    layer_3 =  tf.nn.sigmoid(layer_3)
    
    layer_4 = tf.add(tf.matmul(layer_3,weight['h4']),baises['b4'])
    layer_4 =  tf.nn.sigmoid(layer_4) 
    
    out = tf.add(tf.matmul(layer_4,weight['Out']),baises['Out'])
    out = tf.nn.relu(out)
    return out

weight={
        'h1':tf.Variable(tf.truncated_normal([n_dim,hiddenlayer_1])),
        'h2':tf.Variable(tf.truncated_normal([hiddenlayer_1,hiddenlayer_2])),
        'h3':tf.Variable(tf.truncated_normal([hiddenlayer_2,hiddenlayer_3])),
        'h4':tf.Variable(tf.truncated_normal([hiddenlayer_3,hiddenlayer_4])),
        'Out':tf.Variable(tf.truncated_normal([hiddenlayer_4,n_classes]))
        }

baises={
        'b1':tf.Variable(tf.truncated_normal([hiddenlayer_1])),
        'b2':tf.Variable(tf.truncated_normal([hiddenlayer_2])),
        'b3':tf.Variable(tf.truncated_normal([hiddenlayer_3])),
        'b4':tf.Variable(tf.truncated_normal([hiddenlayer_4])),
        'Out':tf.Variable(tf.truncated_normal([n_classes])),
        }


init = tf.global_variables_initializer()
saver =   tf.train.Saver()
y = MultilayerPerceptron(x,weight,baises)
cost_function = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_,logits = y))
training_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost_function)
sess = tf.Session()
sess.run(init)
mse_history = []
accuracy_history = []

for epochs in range(100):
    sess.run(training_step,feed_dict = {x:train_x,y_:train_y})
    cost = sess.run(cost_function,feed_dict={x:train_x,y_:train_y})
    cost_history = np.append(cost_history,cost)
    correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(y_,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
    print(epochs)
    #print('Accuracy: ',(sess.run(accuracy,feed_dict={xx:test_x,y_:test_y})))
    pred_y = sess.run(y,feed_dict={x:test_x})
    #print(pred_y)
    mse = tf.reduce_mean(tf.square(pred_y-test_y))
    mse_=sess.run(mse)
    #print(mse_)
    mse_history.append(mse_)
    accuracy = (sess.run(accuracy,feed_dict={x:train_x,y_:train_y}))
    accuracy_history.append(accuracy)
    print('epoch : ',epochs,' - cost: ',cost,' - Mse: ',mse_,'- train accuracy',accuracy)
model_path = './model'
save_path = saver.save(sess,model_path)
print('Model saved in file: %s'%save_path)
import matplotlib.pyplot as plt
plt.plot(mse_history,'r')
plt.show()
plt.plot(accuracy_history)
