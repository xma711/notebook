#!/bin/bash

# for all the examples in this folder, 
# use this script to create the containers accordingly

container_name="ubuntu_test"
maxnum=10

if [[ ! $1 ]]; then
	echo "please enter 'create' or 'remove' containers"
	exit 1
fi

action=$1

if [[ ! $action = "create" ]] && [[ ! $action = "remove" ]]; then
	echo "the only choice is create or remove"
	exit 1
fi

if [[ $action = "remove" ]]; then
	echo "remove exisitng containers"
	docker ps -a > /tmp/docker_ps_tmp_all
	docker ps > /tmp/docker_ps_tmp

	for id in $( seq $maxnum );
	do
		if grep -q ${container_name}_${id} /tmp/docker_ps_tmp ;  then 
			echo ${container_name}_${id} is running. stop it.;
			docker stop ${container_name}_${id} 
		fi
		if grep -q ${container_name}_${id} /tmp/docker_ps_tmp_all ;  then 
                        echo ${container_name}_${id} exists. remove it.;
                        docker rm ${container_name}_${id} 
                fi
	done
	exit 0
fi

# from this point, it must be create
if [[ ! $2 ]]; then
	echo "please enter the number of containers wanted"
	exit 1
fi

num=$2

if [[ $num -gt $maxnum ]]; then
	echo "the number of containers cannot be more than 10"
	exit 1
fi

# create the containers
for id in $( seq $num )
do
	echo $id
	docker run -d --net dockernet --ip 192.168.10.10${id}  \
		-v ${HOME}/docker/ubuntu_test/.ssh:/root/.ssh \
		--name ${container_name}_${id} --restart always \
		rastasheep/ubuntu-sshd:16.04-customized
	if [[ $? -ne 0 ]]; then
		echo "there is an error when created container ${id}. Exit."
		exit 1
	else
		echo "successfully created container ${container_name}_${id}"
	fi
done
