from abc import ABC, abstractmethod

class Loss(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def calculate(self, y_true, y_pred):
        pass

    @abstractmethod
    def get_config(self):
        pass
