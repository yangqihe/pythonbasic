import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
#assert tf.__version__.startswith('2.')

a_ph = tf.placeholder(tf.float32,name='variable_a')
b_ph = tf.placeholder(tf.float32,name='variable_b')
c_op = tf.add(a_ph,b_ph,name='variable_c')
#print(a_ph,b_ph,c_op)

sess = tf.InteractiveSession()
init = tf.global_variables_initializer()
sess.run(init)
c_numpy = sess.run(c_op,feed_dict={a_ph:2,b_ph:4})
#print('a+b=',c_numpy)

a = tf.constant(2.)
b = tf.constant(4.)
#print('a+b=',a+b)



