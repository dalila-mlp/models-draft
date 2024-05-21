import pickle
import classeAbstraite
from sklearn.neighbors import KNeighborsClassifier



class KNearestNeighbors():
    def __init__(self):
        super().__init__()
        self.model = KNeighborsClassifier(
            n_neighbors=classeAbstraite.n_neighbors,
            algorithm=classeAbstraite.algorithm,
            leaf_size=classeAbstraite.leaf_size
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
        # FLOPS calculation for Decision Tree depends on the tree structure
        # Providing a generic placeholder
        return 'Depends on tree structure'

    def model_length(self):
        # Number of parameters in Decision Tree
        return self.model.tree_.node_count

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
            'n_neighbors': self.model.tree_.n_neighbors,
            'leaf_size': self.model.tree_.leaf_size
        }
