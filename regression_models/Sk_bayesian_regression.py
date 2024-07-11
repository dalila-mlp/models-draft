import pickle
from sklearn.linear_model import BayesianRidge

class BayesianRegressionModel():
    def __init__(self, params):
        super().__init__()
        self.params = params
        self.model = BayesianRidge(
            max_iter=self.params.get_param("max_iter"),
            tol=self.params.get_param("tol"),
            alpha_1=self.params.get_param("alpha_1"),
            alpha_2=self.params.get_param("alpha_2"),
            lambda_1=self.params.get_param("lambda_1"),
            lambda_2=self.params.get_param("lambda_2"),
            alpha_init=self.params.get_param("alpha_init"),
            verbose=self.params.get_param("verbose")
        )

    def getTypeModel(self):
        return "Sk"

    def train(self, x_train, y_train):
        self.model.fit(x_train, y_train)
        self.x_train = x_train
        self.y_train = y_train

    def predict(self, x_predict):
        self.x_predict = x_predict
        self.y_predict = self.model.predict(x_predict)
        return self.y_predict

    def flops_calculation(self):
        # FLOPS calculation for Bayesian Ridge Regression is a constant operation
        return 'O(1)'

    def model_length(self):
        # Number of parameters in Bayesian Ridge Regression
        return len(self.model.coef_) + 1  # +1 for the intercept

    def compil(self):
        # Not applicable for scikit-learn models, but included for compatibility
        pass

    def evaluate(self, x_evaluate, y_evaluate):
        self.x_evaluate = x_evaluate
        self.y_evaluate = y_evaluate
        return self.model.score(x_evaluate, y_evaluate)

    def save(self, model_id):
        with open(model_id, 'wb') as file:
            pickle.dump(self.model, file)

    def summary(self):
        return {
            'coefficients': self.model.coef_,
            'intercept': self.model.intercept_,
            'alpha': self.model.alpha_,
            'lambda': self.model.lambda_
        }
