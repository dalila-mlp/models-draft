from abstract_classes.optimizer_classes.optimizer_class_main.abstract_optimizer import Optimizer

class AdagradOptimizer(Optimizer):
    def __init__(self, learning_rate=0.01, epsilon=1e-7):
        self.learning_rate = learning_rate
        self.epsilon = epsilon
        self.cache = None

    def apply_gradients(self, gradients, variables):
        if self.cache is None:
            self.cache = [0] * len(gradients)

        for i, (grad, var) in enumerate(zip(gradients, variables)):
            self.cache[i] += grad ** 2
            var -= self.learning_rate * grad / (self.cache[i] ** 0.5 + self.epsilon)

    def get_config(self):
        return {
            "learning_rate": self.learning_rate,
            "epsilon": self.epsilon
        }
