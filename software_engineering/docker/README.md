Commands
-------------------

Useful tutorial: https://www.docker.com/tryit/

check version: *docker version*

search images relating to tutorial: *docker search tutorial*

download the tutorial image: *docker pull learn/tutorial*

start a container and run a command in it: *docker run learn/tutorial echo "hello world"*

install an app ping (not saving yet): *docker run learn/tutorial apt-get install -y ping*

to find the id of the container when running the process of installing the ping: *docker ps -l*

to save the container as a new image: *docker commit 6982a99 learn/ping*  (ie docker commit container_id repo_name)

run the new image: *docker run learn/ping ping www.google.com* (docker run takes a minimum of 2 arguments: 1 an image name and 2 the command you want to execute within that image)

to check a list of running containers: *docker ps* (if the container is not running, then it can not be found here)

inspect the running container: *docker inspect efefdc* (ie docker inspect running_container_id)

to show images in the local machine: *docker images* (the list of images is useful for obtaining the names of images)

to push a newly created image: *docker push learn/ping*  (ie docker push image_name)

to check docker info in the machine: *docker info*

container is like a box where a process runs inside it. the box contains everything the process might need, so it has the filesystem, system libraries, shell ans such. one starts a container by running a process in it.

Difference between a container id and image id: image is read-only template. its id should not change. container is like a box that a process has been running inside. so its id may change. isn't it?

Start an image with a process, there will be a container. to save the container as a new image, then commit container_id image_name to save it. and the cycle goes on.

To run a docker interactively, then it is *docker run -t -i image_name bash*

btw the option "--rm" allow the container to be deleted right after the temporary use

*docker ps -q* gets the container ids only. useful when killing all containers.


Useful options
--------------------------
Reference: https://docs.docker.com/reference/run/

--restart={always; on-failure; no}  
	no: Do not automatically restart the container when it exits. This is the default.   
	on-failure[:max-retries]: Restart only if the container exits with a non-zero exit status. Optionally, limit the number of restart retries the Docker daemon attempts.   
	always: Always restart the container regardless of the exit status. When you specify always, the Docker daemon will try to restart the container indefinitely.   

--cpu-shares=[e.g. 1024, which is default]  : cpu shares (relative weight)

By default, all containers get the same proportion of CPU cycles.  
To modify the proportion from the default of 1024, use the -c or --cpu-shares flag to set the weighting to 2 or higher.
The proportion will only apply when CPU-intensive processes are running. When tasks in one container are idle, other containers can use the left-over CPU time. (not very useful when trying to hard limit the cpu usage)   
On a multi-core system, the shares of CPU time are distributed over all CPU cores. Even if a container is limited to less than 100% of CPU time, it can use 100% of each individual CPU core.  

-m=[]  : memory limit (may not work)

--device=[e.g. /dev/ttyO2]: It allows you to specify one or more devices that will be accessible within the container.

--privileged


concepts
------------------------

Ref: http://blog.flux7.com/blogs/docker/docker-tutorial-series-part-1-an-introduction

docker daemon: service that sits on the host machine answering requests for services

docker client: user interface that allows communication between the user and the docker daemon

docker images: read-only templates that help launch docker containers

dockerfile: a file housing instructions that help automate image creation

docker container: responsible for actual running of applications and includes the operating system, user added files and meta-files

docker index: a centralized registry allowing backup of docker container images with public and private access permissions.


Namespaces: first level of isolation, making sure a process running in a container cannot see or affect processes running outside the container.

Control groups: the key component of LXC, have resource accounting and limiting as their key functionality

unionFS (fileSystem): serves as a building blocks of containers. it creates layers, and thereby, accounts for docker's lightweight and fast features.



2 steps to run any application
-------------------------------

Step 1: build an image

an image holds all the information needed to bootstrap a container, including what processes to run and the configuration data. 
Every image starts from a base image, and a template is created by using the instructions that are stored in the dockerfile. 
For each instruction, a new layer is created on the image.

Once images are created, they can be pushed to the central registry, the Docker Index. 


Step 2: run the container

when a container sis launched, a read-write layer is added to the top of the image. 
After appropriate network and ip address allocation, the desired application can now be run inside the container.

