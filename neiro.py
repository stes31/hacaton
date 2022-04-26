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
            np.array([
                [r(), r(), r()],
                [r(), r(), r()],
                [r(), r(), r()],
                [r(), r(), r()],
                [r(), r(), r()],
                [r(), r(), r()]]),

            # hide-hide
            np.array([
                [r(), r(), r(), r(), r(), r()],
                [r(), r(), r(), r(), r(), r()],
                [r(), r(), r(), r(), r(), r()],
                [r(), r(), r(), r(), r(), r()],
                [r(), r(), r(), r(), r(), r()],
                [r(), r(), r(), r(), r(), r()]]),

            # hide-output
            np.array([
                [r(), r(), r(), r(), r(), r()],
                [r(), r(), r(), r(), r(), r()],
                [r(), r(), r(), r(), r(), r()]])]

        Neirons.neiron(self, np.array([[2], [3], [4]]))

    def neiron(self, neirons):
        for layer in range(self.hides_levels + 1):
            neirons = np.matmul(self.weights[layer], neirons)
            for level in range(len(neirons)):
                pass
            if neirons <= 0:
                neirons = 0.3 * (np.exp(neirons) - 1)
        self.neiro = neirons

    def learn(self, data_values):
        pass
    # обучение


x = Neirons()
print(*x.neiro)
