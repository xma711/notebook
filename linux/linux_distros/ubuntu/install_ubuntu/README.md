Install Ubuntu 16.04 alongside windows 10
------------------------------------------

Firstly, need to disable fastboot.

Also it is good to create a partition from the windows OS.

Then, check if windows 10 is boot using bios (legacy) or efi.  
From the start up setting, i can set the startup to both, bios-only or efi-only.
From here i can check if windows is in legacy mode or efi.

If windows uses legacy mode, then set the startup option to bios-only,
so that Ubuntu won't be booted using efi (by default it is efi).

Without doing this, later during installing Ubuntu,
it may not be able to see the windows OS.

Seems 16.04 is able to deal with this situation than 18.04.
When installing with 16.04, it will say that the installation start with EFI, which may not detect legacy-mode OS.
Just click 'Go Back' and install the Ubuntu in the free space created (or repartition).
(mount the partition or free space in the /)


install Ubuntu 15.10 alongside Windows 10 (obsolete)
-----------------------------------------

Read these references first before doing anything:

reference: http://askubuntu.com/questions/221835/installing-ubuntu-on-a-pre-installed-windows-with-uefi  

UEFI: https://help.ubuntu.com/community/UEFI (read this one very first)

http://askubuntu.com/questions/666631/how-can-i-dual-boot-windows-10-and-ubuntu-on-a-uefi-hp-notebook

maybe this reference too: https://www.linux.com/learn/tutorials/821007-how-to-install-linux-on-a-windows-machine-with-uefi-secure-boot


regarding HP Elite
----------------------

Not every monitor is recognized during the boot process. or maybe it is the issue of the cable.

My SyncMaster 2443 --- with a cable similar to VGA but it is another head (will update the exact model) works.

Never tried HDMI.


Install Ubuntu steps
----------------

Applicable to Ubuntu 15.10 (and maybe 15.04).

1. disable fast startup from windows (in power options): http://www.eightforums.com/tutorials/6320-fast-startup-turn-off-windows-8-a.html

2. shutdown computer

3. press Esc when restart

4. in the boot menu choose try Ubuntu 

5. then install Ubuntu like usual 

(suddenly recall that there is no choice for me to choose the partition size. how come?)


Possible problems
---------------------

Fail to install grub at the last step.  
This problem is encountered when i tried to install Ubuntu along windows 7.

Solution is to shutdown the laptop and repair grub.

Repair grub: http://howtoubuntu.org/how-to-repair-restore-reinstall-grub-2-with-a-ubuntu-live-cd

also if when installing Ubuntu, there is no such option "install Ubuntu alongside window", 
then go to windows and shrink the volume.  
Guide: https://technet.microsoft.com/en-us/library/gg309169.aspx