Btw, to make sure the container keeps running, the app command have to be in a infinite loop, otherwise the container will exit immediately. 


Regarding volume
-----------------------------

Reference: http://crosbymichael.com/advanced-docker-volumes.html

a volume is a directory located outside of the root filesystem of your container.  
This allows you to import the directory in other containers.  
You can also use volumes to mount directories from your host machine inside a container.

E.g. *docker run -v /www ubuntu echo yo* : this command creates a folder in the host machine and mount it in /www inside the container  
you can use "*docker inspect container_id*" to see where the folder locates in the host machine.

To create new volume mounted to your host machine:  
*docker run -v /host/logs:/container/logs ubuntu echo momma* (question: is it container mounts the directory from the hostmachine or the host machine mount the directory from the container?)




Docker on bbb (archlinux)
---------------------------

Update system first:

*pacman -Syy*

then *pacman -S docker lxc*
    
*systemctl start docker*

double check the system date is upto date. otherwise docker will complain the certificate has expired.

To expose the serial port, can use:

*docker run  --privileged -v /dev/ttyO2:/dev/ttyO2 image_name execute_command*

to run it interactively, then it is *docker run -t -i --privileged -v /dev/ttyO2:/dev/ttyO2 image_name bash*


enable systemd for docker in bbb (archlinux)
---------------------------------

Reference: http://developerblog.redhat.com/2014/05/05/running-systemd-within-docker-container/

