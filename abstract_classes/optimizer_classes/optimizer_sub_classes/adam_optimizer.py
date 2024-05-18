from abstract_classes.optimizer_classes.optimizer_class_main.abstract_optimizer import Optimizer

class AdamOptimizer(Optimizer):
    def __init__(self, learning_rate=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-7):
        self.learning_rate = learning_rate
        self.beta_1 = beta_1
        self.beta_2 = beta_2
        self.epsilon = epsilon
        self.m = None
        self.v = None
        self.t = 0

    def apply_gradients(self, gradients, variables):
        if self.m is None:
            self.m = [0] * len(gradients)
            self.v = [0] * len(gradients)

        self.t += 1
        lr_t = self.learning_rate * (1 - self.beta_2 ** self.t) ** 0.5 / (1 - self.beta_1 ** self.t)

        for i, (grad, var) in enumerate(zip(gradients, variables)):
            self.m[i] = self.beta_1 * self.m[i] + (1 - self.beta_1) * grad
            self.v[i] = self.beta_2 * self.v[i] + (1 - self.beta_2) * (grad ** 2)
            m_hat = self.m[i] / (1 - self.beta_1 ** self.t)
            v_hat = self.v[i] / (1 - self.beta_2 ** self.t)
            var -= lr_t * m_hat / (v_hat ** 0.5 + self.epsilon)

    def get_config(self):
        return {
            "learning_rate": self.learning_rate,
            "beta_1": self.beta_1,
            "beta_2": self.beta_2,
            "epsilon": self.epsilon
        }
