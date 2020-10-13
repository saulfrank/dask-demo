from dask.distributed import Client, LocalCluster

if __name__ == '__main__':

    cluster = LocalCluster() #n_workers=3
    cluster.scale(3) #scale to 3 workers
    client = Client(cluster)