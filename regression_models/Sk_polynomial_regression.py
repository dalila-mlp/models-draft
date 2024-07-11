import pickle
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

class PolynomialRegressionModel():
    def __init__(self, params):
        super().__init__()
        self.params = params
        degree = self.params.get_param("degree")
        self.model = make_pipeline(
            PolynomialFeatures(degree),
            LinearRegression()
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
        return 'O(n)'  # where n is the degree of the polynomial

    def model_length(self):
        # Length will depend on the degree and number of features
        return sum(len(coef) for coef in self.model.named_steps['linearregression'].coef_)

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
        linear_model = self.model.named_steps['linearregression']
        return {
            'coefficients': linear_model.coef_,
            'intercept': linear_model.intercept_
        }
