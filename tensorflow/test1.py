import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import numpy as np
import tensorflow as tf

x = np.random.rand(100).astype(np.float32)
y = 0.5*x + 1

weight = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
biase  = tf.Variable(tf.zeros([1]))

learn_y = weight*x + biase
loss = tf.reduce_mean(tf.square(y-learn_y))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for step in range(201):
    sess.run(train)
    if step%20 == 0:
        print(step, sess.run(weight), sess.run(biase))
