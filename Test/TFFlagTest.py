import tensorflow as tf


tf.app.flags.DEFINE_string('str_name', 'default_value', "description1")
tf.app.flags.DEFINE_integer('int_name', 10, "description2")
tf.app.flags.DEFINE_boolean('bool_name', False, "description3")

FLAGS = tf.app.flags.FLAGS


def main(_):
    print(FLAGS.str_name)
    print(FLAGS.int_name)
    print(FLAGS.bool_name)
    print("   sss")


if __name__ == '__main__':
    print(__name__)
    tf.app.run()