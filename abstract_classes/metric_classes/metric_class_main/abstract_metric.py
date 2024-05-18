from abc import ABC, abstractmethod

class Metric(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def calculate(self, y_true, y_pred):
        """Calculate the metric based on true and predicted values."""
        pass

    @abstractmethod
    def get_config(self):
        """Return configuration or parameters of the metric."""
        pass
