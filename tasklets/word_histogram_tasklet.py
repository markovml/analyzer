from tasklets.base_tasklets import TaskletForData


class WordHistogram:
    @staticmethod
    def compute_word_histogram_for_dataset_df(dataset_df):
        pass


class WordHistogramTasklet(TaskletForData):
    def _convert_dataset_df(self, dataset_df):
        # NO-OP
        return dataset_df

    def process(self, dataset_df):
        WordHistogram.compute_word_histogram_for_dataset_df(dataset_df)

    def write_results(self, analysis_results):
        pass
