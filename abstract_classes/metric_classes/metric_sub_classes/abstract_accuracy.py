from abstract_classes.metric_classes.metric_class_main.abstract_metric import Metric

class AccuracyMetric(Metric):
    def __init__(self):
        super().__init__()

    def calculate(self, y_true, y_pred):
        return (y_true == y_pred).mean()

    def get_config(self):
        return {}
