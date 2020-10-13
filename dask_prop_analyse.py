from dask.distributed import Client
client = Client('127.0.0.1:8786')

df = client.get_dataset('prop_paid')
xmin, xmax, xavg = client.compute(df.price.min(), df.price.max(), df.price.mean())

print(" min:",xmin, " max:", xmax, " avg:", xavg)