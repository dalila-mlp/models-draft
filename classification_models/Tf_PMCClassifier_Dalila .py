import pickle
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import classeAbstraite



class PMCClassifier():
    def __init__(self):
        super().__init__()
        self.model = Sequential()
        self.model.add(Dense(classeAbstraite.hidden_units, activation='relu', input_shape=(classeAbstraite.input_shape,)))
        for _ in range(classeAbstraite.num_hidden_layers - 1):
            self.model.add(Dense(classeAbstraite.hidden_units, activation='relu'))
        self.model.add(Dense(classeAbstraite.num_classes, activation='softmax'))
        self.model.compile(optimizer=classeAbstraite.optimizer,
                           loss=classeAbstraite.loss,
                           metrics=['accuracy'])

    def train(self, x_train, y_train, epochs, batch_size):
        self.model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size)
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
        return self.model.count_params()

    def compil(self):
        # Not applicable for scikit-learn models, but included for compatibility
        pass

    def evaluate(self, x_evaluate, y_evaluate):
        self.x_evaluate = x_evaluate
        self.y_evaluate = y_evaluate
        return self.model.score(x_evaluate, y_evaluate)

    def save(self, filename):
        self.model.save(filename)

    def summary(self):
        return self.model.summary()
