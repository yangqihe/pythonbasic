import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import datasets,layers
import os

# a = tf.random.normal([4,35,8])
# print('a:',a)
# b = tf.random.normal([6,35,8])
# print('b:',b)
# c = tf.concat([a,b],axis=0)
# print('c:',c)

# x = tf.random.normal([2,784])
# w1 = tf.Variable(tf.random.truncated_normal([784,256],stddev=0.1))
# b1 = tf.Variable(tf.zeros([256]))
# o1 = tf.matmul(x,w1) + b1
# print('o1:',o1)
# o1 = tf.nn.relu(o1)
# print('o1:',o1)

# x = tf.random.normal([4,28*28])
# print('x:',x)
# fc = layers.Dense(512,activation=tf.nn.relu)
# print('fc:',fc)
# vars(fc)
# h1 = fc(x)
# print('h1:',h1)

# x = tf.random.normal([4,4])
# fc = layers.Dense(3,activation=tf.nn.relu)
# h1 = fc(x)
# print(h1)

# embedding = layers.Embedding(10000,100)
# print('embedding',embedding)
# vars(embedding)
# x = tf.ones([25000,80])
# print('x',x)
# print('...',embedding(x))

z = tf.random.normal([2,10])
#print('z',z)
y_onehot = tf.constant([1,3])
y_onehot = tf.one_hot(y_onehot,depth=10)
#print('y_onehot....',y_onehot)

loss = keras.losses.categorical_crossentropy(y_onehot,z,from_logits=True)
print('loss...',loss)
loss = tf.reduce_mean(loss)
print('loss...',loss)

criteon = keras.losses.CategoricalCrossentropy(from_logits=True)
loss = criteon(y_onehot,z)
print('loss...',loss)



