#!/bin/bash

# the following method cannot have variable in {}
for var in {1..5}
do
	echo $var
done


# another way.. however this starts from 1
num=6
for id in $( seq $num )
do
	echo $id
done


# one more way
for ((a=0; a<$num; a++))
do
	echo $a
done
