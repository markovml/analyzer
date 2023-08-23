import pandas as pd

def read_dataset_as_df(dataset_metadata):
    pd.read_csv(dataset_metadata.path)
