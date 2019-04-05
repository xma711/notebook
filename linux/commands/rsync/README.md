Rsync is similar to scp, but it keeps the permission, ownership as well as symbolic links.

The usage is similar to scp too. 

Example: rsync -avzrl -e ssh ${COMMON_FILES_DIR}/* root@${IP_ADDR}:/

example rsync -avzrl -e ssh ./root root@192.168.1.1.201:/

-r: recursive

-l: keep symbolic link

-e ssh: via ssh


note that rsync also changes the mode and user of the directory that is rsynced to.

Need to set the right owner and the right mode before doing a rsync. 


On the other hand, copy won't change the ownership of the directories. note that copy can copy symbolic links too.

The timestamps of the files are important. the files with older timestamps won't be rsync-ed over to the destination
