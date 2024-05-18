from abstract_classes.metric_classes.metric_class_main.abstract_metric import Metric

class PrecisionMetric(Metric):
    def __init__(self):
        super().__init__()

    def calculate(self, y_true, y_pred):
        true_positive = ((y_true == 1) & (y_pred == 1)).sum()
        predicted_positive = (y_pred == 1).sum()
        if predicted_positive == 0:
            return 0
        return true_positive / predicted_positive

    def get_config(self):
        return {}
