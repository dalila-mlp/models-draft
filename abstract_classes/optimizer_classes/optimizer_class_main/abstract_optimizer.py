from abc import ABC, abstractmethod

class Optimizer(ABC):
    @abstractmethod
    def __init__(self, **kwargs):
        pass

    @abstractmethod
    def apply_gradients(self, gradients, variables):
        pass

    @abstractmethod
    def get_config(self):
        pass
