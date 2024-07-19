from tensorflow.keras.applications import ResNet50
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
import datetime



class ResNetClassifier():
    def __init__(self, params):
        super().__init__()
        self.params = params
        base_model = ResNet50(weights='imagenet', include_top=False)
        x = base_model.output
        x = GlobalAveragePooling2D()(x)
        x = Dense(self.params.get_param("hidden_units"), activation='relu')(x)
        predictions = Dense(self.params.get_param("num_class"), activation='softmax')(x)
        self.model = Model(inputs=base_model.input, outputs=predictions)

        for layer in base_model.layers:
            layer.trainable = self.params.get_param("trainable_base_layers")

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
