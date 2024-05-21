import pickle
import classeAbstraite
from sklearn.svm import SVC


class SupportVectorMachine():
    def __init__(self):
        super().__init__()
        self.model = SVC(
            C=classeAbstraite.C,
            kernel=classeAbstraite.kernel,
            gamma=classeAbstraite.gamma
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
        # Placeholder for FLOPS calculation
        return 'Not directly applicable for SVM'

    def model_length(self):
        # Number of parameters in Decision Tree
        return len(self.model.support_)

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
            'support_vectors': self.model.support_,
            'n_support': self.model.n_support_
        }
