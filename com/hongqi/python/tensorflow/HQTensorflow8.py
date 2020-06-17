import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import datasets,layers,optimizers,Sequential,metrics

resnet = keras.applications.ResNet50(weights='imagenet',include_top=False)
resnet.summary()

x = tf.random.normal([4,224,224,3])
out = resnet(x)
#print('out.shape..',out.shape)

global_average_layer = tf.keras.layers.GlobalAveragePooling2D()
x = tf.random.normal([4,7,7,2048])
out = global_average_layer(x)
#print('out.shape...',out.shape)

fc = tf.keras.layers.Dense(100)
x = tf.random.normal([4,2048])
out = fc(x)
#print('out.shape.......',out.shape)

mynet = Sequential([resnet,global_average_layer,fc])
mynet.summary()

resnet.trainable = False
mynet.summary()