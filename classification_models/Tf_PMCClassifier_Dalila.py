from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import datetime
from classeAbstraite import DynamicParams



class PMCClassifier():
    def __init__(self, params: DynamicParams):
        super().__init__()
        self.params = params
        self.model = Sequential()
        self.model.add(Dense(self.params.get_param("hidden_units"), activation='relu', input_shape=(
        self.params.get_param("input_shape"),)))
        for _ in range(self.params.get_param("num_hidden_layers") - 1):
            self.model.add(Dense(self.params.get_param("hidden_units"), activation='relu'))
        self.model.add(Dense(self.params.get_param("num_class"), activation='softmax'))
        self.model.compile(optimizer=self.params.get_param("optimizer"),
                           loss=self.params.get_param("loss"),
                           metrics=['accuracy'])

    def getTypeModel(self):
        return "Tf"

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

    def save(self):
        # Get the current script filename
        current_filename = "Tf_PMCClassifier_Dalila"

        # Get the current datetime
        current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        # Create a filename with the model name and current datetime
        filename = f"{current_filename}_{current_datetime}"

        self.model.save(filename)

    def summary(self):
        return self.model.summary()
