from abc import ABC, abstractmethod


class DataTaskletRunRequest:
    dataset_id: str


class ModelTaskletRunRequest:
    model_id: str
    dataset_id: str


class Tasklet(ABC):
    def __init__(self):
        self.settings = get_settings()
        self.context = load_context()

    @abstractmethod
    def run(self, run_request):
        pass

    def process_new_run(self, tasklet_request):
        self._create_new_tasklet()
        try:
            self.run(tasklet_request.get_run_request())
        except Exception:
            self._mark_tasklet_as_failed()

        self._mark_tasklet_as_succeeded()

    def _create_new_tasklet(self):
        # some implementation
        pass

    def _mark_tasklet_as_failed(self):
        # some implementation
        pass

    def _mark_tasklet_as_succeeded(self):
        # some implementation
        pass


class TaskletForData(Tasklet):
    def __init__(self):
        super().__init__()
        self._dataset_metadata_store = get_dataset_metadata_store()

    def run(self, run_request: DataTaskletRunRequest):
        dataset_metadata = self._dataset_metadata_store.get_dataset_metadata(dataset_id=run_request.dataset_id)
        dataset_df = self.read_dataset(dataset_metadata)
        analysis_results = self.process(dataset_df)
        self.write_results(analysis_results)

    def read_dataset(self, dataset_metadata):
        dataset_df = dataset_reader.read_dataset_as_df(dataset_metadata)
        return self._convert_dataset_df(dataset_df)

    @abstractmethod
    def _convert_dataset_df(self, dataset_df):
        pass

    @abstractmethod
    def process(self, dataset_df):
        pass

    @abstractmethod
    def write_results(self, analysis_results):
        pass


class TaskletForModel(Tasklet):
    def __init__(self):
        super().__init__()
        self._dataset_metadata_store = get_dataset_metadata_store()
        self._model_metadata_store = get_model_metadata_store()

    def run(self, run_request: ModelTaskletRunRequest):
        dataset_metadata = self._dataset_metadata_store.get_dataset_metadata(dataset_id=run_request.dataset_id)
        model_metadata = self._model_metadata_store.get_model_metadata(model_id=run_request.model_id)
        dataset_df = self.read_dataset(dataset_metadata)
        model = self.load_model(model_metadata)
        analysis_results = self.process(dataset_df, model)
        self.write_results(analysis_results)

    def read_dataset(self, dataset_metadata):
        dataset_df = dataset_reader.read_dataset_as_df(dataset_metadata)
        return self._convert_dataset_df(dataset_df)

    @abstractmethod
    def _convert_dataset_df(self, dataset_df):
        pass

    def load_model(self, model_metadata):
        pass

    @abstractmethod
    def process(self, dataset_df, model):
        pass

    @abstractmethod
    def write_results(self, analysis_results):
        pass
