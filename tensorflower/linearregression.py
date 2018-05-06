import tensorflow as tf
import numpy as np

import matplotlib.pyplot as plt
#
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)
a = tf.Variable([.3] ,tf.float32)
b = tf.Variable([-.3],tf.float32)

l = a*X + b
loss = tf.reduce_sum(tf.square(tf.subtract(Y,l)))



grd = tf.train.GradientDescentOptimizer(.01)
train = grd.minimize(loss)



sess = tf.Session()
sess.run(tf.global_variables_initializer())



for i in range(500):
    sess.run(train,feed_dict={X:[1,2,3,4],Y:[2,3,4,5]})

print(sess.run([a,b]))







