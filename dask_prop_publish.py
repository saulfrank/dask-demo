from dask.distributed import Client
client = Client('127.0.0.1:8786')

import dask.dataframe as dd

print('load parquet')
df = dd.read_parquet('props.parquet')

print('persist dataframe')
df = client.persist(df)
#
print('publish dataframe')
df = client.publish_dataset(prop_paid=df)