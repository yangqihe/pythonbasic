import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import datasets
import os

a = tf.random.normal([4,35,8])
b = tf.random.normal([6,35,8])
c = tf.concat([a,b],axis=0)
print('result..',c.shape)

x = tf.random.normal([2,784])
w1 = tf.Variable(tf.random.truncated_normal([784,256],stddev=0.1))
b1 = tf.Variable(tf.zeros([256]))
o1 = tf.matmul(x,w1) + b1
o1 = tf.nn.relu(o1)

print('o1...',o1.shape)