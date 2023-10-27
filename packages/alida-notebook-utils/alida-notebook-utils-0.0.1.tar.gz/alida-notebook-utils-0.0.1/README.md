# alida-notebook-utils
This package implements a series of functions that helps quick download of ALIDA assets starting from raw DB objects.


## Getting started

### Pandas dataframe
For example, to download a pandas dataframe start by copying its raw DB object from ALIDA GUI. Then pass it to the following function. Print the result to test that it's working.

```python
from alidanotebookutils.pandasAssets import load_as_pandas_dataframe

df = load_as_pandas_dataframe(raw_data=raw_data)

print(df.sample())

```
### Spark dataframe
To download a spark dataframe start by copying its raw DB object from ALIDA GUI. Then pass it to the **init_spark** function to init Spark context.
```python
from alidanotebookutils.sparkAssets import init_spark, load_as_spark_dataframe

spark = init_spark(raw_data=raw_data)
```
Once spark is initialized:
```python
df = load_as_spark_dataframe(spark=spark, raw_data=raw_data)

print(df.show())
```
Alternatively you can skip spark initialization and run directly the second function without passing **spark** object to it.

### Files (and models) download
To download a file first get its raw DB object from ALIDA GUI.
Then:
```python
from alidanotebookutils.files import download_model

path = download_model(raw_data=raw_data, path="<your-desired-local-path>")
```