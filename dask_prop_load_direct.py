from dask.distributed import Client
client = Client('127.0.0.1:8786')

import dask.dataframe as dd
# df = dd.read_csv('s3://dask-data/nyc-taxi/2015/*.csv',
#                  parse_dates=['tpep_pickup_datetime', 'tpep_dropoff_datetime'],
#                  storage_options={'anon': True})

print('read file')
# https://www.gov.uk/guidance/about-the-price-paid-data#download-options
column_names = [
    'id',
    'price',
    'transfer_date',
    'postcode',
    'property_type',
    'old_new',
    'duration',
    'primary_address_obj',
    'secondary_address_obj',
    'street',
    'locality',
    'city_town',
    'district',
    'county',
    'ppd_cat',
    'record_stat'
]

### dont set an index for saving parquet format
# df = dd.read_csv('./propdata/pp-complete.csv', header=None, names=column_names).set_index('id')

df = dd.read_csv('./propdata/pp-complete.csv', header=None, names=column_names)

# print(df.head())

print('persist dataframe')
df = client.persist(df)
#
print('publish dataframe')
df = client.publish_dataset(prop_paid=df)



# print('run calc')
# x = client.submit(lambda a: a.shape, df).result()
#
# # print(df)
# print(x)
