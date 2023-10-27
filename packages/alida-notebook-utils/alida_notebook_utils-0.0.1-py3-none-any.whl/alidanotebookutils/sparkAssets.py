from pyspark.sql import DataFrame
from .asset import Asset

try: 
    import pysparkutilities
except ImportError:
    import pip
    pip.main(['install', "pyspark-utilities"])

from pysparkutilities.spark_initializer import spark_initializer
from pysparkutilities import ds_initializer


def init_spark(raw_data, additional_config=[]):
    asset = Asset(raw_data=raw_data)
    asset.set_properties_as_env()

    spark = spark_initializer("jupyter", asset.properties_as_dict(), additional_config=additional_config)
    return spark

def load_as_spark_dataframe(raw_data, spark=None, additional_config=[])-> DataFrame:

    asset = Asset(raw_data=raw_data)
    asset.set_properties_as_env()

    if spark is None:
        init_spark(asset=asset, additional_config=additional_config)

    return ds_initializer.load_dataset(sc=spark, name=str(raw_data['id']), read_all=False)


