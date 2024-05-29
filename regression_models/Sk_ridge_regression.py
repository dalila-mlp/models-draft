from sklearn.linear_model import Ridge
import pickle

class RidgeRegressionModel(RegressionModel):
    def __init__(self, alpha=1.0):
        super().__init__()
        self.model = Ridge(alpha=alpha)

    def train(self, x_train, y_train):
        self.model.fit(x_train, y_train)
        self.x_train = x_train
        self.y_train = y_train

    def predict(self, x_predict):
        self.x_predict = x_predict
        self.y_predict = self.model.predict(x_predict)
        return self.y_predict

    def flops_calculation(self):
        # FLOPS calculation for Ridge Regression is similar to Linear Regression
        return 'O(1)'

    def model_length(self):
        # Number of parameters in Ridge Regression
        return len(self.model.coef_) + 1  # coefficients + intercept

    def compil(self):
        # Not applicable for scikit-learn models, but included for compatibility
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
            'coefficients': self.model.coef_,
            'intercept': self.model.intercept_
        }
