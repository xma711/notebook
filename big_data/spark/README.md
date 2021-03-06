General
--------------------

Quick setup for tutorial: use docker image from https://hub.docker.com/r/mesosphere/spark/  
then simply docker run -ti mesosphere/spark /bin/bash  
in the container, cd /opt/spark/dist  

then follow this tutorial to learn spark: https://spark.apache.org/docs/latest/quick-start.html


spark related
-------------------------

Activate spark shell using scala: ./bin/spark-shell (in spark/dist directory)

Scala APIs for 'dataset': https://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.Dataset

or better for me, using python shell: ./bin/pyspark

python APIs: https://spark.apache.org/docs/latest/api/python/index.html#pyspark.sql.DataFrame


master and slave
------------------------

To start a master: (in dir /opt/spark/dist/sbin) ./start-master.sh

to access the master: (assumed port 8080 of the container is mapped to the same port in host ) http://localhost:8080/

to start a slave: (remember to copy the url of the master exactly from the web of the master) ./start-slave.sh spark://6a35fa15eefc:7077

to stop the local slave: ./stop-slave.sh

to stop master: ./stop-master.sh



control client and cluster mode
------------------------------------

When using spark-submit to run an application, we can choose the deploy mode:
```
  --deploy-mode DEPLOY_MODE   Whether to launch the driver program locally ("client") or
                              on one of the worker machines inside the cluster ("cluster")
                              (Default: client).
```

for client mode, it means it simply runs the program 'directly' and locally.

For cluster mode, it should goes thru the cluster manager (which itself has multiple choices) and ultimately runs on worker(s).


Use YARN (Hadoop)
-------------------------

Reference: https://linode.com/docs/databases/hadoop/install-configure-run-spark-on-top-of-hadoop-yarn-cluster/

set up the Hadoop cluster as normal.
Then somehow link the Hadoop cluster with the spark (follow the tutorial)

btw even in this case, there are client and cluster modes.

Scala
----------------------

To quick scala: enter ':q'


some thinking
------------------------

Without setting up anything, is the path that spark sees in the host machine?
	- seems so.


