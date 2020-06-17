import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers,Sequential,losses,optimizers,datasets

x = tf.constant([2.,1.,0.1])
layer = layers.Softmax(axis=-1)
print('layer..',layer)
print(layer(x))

def proprocess(x,y):
    x = tf.reshape(x,[-1])
    return x,y

(x,y),(x_test,y_test) = datasets.mnist.load_data()
x = tf.convert_to_tensor(x,dtype=tf.float32) / 255.
y = tf.convert_to_tensor(y,dtype=tf.int32)

x_test = tf.convert_to_tensor(x,dtype=tf.float32) / 255.
y_test = tf.convert_to_tensor(y,dtype=tf.int32)

train_db = tf.data.Dataset.from_tensor_slices((x,y))
train_db = train_db.shuffle(1000).map(proprocess).batch(128)

val_db = tf.data.Dataset.from_tensor_slices((x_test,y_test))
val_db = val_db.shuffle(1000).map(proprocess).batch(128)

x,y = next(iter(train_db))
print(x.shape,y.shape)

from tensorflow.keras import layers,Sequential
network = Sequential([
    layers.Dense(3,activation=None),
    layers.ReLU(),
    layers.Dense(2,activation=None),
    layers.ReLU()
])
x = tf.random.normal([4,3])
x_ = network(x)
#print('x_',x_)

layers_num = 2
network = Sequential([])
for _ in range(layers_num):
    network.add(layers.Dense(3))
    network.add(layers.ReLU())
network.build(input_shape=(None,4))
network.summary()

print('----------------')

for p in network.trainable_variables:
    print(p.name,p.shape)

network = Sequential([
    layers.Dense(256,activation='relu'),
    layers.Dense(128,activation='relu'),
    layers.Dense(64,activation='relu'),
    layers.Dense(32,activation='relu'),
    layers.Dense(10)
])
network.build(input_shape=(4,28*28))
network.summary()

from tensorflow.keras import optimizers,losses
network.compile(optimizer=optimizers.Adam(lr=0.01),
                loss=losses.CategoricalCrossentropy(from_logits=True),
                metrics=['accuracy'])

history = network.fit(train_db,epochs=5,validation_data=val_db,validation_freq=2)

print('history....',history.history)

network.sample_weights('weight.ckpt')
print('saved weights')
del network
network = Sequential([layers.Dense(256,activation='relu'),
                      layers.Dense(128,activation='relu'),
                      layers.Dense(64,activation='relu'),
                      layers.Dense(32,activation='relu'),
                      layers.Dense(10)
                      ])

network.compile(optimizer=optimizers.Adam(lr=0.01),
                loss=tf.losses.CategoricalCrossentropy(from_logits=True),
                metrics=['accuracy']
                )
network.load_weights('weight.ckpt')
print('loaded weight!')

global_average_layer = layers.GlobalAveragePooling2D()
x = tf.random.normal([4,7,7,2048])
out = global_average_layer(x)
print('############out.shape##############',out.shape)

fc = layers.Dense(100)
x = tf.random.normal([4,2048])
out = fc(x)
print('........out.shape.........',out.shape)



