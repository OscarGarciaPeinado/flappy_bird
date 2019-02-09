# coding: utf-8

import os
import numpy as np
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


class Perceptron:
    def __init__(self):
        num_input = 2
        n_hidden_layer_1 = 6
        num_classes = 2

        weights = {
            'h1': tf.Variable(tf.random_normal([num_input, n_hidden_layer_1])),
            'out': tf.Variable(tf.random_normal([n_hidden_layer_1, num_classes]))
        }
        biases = {
            'b1': tf.Variable(tf.random_normal([n_hidden_layer_1])),
            'out': tf.Variable(tf.random_normal([num_classes]))
        }
        self.input_placeholder = tf.placeholder(tf.float32, [None, num_input])
        self.layer_1 = tf.add(tf.matmul(self.input_placeholder, weights['h1']), biases['b1'])
        self.out_layer = tf.matmul(self.layer_1, weights['out']) + biases['out']
        self.result = tf.nn.softmax(self.out_layer)
        self.sess = tf.Session()
        self.sess.run(tf.global_variables_initializer())

    def predict(self, distance_x, distance_y):
        input_array = [[distance_x, distance_y], ]
        return self.sess.run(self.result, feed_dict={self.input_placeholder: input_array})
        # return tf.nn.softmax(self.neural_network)
