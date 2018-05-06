import tensorflow as tf
#basic computational map
#dealing with constant
 
a = tf.constant(3.0,tf.float32)
b = tf.constant(4.0,tf.float32)
c = tf.constant(5.0,tf.float32)

d = tf.add(a,b)
e = tf.multiply(c,b)
f = tf.subtract(d,e)

sess = tf.Session()
outs = sess.run(f)
print(outs)
sess.close()