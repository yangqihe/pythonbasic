import tensorflow as tf
from tensorflow.keras import  datasets,layers,optimizers,Sequential,metrics

gpus = tf.config.experimental.list_physical_devices('gpu')
if gpus:
    try:
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu,True)
    except RuntimeError as e:
        print(e)
else:
    print('不支持GPU')

(xs,ys),_ = datasets.mnist.load_data()
print('datasets:',xs.shape,ys.shape,xs.min(),xs.max())

batch_size = 32

xs = tf.convert_to_tensor(xs,dtype=tf.float32) / 255.
db = tf.data.Dataset.from_tensor_slices((xs,ys))
db = db.batch(batch_size).repeat(30)

model = Sequential([layers.Dense(256,activation='relu'),
                    layers.Dense(128,activation='relu'),
                    layers.Dense(10)])
model.build(input_shape=(4,28*28))
model.summary()
optimizers = optimizers.SGD(lr=0.01)
acc_meter = metrics.Accuracy()

for step,(x,y) in enumerate(db):
    with tf.GradientTape() as tap:
        x = tf.reshape(x,(-1,28*28))
        out = model(x)
        y_onehot = tf.one_hot(y,depth=10)
        loss = tf.square(out-y_onehot)
        loss = tf.reduce_sum(loss) / x.shape[0]

    acc_meter.update_state(tf.argmax(out,axis=1),y)

    grads = tap.gradient(loss,model.trainable_variables)
    optimizers.apply_gradients(zip(grads,model.trainable_variables))

    if step % 200==0:
        print(step,'loss',float(loss),'acc:',acc_meter.result().numpy())
        acc_meter.reset_states()



