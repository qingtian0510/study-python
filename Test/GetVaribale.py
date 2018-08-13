import tensorflow as tf

with tf.Session() as sess:
    v = tf.get_variable("v", [1])
    print sess.run(v.eval())


