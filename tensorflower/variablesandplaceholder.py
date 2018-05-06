import tensorflow as tf

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)

c = tf.add(a,b)

sess = tf.Session()
c=sess.run(c,{a:[3,4],b:[5,6]})
#c is just a node and it will not take output at all
#output will be returned by the sess.run() method
#all kind of symbolic manipulation is just for making the computational graph
print(c)
sess.close()


