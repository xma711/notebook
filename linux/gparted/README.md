gparted
------------------

tutorial: http://www.dedoimedo.com/computers/gparted.html

gparted is like fdisk but may have more functionalities.


how to format a harddisk
-----------------------

install gparted, then sudo gparted to open the gui.

choose the harddisk, and then umount the partitions.

then create new partition, choose the type: mbr or gpt (mbr can support a max of 2T, gpt doesn't have such limitation)

then later choose the filesystem type: ntfs (windows) or ext4 (linux)

then click tick to run the commands.


resize windows partition using gparted
--------------------------------------------

reference: https://howtoubuntu.org/how-to-resize-partitions-with-the-ubuntu-or-gparted-live-cd

in short, open gparted gui, right click on the windows partition, select resize, move the bar to get free space, then click apply.

if to make the free space its own partition, then use gparted to make it as a ext4 partition.
however, it will be owned by root and cannot be added files by local user.  
to enable this, use: sudo chmod ugo+wx /media/username/your_drive 
(reference: https://askubuntu.com/questions/90339/how-do-i-set-read-write-permissions-my-hard-drives)
