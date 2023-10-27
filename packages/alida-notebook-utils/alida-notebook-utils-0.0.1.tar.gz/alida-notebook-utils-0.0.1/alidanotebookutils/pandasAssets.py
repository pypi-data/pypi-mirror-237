from pandas import DataFrame
from .asset import Asset
import pandas as pd
from dsioutilities import Dataset


def load_as_pandas_dataframe(raw_data)-> DataFrame:

    asset = Asset(raw_data=raw_data)
    asset.set_properties_as_env()

    dataset = Dataset(name=str(raw_data['id']), dataset_type="tabular")

    if isinstance(dataset.get_path(), list):
        df = pd.concat([pd.read_csv(filename) for filename in dataset.get_path()])
    else:
        df = pd.read_csv(dataset.get_path())

    return df