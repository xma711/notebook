install
---------------------

follow http://www.bogotobogo.com/Hadoop/BigData_hadoop_Install_on_ubuntu_single_node_cluster.php  
to install the hadoop to the ubuntu system.

the hadoop version can be changed to the most updated one, which can be downloaded from  
http://mirror.nus.edu.sg/apache/hadoop/core/ 
  
the java version also needs to be changed to the latest one in the system.  
in my case it is "JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre"

issue1: datanode not start  
	solution: Edit the value of namespaceID/clusterID in /usr/local/hadoop_store/hdfs/datanode/current/VERSION to match the corresponding value of the current NameNode in ${dfs.name.dir}/current/VERSION.
	or just remove the folder /usr/local/hadoop_store; and recreate the folder


## (obsolete) multi-node cluster: http://www.michael-noll.com/tutorials/running-hadoop-on-ubuntu-linux-multi-node-cluster/

for hadoop 2.7.0, set up multi-node cluser by: http://chaalpritam.blogspot.sg/2015/05/hadoop-270-multi-node-cluster-setup-on.html  
	- the master and slaves have exactly the same settings!  
	- but they refer to each other by their hostnames, which can be set in /etc/hosts in EACH machine    
	- if datanode is not running in master, start it by ./hadoop-daemon.sh stop datanode

to let nanenode exit from safe mode: ./hadoop dfsadmin -safemode leave


Hadoop distributed file system (HDFS)
--------------------------------

it is a bit like linux filesystem, starting with / root direcotry too.

switch to hduser first.. because /usr/local/hadoop has a user/group mode of hduser:hdoop.

to list the files inside HDFS in a particular directory, use command:  
	hadoop fs -ls full_path_to_directory (e.g. hadoop fs -ls /)  
	(Seems that we can also use "hdfs dfs -ls /")

to create/remove folder:  
	hadoop fs -mkdir/-rmr /direcotry/FOLDER_NAME

data transferred to/from host computer from/to the hdfs:
	hadoop fs -put/-get src dest

data transferred inside the hdfs:
	hadoop fs -cp/-mv  src dest

display a file's content:  
	hadoop fs -cat full_path_to_the_file

remove a file:  
	hadoop fs -rm full_path_to_the_file

as you can see, it is exactly the same as linux command, except there is a "hadoop fs -" in front.\


compile code and run code
----------------------------------

to compile hadoop code:  
	javac -classpath `hadoop classpath` -d destination_dir source_dir/Filename.java  
	(e.g. javac -classpath `hadoop classpath` -d WordCount/ ./WordCount.java)  
note that just keep the plain text 'hadoop classpath' and it is a backward quote ``, not forward.

to generate a jar file:  
	jar -cvf WordCount.jar -C destination_dir .  
	(note that there is a dot at the end)

launch job command:  
	hadoop jar PATH_TO_JAR_FILE classname parameters  
	(e.g. hadoop jar ./WordCount.jar WordCount /data/input  /data/output)  
note that the path of ./WordCount.jar refers to the path in the host computer, not hdfs;  
however, the /data/input and /data/output refers to the directories in hdfs.  
This is somewhat confusing so have to be careful about this.

display the job result:  
	hadoop fs –ls /data/output  
	hadoop fs ‐cat /data/output/part‐r‐00000

Note: if you run a job multiple times, need to 
delete the output folder every time before you 
launch the job: hadoop fs –rmr /data/output


run python in hadoop
-----------------------------

reference: http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/

after wrtting a mapper and a reducer, run this command:  
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -file ./mapper.py -mapper ./mapper.py -file ./reducer.py -reducer ./reducer.py -input /user/hduser/gutenberg/* -output /user/hduser/gutenberg-output

if hadoop-streaming-2.7.1.jar is not found, just search it by "find /usr/local/hadoop/ -name "hadoop-streaming*.jar"".

to get the filename of an input word, use os.environ["map_input_file"], e.g. print '%s\t%s' % (word, os.environ["map_input_file"])

to get the content of a file from hdfs: http://stackoverflow.com/questions/28139406/reading-writing-files-from-hdfs-using-python-with-subprocess-pipe-popen-give


run hadoop in a docker container
-----------------------------

follow docker repo: https://hub.docker.com/r/sequenceiq/hadoop-docker/  
or github repo: https://github.com/sequenceiq/hadoop-docker

anyway, it is to:  
	a. docker pull sequenceiq/hadoop-docker:2.7.1  
	b. docker run -d -p 2122:2122 sequenceiq/hadoop-docker:2.7.1 /etc/bootstrap.sh -d (use -d to keep the container running; use -bash to login to a bash, run with -ti)
	c. to access this node from another computer, add the ssh public key of another computer to this container (/root/.ssh/authorized_keys)


Note that when using the sequenceiq/hadoop-docker image, the default ssh port is 2122.  
even when i use ssh xma@my_computer_ip_addr, there won't be connection because the default port in this command is also 2122.  
the correct way is: ssh -p 22 xma@192.168.1.132

issue1: jps stuck... after starting the services using start-all.sh, and then type "jps", and then the terminal stops.   
nothing can be done to kill the zombie jps process..

To run the ubuntu-hadoop docker, follow: https://github.com/sequenceiq/docker-hadoop-ubuntu


some issues encountered
-----------------------------

hard disk no space!

solution (not may be the best): found out that there are many big folder in /app/hadoop/tmp/mapred/local/localRunner/hduser/jobcache .   
search them out: du -h  * | grep G  
and then delete them.

anyway jobtracter http://path:8088/cluster can be used to see nodes' status.

to see logs and hdfs, go to http://localhost:50070/
