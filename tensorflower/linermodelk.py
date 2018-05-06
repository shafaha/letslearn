import tensorflow as tf


w = tf.Variable([.3],tf.float32)
b = tf.Variable([-.3],tf.float32)

#input and output
x = tf.placeholder(tf.float32)
y=tf.placeholder(tf.float32)

#model
linear_model = w*x + b

#loss
squared_deltas = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_deltas)
#initializing the variables
init = tf.global_variables_initializer()
#optimozer

optimizer  = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)
'''
basicaly all the above work is just for the creating the computational graph.
and internally when ever we apply minimize function on the loss minimize function 
actually attack the w and b

'''

#creating the sessionns
sess = tf.Session()
sess.run(init)

#File_Writer = tf.summary.FileWriter('graph',sess.graph)
for i in range(1000):    
    value = sess.run(train,{x:[1,2,3,4],y:[0,-1,-2,-3]})
#since the w,b are tensor so the thatswhy for outputting we need to do that
    
print(sess.run([w,b]))
File_Writer = tf.summary.FileWriter('graph',sess.graph)
sess.close()