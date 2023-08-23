from store.data_store import DataStore
from store.model_store import ModelStore

def get_dataset_metadata_store():
    return DataStore()

def get_model_metadata_store():
    return ModelStore