need to run in a privileged container.  
Need to add the cgroup file system to the container using "–v /sys/fs/cgroup:/sys/fs/cgroup:ro"  
need to remove unit file links from the /lib/systemd/system/*wants/ and  /etc/systemd/system/*wants/ directories  

a dockerfile something like the follows will enable systemd:
```
FROM armv7/armhf-archlinux

ENV container docker

RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done); \
rm -f /lib/systemd/system/multi-user.target.wants/*;\
rm -f /etc/systemd/system/*.wants/*;\
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*;\
rm -f /lib/systemd/system/anaconda.target.wants/*;
VOLUME [ "/sys/fs/cgroup" ]
CMD ["/usr/sbin/init"]
```

to run this container, use command:  
docker run --privileged -ti -v /sys/fs/cgroup:/sys/fs/cgroup:ro image_name

if encountered issue "Failed to get D-Bus connection: Operation not permitted",  
most likely it is because the image's default command is overridden.  
The default command is /usr/sbin/init, and if i run it as /bin/bash, this command won't be executed.  
The correct way is to generate a new image with the loaded systemd files with the same default command.

Another way to test is to docker run the image first, and log in to the container using "docker exec -ti container_id /bin/bash"  
and then add the service file and start it.

(cannot do it the other way, i.e. start the image with /bin/bash and then run "/usr/sbin/init". 
Otherwise there will be an error: "Trying to run as user instance, but the system has not been booted with systemd.")


Control in-built leds and gpio on bbb using docker
-----------------------------

Replace the docker volume /sys/devices/ocp.3/gpio-leds.8/leds by the host volume. (not /sys/class/leds, inside which the folders are symbolic links to /sys/devices/ocp.3/gpio-leds.8/leds)

e.g.   
Docker run --rm -ti -v /sys/devices/ocp.3/gpio-leds.8/leds:/sys/devices/ocp.3/gpio-leds.8/leds image_name /bin/bash (no need privileged)

then one can control the leds as if it is in the host machine:  
echo none > /sys/class/leds/beaglebone\:green\:usr0/trigger  
echo timer > /sys/class/leds/beaglebone\:green\:usr1/trigger  
etc. (reference: http://robotic-controls.com/learn/beaglebone/beaglebone-black-built-leds)

to control gpios (need to map 2 volumes):  
e.g. docker run --rm -ti -v /sys/devices/virtual/gpio:/sys/devices/virtual/gpio -v /sys/class/gpio:/sys/class/gpio  86421925a2d4 /bin/bash

to make things simpler but less safe, one can mount the whole /sys directory to the docker container then the container can control all leds and gpios. of course, this is not very safe.

In fact, as long as the container is run with --privileged, then the whole /sys directory can be controlled by the docker container already.. this is super unsafe because a container can misbehave and destroy the host machine. and now the container is no longer unable to affect the host system..


Privileged mode
---------------------------
Reference: https://docs.docker.com/reference/run/

"By default, Docker containers are "unprivileged" and cannot, for example, run a Docker daemon inside a Docker container. 
This is because by default a container is not allowed to access any devices, but a "privileged" container is given access to all devices."

"When the operator executes docker run --privileged, Docker will enable to access to all devices on the host as well as 
set some configuration in AppArmor or SELinux to allow the container nearly all the same access to the host as processes running outside containers on the host. "

"If you want to limit access to a specific device or devices you can use the --device flag. It allows you to specify one or more devices that will be accessible within the container."
 

Ssh among containers and real machines
---------------------------------

1. ssh to another computer: use the same cmd: ssh user@ip

ssh to the local computer: use the local computer's ip addr: ssh root@local_ip (not 127.0.0.1, but 192.168.1.x)


2. ssh to docker container from another computer:

from host computer, it is easy. just treat it as another computer.  
Ssh username@172.17.0.2 
	- (username is the user in the container, not host machine)  
	- (the ip address of the container can be contained by logging into the container and do a ifconfig)

from another computer, the container has to be started with proper port mapping.  
Assume the ssh port is 22 for the container, then the container should be started something like:  
docker run -p 2222:22 image_name  
then the external computer can access the container by: ssh -p 2222 username@host_ip_addr

3. ssh from one container to another:

run both containers with port mapping (e.g. docker run -p 2222:22 image_name), then  
ssh -p 2222 username@host_ip_addr  
from one container to another.  
Host_ip_addr is the ip address of the host where a container runs.

Dockerfile
---------------------


When building the dockerfile, i can add "-t repo_name" to indicate which repo the newly created image belong to.

E.g. *sudo docker build -t xma711/ubuntu:extra_tag .*

and then i can do a "sudo docker push xma711/ubuntu" to push the image to my repo.

Sometimes need to do a "sudo docker login" first

ENTRYPOINT:  
The ENTRYPOINT of an image is similar to a COMMAND because it specifies what executable to run when the container starts, 
but it is (purposely) more difficult to override. 
The ENTRYPOINT gives a container its default nature or behavior, 
so that when you set an ENTRYPOINT you can run the container *as if it were that binary, complete with default options*, 
and you can pass in more options via the COMMAND. 

CMD:
a default fixed command (+ arguments) for the image.



Docker repo in docker hub
----------------------------

Like GitHub, i can create a repo in docker hub.

A repo will store a history of commits. 



Private docker hub
----------------------

Reference: https://registry.hub.docker.com/_/registry/

simply docker pull the official registry and run it in the local computer.

Pull and run the registry: *docker run -p 5000:5000 registry*

to commit to the local registry, i need to re-tag an image and push it.

For example, i have this archlinux_x86 in my computer. Then:

*sudo docker tag archlinux_x86:latest localhost:5000/archlinux_x86*

*sudo docker push localhost:5000/archlinux_x86*

from a remote machine, the image has to be tagged as ip_local_hub:port/image_name.

E.g. *sudo docker tag archlinux_x86:latest 192.168.1.132:5000/archlinux_x86*

before the image can be pushed to the local docker hub, one needs to stop the docker daemon and restart it with "--insecure-registry ip:port"

*sudo docker -d --insecure-registry 192.168.1.132:5000*

and finally, the image can be pushed to the local hub with *sudo docker push 192.168.1.132:5000/archlinux_x86*  
reference: http://stackoverflow.com/questions/26710153/remote-access-to-a-private-docker-registry

to get info from private registry: https://docs.docker.com/v1.6/reference/api/registry_api/

to list all images in a private docker hub: *curl 192.168.1.125:5000/v1/search* (ie curl [host:port]/v1/search)  
another way is "docker search 192.168.1.125:5000/library" which display the repositories in a neater way.
(ref: http://stackoverflow.com/questions/23733678/how-to-search-images-from-private-1-0-registry-in-docker)

to list all tags under an image in a private docker hub: *curl http://192.168.1.174:5000/v1/repositories/library/armhf-archlinux/tags | python -m json.tool"

Btw this is a useful tutorial: https://www.digitalocean.com/community/tutorials/how-to-set-up-a-private-docker-registry-on-ubuntu-14-04

To use a GUI to manage to repository, follow: https://github.com/atc-/docker-registry-ui  
in short, just run docker run -d -p 8080:8080 atcol/docker-registry-ui  
and then add a registry using the native ip address (cannot use 'localhost' because the ip address is used inside the container)

change docker daemon options
-----------------------------

In ubuntu 14.04, docker is managed by upstart.

The configuration file is at /etc/default/docker;   
therefore docker options can be modified by this file, and then restart docker

btw upstart seems to use the /etc/init/docker.conf to start the docker daemon,
which in turn use the options specified in /etc/default/docker

to allow a computer to push/ pull images from a private registry, 
add "-H tcp://127.0.0.1:2375 -H unix:///var/run/docker.sock --insecure-registry <REGISTRY_HOSTNAME>:5000" to /etc/default/docker.

In ubuntu 15.04 onward, docker is managed by systemd.  
One direct way is to modify the systemd service file.  
Use "systemctl status docker" to find out where the service file is,
then simply add "-H tcp://127.0.0.1:2375 -H unix:///var/run/docker.sock --insecure-registry <REGISTRY_HOSTNAME>:5000" to the starting line


docker as a vm
--------------------------

Just realize docker can be used as if it is a vm, when running it in the interactive mode.

But need to remember to commit the changes after come out, otherwise all changes will be lost. or the container id has to be remembered.

Docker container may be able to limit the cpu usage by any programs, which can reduce energy consumption

docker tips
----------------------------
Have not had time to read:  
http://nathanleclaire.com/blog/2014/07/12/10-docker-tips-and-tricks-that-will-make-you-sing-a-whale-song-of-joy/


shipyard
------------------------
Reference: https://shipyard-project.com/  
"Built on the Docker cluster management toolkit Citadel, Shipyard gives you the ability to manage Docker resources including containers, hosts and more."

To start the shipyard dashboard manually:  
docker run -it -d --name shipyard-rethinkdb-data --entrypoint /bin/bash shipyard/rethinkdb -l  
docker run -it -P -d --name shipyard-rethinkdb --volumes-from shipyard-rethinkdb-data shipyard/rethinkdb  
docker run -it -p 8080:8080 -d --name shipyard --link shipyard-rethinkdb:rethinkdb shipyard/shipyard  

now shipyard can be accessed at http://localhost:8080

to add an engine (engine means a host machine that runs docker daemon), click add engine and enter http://ipaddress:2375.

However, this host machine has to run the docker daemon as "docker -H tcp://127.0.0.1:2375 -H unix:///var/run/docker.sock -d" (or -H tcp://0.0.0.0:2375)

in ubuntu 14.04, the docker options can be modified at file /etc/default/docke:   
DOCKER_OPTS="-H tcp://0.0.0.0:2375 -H unix:///var/run/docker.sock"

in computers using systemd, find out where the systemd file is and then add the options to the line.


Find out which interface belongs to which container
-----------------------------------------------------------

Reference: https://stackoverflow.com/questions/37860936/find-out-which-network-interface-belongs-to-docker-container

commands:  
docker exec -it my-container cat /sys/class/net/eth1/iflink  
ip ad | grep 123


regarding docker network
---------------------------------------

Reference: https://stackoverflow.com/questions/35194761/how-to-let-different-docker-containers-talk-to-each-other-without-exposing-the-p/35196493#35196493

by default docker daemon adds a network adapter docker0, usually uses 172.17.0.1.  
All containers are by default connected to this network in incremental ip address.

However, we can always create a new network adopter and connect a new container to the new network.


The official reference: https://docs.docker.com/engine/userguide/networking/

to list the networks docker created: docker network ls

docker creates 3 networks by default, one bridge (i.e. docker0), one host and one "none"

if using the "none" network, the container will lack a network interface.

The host network adds a container on the host's network stack. 
There is no isolation between the host machine and the container. 
In short, the container has the same ip address as the host machine. 

To inspect a network, use: docker network inspect network_name (e.g. docker0)

to remove a self-defined network, use: docker network rm network_name (e.g. app_default)
