from abstract_classes.loss_classes.loss_class_main.abstract_loss import Loss

class MeanSquaredErrorLoss(Loss):
    def __init__(self):
        super().__init__()

    def calculate(self, y_true, y_pred):
        return ((y_true - y_pred) ** 2).mean()

    def get_config(self):
        return {}
