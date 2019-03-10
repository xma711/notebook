Desktop or laptop
-------------

install debian from another linux system: https://www.debian.org/releases/stable/amd64/apds03.html.en


if ethernet not working, can try

ifconfig eth0 up

dhclient eth0


To get wifi works: http://www.linux.com/learn/answers/view/1628-how-do-i-get-debian-to-see-my-wifi

Step 1: find out what wifi hardware you have. If an internal wificard, lspci will show you what internal pci devices are installed including the wifi card. The list is long. However this line appeared near the end.

# lspci

02:00.0 Network controller: Intel Corporation WiFi Link 5100


Step 2: Modify /etc/apt/sources.list to handle potential non-free drivers. Login a root, su, and use your prefered editor to change this line in /etc/apt/sources.list from (substitute wheezy for jessie as for your installation)

deb http://ftp.us.debian.org/debian/ jessie main

to

deb http://ftp.us.debian.org/debian/ jessie main contrib non-free

# apt-get update


Step3: Since the above lsb command identified my usb wifi device as ralink, the following command identifies the firmware driver:


# apt-cache search Intel | grep wifi
firmware-iwlwifi - Binary firmware for Intel PRO/Wireless 3945 and 802.11n cards

Similarly intall the identified intel firmware:

# apt-get install firmware-iwlwifi


Then follow the wifi guide in ../wifi/README.md


Desktop - gnome desktop : install it based on: https://wiki.debian.org/Gnome

install debian for bbb
-------------------------------

http://elinux.org/BeagleBoardDebian

i downloaded https://rcn-ee.com/rootfs/2015-12-11/microsd/bone-debian-8.2-console-armhf-2015-12-11-2gb.img.xz 
(kernel: Linux arm 4.1.13-ti-r36 #1 SMP PREEMPT Fri Dec 11 00:44:56 UTC 2015 armv7l GNU/Linux),  
and installed it to a sd card using dd (sudo dd if=./bone-debian-8.2-console-armhf-2015-12-11-2gb.img of=/dev/sdX). 

the MT7601U wifi dongle works automatically, but lcd is all white and no display. in addition, the uart1 is not working due to conflict with lcd (apparently).

as a result, this debian image is not useful for me.


install debian-7.5 instead
-------------------------------

the kernel is probably v3.8


kernel v4.1x
----------------

btw, kernel v4.1x is another version (besides v3.8x) that supports device tree.   
the way of using device tree is similar. reference: http://voidnoise.co.uk/blog/?p=734  
to see the loaded capes: cat /sys/devices/platform/bone_capemgr/slots  
to load a cape: sudo sh -c "echo 'BB-UART4' > /sys/devices/platform/bone_capemgr/slots"

Beaglebone black
------------------------------

issues encountered:

1. problem with "insserv: Starting led_aging.sh depends on rmnologin and therefore on system facility `$all' which can not be true!"
when running apt-get upgrade  
solution:  http://unix.stackexchange.com/questions/198805/update-rc-d-doesnt-accept-the-header-of-a-script-file  
in fact, it is just to change the #!/bin/sh to #!/bin/sh -e

2. locale problem.  
solution: http://superuser.com/questions/885170/locales-broken-on-beaglebone-black-running-debian

3.  GPG error
solution: refer to http://elinux.org/Beagleboard:BeagleBoneBlack_Debian and search for GPG error
