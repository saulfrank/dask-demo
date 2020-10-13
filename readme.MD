### Install postgresql
````shell script
brew install postgresql
createuser -s postgres
brew install go
brew services restart postgresql
````

### Optimise write time
```postgresql
alter system set fsync='off';
alter system set synchronous_commit='off';
alter system set full_page_writes='off';
alter system set bgwriter_lru_maxpages=0;
alter system set wal_level='minimal';
alter system set archive_mode='off';
 alter system set work_mem='64MB';
alter system set checkpoint_segments=32;
alter system set max_wal_senders=0;
alter system set maintenance_work_mem='64MB';
alter system set shared_buffers='128MB';
```

### Migration sh executable
```shell script
cd goModel
chmod +x localMigrate.sh
```

### Install
```shell script
python -m pip install "dask[complete]" 
```

### Setup

Setup the scheduler
```shell script
dask-scheduler
```
Add workers
```shell script
dask-worker --nprocs=6 --memory-limit=2GB 127.0.0.1:8786 
```

### Workers dashboard

http://localhost:8787

### Test data
https://www.gov.uk/guidance/about-the-price-paid-data
https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads#single-file

### Reading

Storage: https://github.com/dask/dask-tutorial/blob/master/07_dataframe_storage.ipynb
CSV parrallel: https://stackoverflow.com/questions/40100176/can-dask-parralelize-reading-fom-a-csv-file
Share results, persist or re use elsewhere: https://distributed.dask.org/en/latest/publish.html


### Common commands
```shell script
head -3 pp-complete.csv
```
```python
# clear the client of any dataframes
client.restart()
client.list_datasets()
client.unpublish_dataset('prop_paid')
df = client.get_dataset('prop_paid')
```