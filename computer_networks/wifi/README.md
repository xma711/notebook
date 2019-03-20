Find ssid from command line
------------------------------

Reference: https://askubuntu.com/questions/117065/how-do-i-find-out-the-name-of-the-ssid-im-connected-to-from-the-command-line

in short: use 'iwgetid' to get the ssid. 


Solve ubuntu wifi problem
----------------------

Just disable the power saving for wifi:

/sbin/iwconfig wlan0 power off


configure wifi using command line.
------------------------------

In archlinux or debian or gentoo, using reference https://wiki.archlinux.org/index.php/Wireless_network_configuration

command:

    wpa_supplicant -D nl80211,wext -i wlan0 -c <(wpa_passphrase "your_SSID" "your_key")

If this does not work, you may need to adjust the options. If connected successfully, continue in a new terminal (or quit wpa_supplicant with Ctrl+c and add the -B switch to the above command to run it in the background). WPA supplicant contains more information on options and on how to create a permanent configuration file for the wireless access point. 

In my case, i used 

    wpa_supplicant -B -D nl80211,wext -i wlp6s0 -c <(wpa_passphrase "SSID" "the_key")

in debian, also need to get an ip address:

    dhclient wlan0

in gentoo, get and ip address using:

    dhcpcd

Note that NetworkManager is easier to manage wifi or ethernet.


Using wifi dongle Model Number: UWN200. Inside: MediaTek MT7601 (Ralink 7601) Controller
-------------------------------

Reference: http://www.logicsupply.com/uwn200/

The guide to install the driver for linux can be found here: https://docs.google.com/document/d/1-CIGQYdk8ZhU3D3UCNn70jc7C9HdXvEZAsiNW71fGIE/edit

For archlinux, use command "*pacman -S dkms-mt7601*". so far this command works on kernel 3.18.1-1-ARCH. 
What i did actually is: install dkms-mt7601 first. reboot. not working. uninstall mt7601 and reinstall. copy the NetworkManager wifi conf file to the node. enable network manager. and then it works.
So the point is that i need to use networkManager rather than the original whatever manager in the node.

One possible solucion to make it work in kernel 3.8, is to upgrade the kernel from 3.8.13-31-ARCH to 3.8.13.39-ARCH. commands:

*pacman -Syy* (update package list)

*pacman -Syyu* (use *y
* if the system complains that "package-query: requires pacman<4.2 & yaourt: requires package-query>=1.4" )

*pacman-db-upgrade*

*reboot*

*pacman -S dkms-mt7601* (install the driver using pacman but this won't work..)

The problem with "pacman -S dkms-mt7601" is that the compilation of the kernel module fails. Error msg:

/var/lib/dkms/mt7601/v3.0.0.4/build/os/linux/../../os/linux/rt_linux.c:1121:37: error: request for member 'val' in something not a structure or union

/var/lib/dkms/mt7601/v3.0.0.4/build/os/linux/../../os/linux/rt_linux.c:1122:37: error: request for member 'val' in something not a structure or union


to solve this problem, follow the guide for installing the driver in ubuntu (http://askubuntu.com/questions/457061/ralink-148f7601-wifi-adaptor-installation): 

firstly, have to install headers: pacman -S linux-headers-am33x-legacy

sudo apt-get install linux-headers-generic build-essential git (not for bbb)

sudo apt-get install git

git clone https://github.com/porjo/mt7601.git 

cd mt7601/src

make

sudo make install

sudo mkdir -p /etc/Wireless/RT2870STA/

sudo cp RT2870STA.dat /etc/Wireless/RT2870STA/

sudo modprobe mt7601Usta

one issue: the node can ping internal ip addresses but cannot ping external ip addresses. -- the issue resolves by itself.. suddenly the node can ping google.com after a while


install mt7601u when there is no linux header to be found in archlinux repo
------------------------------------------------------
Main reference: https://headcrash.industries/reference/archlinux-kernel-compilation-on-beaglebone-black/

(in archlinux 3.8.13.31, create a normal user. add him to sudo group. create sudo group. enable sudo group to be able to run as root. type 'visudo' to edit sudoers file. uncomment this line "#%sudoers    ALL=(ALL) AL" so that it becomes "%sudoers    ALL=(ALL) AL")

in new user's home directory,

git clone git://github.com/archlinuxarm/PKGBUILDs.git

git checkout 5eb109d60511917d62fe0c42f5704b1d7d378bfa  ## to get to the 2014-08-27 version of archlinux

git branch 2014-08-27  
git checkout 2014-08-27

cd PKGBUILDs/core/linux-am33x-legacy

makepkg -Acs

this command will download the linux source codes first. at some point, it will stop and ask for sth.  
At this point, download compiler-gcc5.h from linux repo (commit number: a6c5170d1edea97c538c81e377e56c7b5c5b7e63) in the path linux_repo/include/linux/compiler-gcc5.h.

Copy compiler-gcc5.h to PKGBUILDs/core/linux-am33x-legacy/src/linux-3.8/include/linux/

(i cloned the whole linux repo before. the original one is https://github.com/torvalds/linux/tree/master/include/linux . one can just go to this link, and then checkout the right commit number and then download the raw file of compiler-gcc5.h)  
(reference: http://stackoverflow.com/questions/29925513/compile-a-linux-2-6-kernel-module-with-newer-compiler)

back to the terminal of command "makepkg -Acs" and press y or sth to continue compiling. (this step is necessary. otherwise the autoconf.h wont be generated.)

Bbb will try to compile the kernel and the header for somethime, until it will fail for some reasons. but it is okay.  
Check if directory PKGBUILDs/core/linux-am33x-legacy/src/linux-3.8/include/generated is created.   
Inside there should be these files: asm-offsets.h  autoconf.h  bounds.h  compile.h	mach-types.h  uapi  utsrelease.h (without autoconf.h, later compiling the mt7601u kernel module will lead to some complaints) (reference: http://serverfault.com/questions/568395/what-is-creating-the-generated-autoconf-h)  

then create a link at /usr/src/, as if i am installing the linux header: ln -s ~/PKGBUILDs/core/linux-am33x-legacy/src/linux-3.8 /usr/src/linux-3.8.13-31-ARCH

then create a link at /lib/modules/3.8.13-31-ARCH. ln -s /usr/src/linux-3.8.13-31-ARCH /lib/modules/3.8.13-31-ARCH/build  

the last two steps are exactly what is carried out when pacman install the linux header. of course, the link to linux-3.8 is not merely header, it has all the source codes. but more is okay, less will have problems.

Now go to mt7601/src folder, and then type make and follow other steps to get the kernel module installed.

When i do a "modprobe mt7601Usta" it may complain that the exec format not right, in this case, i just have to  
modprobe --force mt7601Usta   
to make it work.  
(reference: https://www.raspberrypi.org/forums/viewtopic.php?f=28&t=73005)

finally, i may need to write a systemd service file to enable it everytime the board reboots. (/usr/bin/modprobe --force mt7601Usta)
```
[Unit]
Description=Enable mt7601u wifi

[Service]
Type=simple
ExecStart=/usr/bin/modprobe --force mt7601Usta
Restart=none

[Install]
WantedBy=multi-user.target
```

Router
-----------------------

Router can be configured as a normal ethernet router, or a repeater.

A repeater forwards all requests to the main router.
