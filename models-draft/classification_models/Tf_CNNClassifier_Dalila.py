from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
import datetime



class CNNClassifier():
    def __init__(self, params):
        super().__init__()
        self.params = params
        self.model = Sequential()
        self.model.add(Conv2D(self.params.get_param("conv_filters"), kernel_size=self.params.get_param("kernel_size"), activation='relu', input_shape=self.params.get_param("input_shape_CNN")))
        self.model.add(MaxPooling2D(pool_size=self.params.get_param("pool_size")))
        for _ in range(self.params.get_param("num_conv_layers") - 1):
            self.model.add(Conv2D(self.params.get_param("conv_filters"), kernel_size=self.params.get_param("kernel_size"), activation='relu'))
            self.model.add(MaxPooling2D(pool_size=self.params.get_param("pool_size")))
        self.model.add(Flatten())
        self.model.add(Dense(self.params.get_param("hidden_units"), activation='relu'))
        self.model.add(Dense(self.params.get_param("num_classes"), activation='softmax'))
        self.model.compile(optimizer=self.params.get_param("optimizer"),
                           loss=self.params.get_param("loss"),
                           metrics=['accuracy'])

    def getTypeModel(self):
        return "Tf"

    def train(self, x_train, y_train, batch_size):
        history = self.model.fit(x_train, y_train, epochs=self.params.get_param("epochs"), batch_size=batch_size)
        self.x_train = x_train
        self.y_train = y_train

        return history

    def predict(self, x_predict):
        self.x_predict = x_predict
        self.y_predict = self.model.predict(x_predict)
        return self.y_predict

    def flops_calculation(self):
        # Placeholder for FLOPS calculation
        return 'Depends on model structure'

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

    def save(self, model_id):
        self.model.save(model_id)

    def summary(self):
        return self.model.summary()
