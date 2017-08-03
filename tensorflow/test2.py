import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import numpy as np
import tensorflow as tf

x = np.random.rand(100).astype(np.float32)
y = 0.5*x*x + 1

weight = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
weight2 = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
weight3 = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
biase  = tf.Variable(tf.zeros([1]))
biase2 = tf.Variable(tf.zeros([1]))

linear_y = weight*x + biase
quadratic_y = weight2*x*x + weight3*x + biase2
linear_loss = tf.reduce_mean(tf.square(y-linear_y))
quadratic_loss = tf.reduce_mean(tf.square(y-quadratic_y))
optimizer = tf.train.GradientDescentOptimizer(0.5)
linear_train = optimizer.minimize(linear_loss)
quadratic_train = optimizer.minimize(quadratic_loss)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for step in range(201):
    sess.run(linear_train)
    sess.run(quadratic_train)
    if step%20 == 0:
        print(step, 'linear', sess.run(linear_loss))
        print(step, 'quadratic', sess.run(quadratic_loss))
