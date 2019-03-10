#!/bin/bash

if [[ ! $1 ]]; then
	echo "please enter the path to knowledge repo"
	exit 1
fi

path_k=$1

find ${path_k} -name "*.sh"
