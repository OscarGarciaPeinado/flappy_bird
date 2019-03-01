import numpy as np


class NN:

    def __init__(self, n_input, n_hidden_layer, n_output, random_seed=1234):
        np.random.seed(random_seed)

        self.w1 = np.random.randn(n_input, n_hidden_layer)
        self.w2 = np.random.randn(n_hidden_layer, n_output)
        self.b1 = np.random.randn(1, n_hidden_layer)
        self.b2 = np.random.randn(1, n_output)

    def predict(self, distance_x, distance_y):
        arr = np.array([distance_x, distance_y])

        z1 = arr.dot(self.w1) + self.b1
        a1 = self.leaky_relu(z1)

        z2 = a1.dot(self.w2) + self.b2
        a2 = self.sigmoid(z2)

        return a2[0][0]

    @staticmethod
    def sigmoid(a):
        return 1. / (1. + np.exp(-a))

    @staticmethod
    def relu(a):
        return np.where(a > 0, a, 0)

    @staticmethod
    def leaky_relu(a):
        return np.where(a > 0, a, a * 0.01)

    @staticmethod
    def softmax(a):
        expA = np.exp(a)
        return expA / expA.sum()

    @staticmethod
    def tanh(a):
        return np.tan(a)
