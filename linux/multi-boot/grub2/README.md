Attempt
---------------------

After install Gentoo following the guide in https://wiki.gentoo.org/wiki/Handbook:AMD64,
Ubuntu is installed by the installation disk.
The Ubuntu installation rewrote the /dev/sda1 the bootloader and then Gentoo disappear. 

Gentoo livecd is used to chroot to the installed Gentoo, and restore its grub.
But Ubuntu is gone.

The solution is to add an entry for Ubuntu in the /etc/grub.d/40_custom in Gentoo and update the grub.cfg by  
"grub2-mkconfig -o /boot/grub/grub.cfg". 

The entry in 40_custom is something like:

```
menuentry "ubuntu" {
    set root='hd0,10'
    linux /vmlinuz root=/dev/sda10 ro quiet splash
    initrd /initrd.img
}
```

The ubuntu is install in /dev/sda10 partition.
(One observation is that in menuentry, root='hd0,10' rather than root='sda,10'.
Not sure about the reason.)

References:
http://askubuntu.com/questions/344125/how-to-add-a-grub2-menu-entry-for-booting-installed-ubuntu-on-a-usb-drive  
https://wiki.archlinux.org/index.php/GRUB

Similarly for archlinux:

```
menuentry "archlinux" {
    set root='hd0,6'
    linux /vmlinuz root=/dev/sda6 rw quiet splash
    initrd /initrd.img
}
```

Note that we need to create the symbolic link of vmlinuz and initrd.img to the files in /boot in the sda6 partition.
Also note that in "linux /vmlinuz root=/dev/sda6 rw quiet splash" it is rw not ro.
If using ro, archlinux will complain the root is read only.

Reference: https://wiki.archlinux.org/index.php/fstab


To use ubuntu as the default OS and dual boot other OS
----------------------------------------------------------

Go to ubuntu, mount all the partitions somewhere (e.g. sudo mount /dev/sda2 sda2; sudo mount /dev/sda5 sda5; sudo mount /dev/sda6 sda6), then run

```
sudo update-grub
os-prober
and then reinstall grub to /dev/sda:
sudo grub-install /dev/sda
and then reboot and it is done.
```

Recap what were done to dual boot Gentoo, arch, and ubuntu.
--------------------------------------------------------------

1. Install Gentoo live cd

2. Use live cd to boot to the system and partitions using fdisk. make many partitions for future os.

3. Install Gentoo following the guide in https://wiki.gentoo.org/wiki/Handbook:AMD64 .
In summary, install the file system to sda5, kernel image to sda2, swap to sd3 and then install grub2.

4. Install ubuntu using ubuntu livecd. just choose install along side Gentoo.
The grub will be replaced by ubuntu and Gentoo is disappear.
(If we want to make Gentoo as the first option in boot then we can use Gentoo live cd to got Gentoo and chroot to the install Gentoo filesystem and then reinstall the grub
and add an entry of ubuntu to the /etc/grub.d/40_custom;
a better way is to use ubuntu as the default system and use update-grub and os-prober to add Gentoo to Ubuntu's grub.cfg)

5. Whichever way, we can log in to Gentoo again, and then install archlinux to sda6 following https://wiki.archlinux.org/index.php/Install_from_Existing_Linux.
Then we can add archlinux to either Gentoo's grub or Ubuntu's grub, depending on which will be used as default.


In summary, we have to install the kernel (/boot) and filesystem in a new partition
and then we just add the new os to one of the grub in the default system.
However, only one grub in one os will be used.

Reference:  
http://ubuntuforums.org/showthread.php?t=1739833  
http://askubuntu.com/questions/506082/ubuntu-grub-menu-after-installing-centos
