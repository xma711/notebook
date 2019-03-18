Gparted
------------------

Tutorial: http://www.dedoimedo.com/computers/gparted.html

gparted is like fdisk but may have more functionalities.


How to format a harddisk
-----------------------

Install gparted, then sudo gparted to open the gui.

Choose the harddisk, and then umount the partitions.

Then create new partition, choose the type: mbr or gpt (mbr can support a max of 2T, gpt doesn't have such limitation)

then later choose the filesystem type: ntfs (windows) or ext4 (linux)

then click tick to run the commands.


Resize windows partition using gparted
--------------------------------------------

Reference: https://howtoubuntu.org/how-to-resize-partitions-with-the-ubuntu-or-gparted-live-cd

in short, open gparted gui, right click on the windows partition, select resize, move the bar to get free space, then click apply.

If to make the free space its own partition, then use gparted to make it as a ext4 partition.
However, it will be owned by root and cannot be added files by local user.  
To enable this, use: sudo chmod ugo+wx /media/username/your_drive 
(reference: https://askubuntu.com/questions/90339/how-do-i-set-read-write-permissions-my-hard-drives)
