from abstract_classes.optimizer_classes.optimizer_class_main.abstract_optimizer import Optimizer

class SGDOptimizer(Optimizer):
    def __init__(self, learning_rate=0.01):
        self.learning_rate = learning_rate

    def apply_gradients(self, gradients, variables):
        for g, v in zip(gradients, variables):
            v -= self.learning_rate * g

    def get_config(self):
        return {
            "learning_rate": self.learning_rate
        }
