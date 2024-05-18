from abc import ABC, abstractmethod
from typing import List, Dict

class RegressionModel(ABC):
    def __init__(self):
        self.x_train = None
        self.y_train = None
        self.x_predict = None
        self.y_predict = None
        self.x_evaluate = None
        self.y_evaluate = None
        self.hyperparameters = []
        self.activation_functions = []
        self.epoch = None
        self.batch_size = None
        self.steps = None
        self.callback = None

    @abstractmethod
    def train(self, x_train, y_train):
        pass

    @abstractmethod
    def predict(self, x_predict):
        pass

    @abstractmethod
    def flops_calculation(self):
        pass

    @abstractmethod
    def model_length(self):
        pass

    @abstractmethod
    def compil(self):
        pass

    @abstractmethod
    def evaluate(self, x_evaluate, y_evaluate):
        pass

    @abstractmethod
    def save(self, filename):
        pass

    @abstractmethod
    def summary(self):
        pass
