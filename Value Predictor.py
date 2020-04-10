import tensorflow as tf
import numpy as np
from tensorflow import keras

#forming simple one layer neural network
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

#forming optimizer `stochastic gradient descent` (sgd) and loss calculation
model.compile(optimizer='sgd', loss= 'mean_squared_error')

#relationship between x and y is y=3x+1
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-2.0, 1.0, 4.0, 7.0, 10.0, 13.0], dtype=float)

#this will run for given epochs value and predict the value and work with optimizer and loss for guessing the correct value
model.fit(xs, ys, epochs= 500)

#predict the y value for given x
print(model.predict([10.0]))




