import numpy as np
import math
import random

class NeuralNaum:
    def __init__(self):
        self.weights_to_output = [random.random() for i in range(5)] #quite clear. random returns in range [0;1]
        self.learning_rate = 0.003 #test has shown that this value is efficient
    def predict(self, inputs):
        answer = np.dot(inputs[:5], self.weights_to_output)
        print(self.weights_to_output)
        print(self.train(answer, inputs[5], inputs))
        return round(answer, 2)
    def train(self, expected, real, inputs):
        error = expected-real # error = 1/2*(expected-real)^2, so one of the part of a derivate looks exactly exp-real, read about chain rule
        for i in range(len(self.weights_to_output)):
            self.weights_to_output[i]-=error*self.learning_rate*inputs[i]
        return error**2/2
n = int(input("Elaborate number of tests: "))
obj = NeuralNaum()
for i in range(n):
    inputs = list(map(lambda x: float(x), input().split()))
    print(obj.predict(inputs))
