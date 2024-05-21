import pickle
import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
import classeAbstraite



class ResNetClassifier():
    def __init__(self):
        super().__init__()
        self.model = ResNet50(weights='imagenet', include_top=False)
        x = base_model.output
        x = GlobalAveragePooling2D()(x)
        x = Dense(classeAbstraite.hidden_units, activation='relu')(x)
        predictions = Dense(classeAbstraite.num_classes, activation='softmax')(x)
        self.model = Model(inputs=base_model.input, outputs=predictions)

        for layer in base_model.layers:
            layer.trainable = classeAbstraite.trainable_base_layers

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

    def save(self, filename):
        self.model.save(filename)

    def summary(self):
        return self.model.summary()
