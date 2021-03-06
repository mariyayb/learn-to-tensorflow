
print("""

The difference between this lesson and the previous
is that we will be using a matrix for 'x' and 'y'.

Previously 'x' and 'y' were a single value.  For training
we fed in 1 value for each at a time.  Tensorflow allows
for, and excels at, working with matrixies.

In this example 'x' and 'y' will be a 1D matrix of variable length.

Instead of feeding each pair of values of x and y to Tensorflow
we can instead feed all the values at once.

""")

# -- imports --
import tensorflow as tf
from tensorflow.compat.v1 import Session, global_variables_initializer, placeholder
from tensorflow.compat.v1.train import GradientDescentOptimizer

# -- variables --
# f(x) = ax + b
a = tf.Variable(0.0)
x = placeholder(dtype=tf.float32, shape=[None])
b = tf.Variable(0.0)

# -- induction --
# f(x) = ax + b
fx = tf.add(tf.multiply(a, x), b)

# -- loss --
# but we want f(x) to equal y
y = placeholder(dtype=tf.float32, shape=[None])

# so we calculate a loss accordingly
loss = tf.reduce_mean(tf.square(fx - y))
learn = GradientDescentOptimizer(.01).minimize(loss)

# start a session
sess = Session()
# initialize the variables
sess.run(global_variables_initializer())

data_x = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
data_y = [0.1, 0.2, 0.4, 0.4, 0.6, 0.5, 0.7, 0.7, 0.9]


for iteration in range(1, 1001):
    sess.run(learn, feed_dict={x: data_x, y: data_y})
    if iteration == 1 or iteration == 10 or iteration == 100 or iteration % 1000 == 0:
        print("iteration", iteration,", total loss =", sess.run(loss, feed_dict={x: data_x, y: data_y}))

print("The equation is approximately f(x) =", sess.run(a), "* x +", sess.run(b))

print()