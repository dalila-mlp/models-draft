import pickle
from sklearn.svm import SVR

class SVRModel():
    def __init__(self, params):
        super().__init__()
        self.params = params
        self.model = SVR(
            kernel=self.params.get_param("kernel"),
            degree=self.params.get_param("degree"),
            gamma=self.params.get_param("gamma"),
            epsilon=self.params.get_param("epsilon")
        )

    def train(self, x_train, y_train):
        self.model.fit(x_train, y_train)
        self.x_train = x_train
        self.y_train = y_train

    def predict(self, x_predict):
        self.x_predict = x_predict
        self.y_predict = self.model.predict(x_predict)
        return self.y_predict

    def flops_calculation(self):
        return 'Complex calculation based on kernel'

    def model_length(self):
        # SVR doesn't have coefficients like linear models
        return 'Not applicable'

    def compil(self):
        pass

    def evaluate(self, x_evaluate, y_evaluate):
        self.x_evaluate = x_evaluate
        self.y_evaluate = y_evaluate
        return self.model.score(x_evaluate, y_evaluate)

    def save(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.model, file)

    def summary(self):
        return {
            'support_vectors': self.model.support_,
            'dual_coef': self.model.dual_coef_
        }
