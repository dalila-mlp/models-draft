from abstract_classes.loss_classes.loss_class_main.abstract_loss import Loss

class MeanAbsoluteErrorLoss(Loss):
    def __init__(self):
        super().__init__()

    def calculate(self, y_true, y_pred):
        return (abs(y_true - y_pred)).mean()

    def get_config(self):
        return {}