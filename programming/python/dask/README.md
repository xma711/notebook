Dask
----------------------

Reference: https://towardsdatascience.com/trying-out-dask-dataframes-in-python-for-fast-data-analysis-in-parallel-aa960c18a915

official docs: http://docs.dask.org/en/latest/dataframe.html

a Dask DataFrame is a large parallel DataFrame composed of many smaller Panda dataframes,
split along the index.

These panda dataframes may live on disk for larger-than-memory computing on a single machine,
or on many different machines in a cluster.

One dask dataframe operation triggers many operations on the constituent pandas dataframes.

A dask dataframe is partitioned row-wise, grouping rows by index value for efficiency.


Installation
------------------------

Anaconda by default has Dask.


Example (single machine)
----------------------------------

Example of reading file:  
(Btw this is an example on a single machine.)  
```
import dask.dataframe as dd
df = dd.read_csv("2014-*.csv")
df.head()

df2 = df[df.y == 'a'].x + 1
```

run on a distributed cluster
-------------------------------

When runing on a cluster, we need a 'Client' locally to connect to the cluster.

Example:   
```
from dask.distributed import Client
client = Client(...)
Df.x.sum().compute()
```
