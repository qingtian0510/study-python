import tensorflow as tf

v1=tf.Variable(tf.constant(1.0,shape=[1]),name="v1")
v2=tf.Variable(tf.constant(2.0,shape=[1]),name="v2")

result=v1+v2

init_op=tf.initialize_all_variables()

saver=tf.train.Saver()
saver.export_meta_graph("path/to/mode.ckpt.meda.json",as_text=True)

with tf.Session() as sess:
    sess.run(init_op)
    saver.save(sess,"path/model.ckpt")
    # saver.restore(sess,"path/model.ckpt")
    # print sess.run(result)