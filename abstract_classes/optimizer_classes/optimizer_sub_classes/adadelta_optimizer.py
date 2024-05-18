from abstract_classes.optimizer_classes.optimizer_class_main.abstract_optimizer import Optimizer

class AdadeltaOptimizer(Optimizer):
    def __init__(self, rho=0.95, epsilon=1e-7):
        self.rho = rho
        self.epsilon = epsilon
        self.accum_grad = None
        self.accum_update = None

    def apply_gradients(self, gradients, variables):
        if self.accum_grad is None:
            self.accum_grad = [0] * len(gradients)
            self.accum_update = [0] * len(gradients)

        for i, (grad, var) in enumerate(zip(gradients, variables)):
            self.accum_grad[i] = self.rho * self.accum_grad[i] + (1 - self.rho) * (grad ** 2)
            update = grad * ((self.accum_update[i] + self.epsilon) ** 0.5 / (self.accum_grad[i] + self.epsilon) ** 0.5)
            var -= update
            self.accum_update[i] = self.rho * self.accum_update[i] + (1 - self.rho) * (update ** 2)

    def get_config(self):
        return {
            "rho": self.rho,
            "epsilon": self.epsilon
        }
