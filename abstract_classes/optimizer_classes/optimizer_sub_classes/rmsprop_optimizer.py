from abstract_classes.optimizer_classes.optimizer_class_main.abstract_optimizer import Optimizer

class RMSpropOptimizer(Optimizer):
    def __init__(self, learning_rate=0.001, rho=0.9, epsilon=1e-7):
        self.learning_rate = learning_rate
        self.rho = rho
        self.epsilon = epsilon
        self.cache = None

    def apply_gradients(self, gradients, variables):
        if self.cache is None:
            self.cache = [0] * len(gradients)

        for i, (grad, var) in enumerate(zip(gradients, variables)):
            self.cache[i] = self.rho * self.cache[i] + (1 - self.rho) * (grad ** 2)
            var -= self.learning_rate * grad / (self.cache[i] ** 0.5 + self.epsilon)

    def get_config(self):
        return {
            "learning_rate": self.learning_rate,
            "rho": self.rho,
            "epsilon": self.epsilon
        }
