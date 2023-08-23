from store.data_s3_store import DataS3Store
from store.model_s3_store import ModelS3Store

def get_dataset_metadata_store():
    return DataS3Store()

def get_model_metadata_store():
    return ModelS3Store
