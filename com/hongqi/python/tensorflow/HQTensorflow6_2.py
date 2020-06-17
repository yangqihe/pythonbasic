import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras import datasets
import os

x = tf.random.normal([2,28*28])
#print('##########',x)
w1 = tf.Variable(tf.random.truncated_normal([784,256],stddev=0.1))
#print('w1.....',w1)
b1 = tf.Variable(tf.zeros([256]))
#print('b1.....',b1)
o1 = tf.matmul(x,w1) + b1
#print('o1.....',o1)

x = tf.random.normal([4,28*28])
fc1 = layers.Dense(256,activation=tf.nn.relu)
#print('fc1.....',fc1)
fc2 = layers.Dense(128,activation=tf.nn.relu)
fc3 = layers.Dense(64,activation=tf.nn.relu)
fc4 = layers.Dense(10,activation=None)
h1 = fc1(x)
#print('h1...',h1)
h2 = fc2(h1)
#print('h2...',h2)
h3 = fc3(h2)
h4 = fc4(h3)

model = tf.keras.Sequential([
    layers.Dense(256,activation=tf.nn.relu),
    layers.Dense(128,activation=tf.nn.relu),
    layers.Dense(64,activation=tf.nn.relu),
    layers.Dense(10,activation=None)
])
out = model(x)
print('out',out)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

(x,y),_ = datasets.mnist.load_data()
x = tf.convert_to_tensor(x,dtype=tf.float32) / 255.
y = tf.convert_to_tensor(y,dtype=tf.int32)

print('x.....',x)