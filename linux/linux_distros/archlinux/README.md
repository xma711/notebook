Install Archlinux from Gentoo
--------------------------------

Install Archlinux from Gentoo (an existing Linux) following the guide in:
https://wiki.archlinux.org/index.php/Install_from_Existing_Linux

the steps are roughly:

0. start Gentoo

1. install the Archlinux filesystem in /temp

2. chroot to /temp/Archlinux

3. init pacman keyring

4. mount the intended partition to /mnt in the chroot environment

5. (maybe needed: create boot folder and home folder in /mnt) pacstrap /mnt base to install the filesystem as well as boot to the partition.

6. configure the system

7. go to Gentoo and add one entry to the grub (see [README.md for grub2](../../multi-boot/grub2/README.md))

8. reboot and choose Archlinux. if the network is not on, start the network by "ip link set eth0/enp8s0[interfaceName] up" and then "dhcpcd". reference: https://wiki.archlinux.org/index.php/Network_configuration. to use ifconfig, pacman -S net-tools


Pacman
-----------

To see pacman manual: man pacman

Pacman has operations and options. operations are just like options with capitals, like -S means sync, -R means remove etc. 
Options are used to affect operations, so the same option can mean different things with different operations.

To refresh the package list: *pacman -Syy* (-S: synchronize; -Sy: refresh)

To update the whole system: *pacman -Syu* (-Su: sysupgrade)

To install a package: *pacman -S package_name*

To search a package: *pacman -Ss package_name*


System upgrade issues
-------------------------

1. error package-query: requires pacman"<"4.2  
	- solution: remove and reinstall yaourt and package-query: pacman -Rns yaourt; pacman -Rns package-query
	- reference: http://bbs.archbang.org/viewtopic.php?id=5216

2. if sg's mirror address not working, can try this: Server = http://sg.mirror.archlinuxarm.org/$arch/$repo 
(change it in /etc/pacman.d/mirrorlist)

3. ca-certificates-utils error.

```
(211/211) checking for file conflicts                        [#################################] 100%
error: failed to commit transaction (conflicting files)
ca-certificates-utils: /etc/ssl/certs/ca-certificates.crt exists in filesystem
```

Solution: https://www.archlinux.org/news/ca-certificates-utils-20170307-1-upgrade-requires-manual-intervention/

```
pacman -Syuw                           # download packages
rm /etc/ssl/certs/ca-certificates.crt  # remove conflicting file
pacman -Su                             # perform upgrade
```

Network issue
------------------

Eth0 disappears after upgrade. using ifconfig eth0 up shows "libphy: PHY 4a101000.mdio:01 not found".

One temporary solution: systemctrl restart dhcpcd (it will still show the problem, but then eth0 will appear.)


Downgrade a package
----------------------------

Objective: download the linux-headers-am33x-legacy-3.8.13-31-armv7h.pkg.tar.xz when the current repo holds only the latest packages

From 'pacman -Ss header | grep 3.8' , there does not exist this linux-headers-am33x-legacy header package wanted in my test.

The easiest way is to get a arch arm rollback machine and download the package. one candidate is http://rollback.adminempire.com/alarm-rollback-machine/ but it appears to be down.

Reference https://wiki.archlinux.org/index.php/Arch_Linux_Archive tells that there is this agetpkg program (that can be installed by pacman)
and it can be used to look for old package,
but somehow it cannot be found.

The mirror link suggested looks like for x86 and i686 only (Server=https://archive.archlinux.org/repos/2014/03/30/$repo/os/$arch)
(In fact, the ARM one mentioned stands for Archlinux rollback machine, not for arm7)

One more way is to use the downgrade script, downloadable from https://aur.archlinux.org/packages/downgrade/ . it seems to use http://repo-arm.archlinuxcn.org/ by default, but is arm doesn't mean arm7 but Arch Rollback Machine... damn!

Another way is to rebuild the package based on https://wiki.archlinux.org/index.php/Downgrading_packages.
But we need to find the right source to build.

One active rollback machine for arm can be found at http://tardis.tiny-vps.com/aarm/repos/ but it started from 2015 Dec only.

 
Change console font size
---------------------------
Reference: https://wiki.archlinux.org/index.php/Fonts  (section: Console fonts)

previewing: from terminal, setfont lat2-16 -m 8859-2 (It means that second part of ISO/IEC 8859 characters are used with size 16)  
(all the available fonts can be found at /usr/share/kbd/consolefonts/)   
(to make it smaller, we can change lat2-16 to lat2-14, lat2-10 etc)

To make the change permanent, we can add something to /etc/vconsole.conf (create this file if it is not there):

```
FONT=lat2-16 
```

Btw don't add the following line:  
FONT_MAP=8859-2 (because after adding it, the tab, ctrl etc wont work..)


Change console rotation
------------------------------

Echo 1 > /sys/class/graphics/fbcon/rotate for a rotation of 90% (or echo 2/3 for 180 and 270)


Wake up screen at console
-------------------------
Possible solution: echo 0 > /sys/class/graphics/fb0/blank  
reference: https://groups.google.com/forum/#!topic/beagleboard/MdOBsXNXzEI

Other ways: http://superuser.com/questions/152347/change-linux-console-screen-blanking-behavior  
Like: put "consoleblank=0" in uEnv.txt
