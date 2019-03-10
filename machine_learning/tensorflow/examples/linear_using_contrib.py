# follow the guide here: https://www.tensorflow.org/get_started/get_started

import tensorflow as tf
import numpy as np

# declare list of features. we only have one real-valued feature.
# there are many other types of columns that are more complicated and useful.
features = [tf.contrib.layers.real_valued_column("x", dimension = 1)]

# an estimator is the front end to invoke training (fitting) and evaluation (inference).
# there are many predefined types like linear regression, logistic regression,
# lnear classification, logistic classification, and provides an estimator that does linear regression
estimator = tf.contrib.learn.LinearRegressor(feature_columns = features)

# tensorflow provides many helper methods to read and set up data sets.
# here we use 'numpy_input_fn'.
# we have to tell the function how many batches of data (num_epochs) we want and how big each batch should be.
x = np.array([1.,2.,3.,4.])
y = np.array([0.,-1.,-2.,-3.])
input_fn = tf.contrib.learn.io.numpy_input_fn({"x":x}, y, batch_size=4, num_epochs = 1000)

# we can invoke 1000 training steps by invoking the 'fit' method and passing the training data set.
estimator.fit(input_fn = input_fn, steps=1000) # how do we need to input steps=1000 again?

# here we evaluate how well our model did.
# in a real example, we would want to use a separate validation and teesting data set to avoid overfitting
print ( estimator.evalute(input_fn = input_fn) )
