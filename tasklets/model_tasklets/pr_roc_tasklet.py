from tasklets.base_tasklets import TaskletForModel


class ModelPredictor:
    def __init__(self):
        self._model = None
        self.load_model()

    def load_model(self):
        self._model = {}

    def predict(self, model_input):
        return self._model.predict(model_input)


class PrRocProcessor:
    @staticmethod
    def compute_pr(y_actual, y_pred):
        return []

    @staticmethod
    def compute_roc(y_actual, y_pred):
        return []


class PrRocTasklet(TaskletForModel):
    def _convert_dataset_df(self, dataset_df):
        return dataset_df

    def process(self, dataset_df, model):
        test_df = dataset_df
        y_pred = ModelPredictor().predict(test_df)
        y_actual = test_df
        pr_curve = PrRocProcessor.compute_pr(y_actual, y_pred)
        roc_curve = PrRocProcessor.compute_roc(y_actual, y_pred)
        return pr_curve, roc_curve

    def write_results(self, analysis_results):
        pass