import pickle
import datetime
from sklearn.svm import SVC


class SupportVectorMachine():
    def __init__(self, params):
        super().__init__()
        self.params = params
        self.model = SVC(
            C=self.params.get_param("C"),
            kernel=self.params.get_param("kernel"),
            gamma=self.params.get_param("gamma")
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

    def save(self):
        # Get the current script filename
        current_filename = "Sk_SVMClassifier_Dalila"

        # Get the current datetime
        current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        # Create a filename with the model name and current datetime
        filename = f"{current_filename}_{current_datetime}.pkl"

        with open(filename, 'wb') as file:
            pickle.dump(self.model, file)

    def summary(self):
        return {
            'support_vectors': self.model.support_,
            'n_support': self.model.n_support_
        }
