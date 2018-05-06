import tensorflow as tf

#simple perceptron
w = tf.Variable(tf.random_normal([3,1]))
#baises = tf.variable(1,tf.float32)
t,f = 1,-1
x,y = 1,-1
baises = 1
#input and output
ip = tf.to_float([[t,t,1],[f,t,1],[t,f,1],[f,f,1]])
op = tf.to_float([[x],[y],[y],[y]])


#we gonna define step function
def step(x):
    is_greater = tf.greater(x,0)
    as_float = tf.to_float(is_greater)
    doubled = tf.multiply(as_float,2)
    return tf.subtract(doubled , 1)
output = step(tf.matmul(ip,w))
error = tf.subtract(op,output)

mse = tf.reduce_mean(tf.square(error))
deltas = tf.matmul(ip,error,transpose_a = True)
train = tf.assign(w,tf.add(w,deltas))
sess = tf.Session()
sess.run(tf.initialize_all_variables())

err,target = 1,0
#actually epoch are the number of iterration required to do manipulation
epoch,max_epochs = 0,10
while err>target and epoch<max_epochs :
    err,_ = sess.run([mse,train])
    print('epoch: ',epoch,' mean_squared_error: ',err,' weight: ',sess.run(w))
    epoch += 1
sess.close()
    