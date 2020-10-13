from dask.distributed import Client
client = Client('127.0.0.1:8786')

import dask.dataframe as dd

import csv
from io import StringIO

def psql_insert_copy(table, conn, keys, data_iter):
    """
    Execute SQL statement inserting data

    Parameters
    ----------
    table : pandas.io.sql.SQLTable
    conn : sqlalchemy.engine.Engine or sqlalchemy.engine.Connection
    keys : list of str
        Column names
    data_iter : Iterable that iterates the values to be inserted
    """
    # gets a DBAPI connection that can provide a cursor
    dbapi_conn = conn.connection
    with dbapi_conn.cursor() as cur:
        s_buf = StringIO()
        writer = csv.writer(s_buf)
        writer.writerows(data_iter)
        s_buf.seek(0)

        columns = ', '.join('"{}"'.format(k) for k in keys)
        if table.schema:
            table_name = '{}.{}'.format(table.schema, table.name)
        else:
            table_name = table.name

        sql = 'COPY {} ({}) FROM STDIN WITH CSV'.format(
            table_name, columns)
        cur.copy_expert(sql=sql, file=s_buf)

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

df = dd.read_csv('./propdata/pp-complete.csv', header=None, names=column_names)

print(df.head())

uristring = "postgresql://postgres@127.0.0.1:5432/mydb?sslmode=disable"
df.to_sql('test14', uristring, method=psql_insert_copy, parallel=True, if_exists='append')

# , parallel=True
# method=psql_insert_copy,




# print('run calc')
# x = client.submit(lambda a: a.shape, df).result()
#
# # print(df)
# print(x)
