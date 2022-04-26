from picture import *
import numpy as np
from random import random as r


class Neirons:

    def __init__(self):
        self.neiro = None
        self.inputs = 3
        self.hides_levels = 2
        self.hiden = 6
        self.outputs = 3
        self.weights = [

            # input-hide
            np.array(
                [r(), r(), r()],
                [r(), r(), r()],
                [r(), r(), r()],
                [r(), r(), r()],
                [r(), r(), r()],
                [r(), r(), r()]),

            # hide-hide
            np.array(
                [r(), r(), r(), r(), r(), r()],
                [r(), r(), r(), r(), r(), r()],
                [r(), r(), r(), r(), r(), r()],
                [r(), r(), r(), r(), r(), r()],
                [r(), r(), r(), r(), r(), r()],
                [r(), r(), r(), r(), r(), r()]),

            # hide-output
            np.array(
                [r(), r(), r(), r(), r(), r()],
                [r(), r(), r(), r(), r(), r()],
                [r(), r(), r(), r(), r(), r()])]

    def neiron(self, x):
        for layer in range(self.hides_levels + 1):
            x = np.matmul(self.weights[layer], x)
        self.neiro = x

    def learn(self):
        pass
    # обучение

