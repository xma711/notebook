Diary
________

after install gentoo following the guide in https://wiki.gentoo.org/wiki/Handbook:AMD64, i installed ubuntu by the installation disk. the ubuntu installation rewrote the /dev/sda1 the bootloader i think and then gentoo disappear. 


I use gentoo livecd and chroot to the installed gentoo, and restore its grub. but ubuntu is gone.


The solution is to add an entry for ubuntu in the /etc/grub.d/40_custom in gentoo and update the grub.cfg by 

"grub2-mkconfig -o /boot/grub/grub.cfg". 

The entry in 40_custom is something like:

menuentry "ubuntu" {
    set root='hd0,10'
    linux /vmlinuz root=/dev/sda10 ro quiet splash
    initrd /initrd.img
}
the ubuntu is install in /dev/sda10 partition. the thing i don't understand is why root='hd0,10' rather than root='sda,10'

references:
http://askubuntu.com/questions/344125/how-to-add-a-grub2-menu-entry-for-booting-installed-ubuntu-on-a-usb-drive

https://wiki.archlinux.org/index.php/GRUB

similar for archlinux:
menuentry "archlinux" {
    set root='hd0,6'
    linux /vmlinuz root=/dev/sda6 rw quiet splash
    initrd /initrd.img
}

note that i need to create the symbolic link of vmlinuz and initrd.img to the files in /boot in the sda6 partition.
Also note that in "linux /vmlinuz root=/dev/sda6 rw quiet splash" it is rw not ro. if using ro, archlinux will complain the root is read only.

Reference: https://wiki.archlinux.org/index.php/fstab

----------------------------------

To use ubuntu as the default os and dual boot other os:
go to ubuntu, mount all the partitions somewhere (e.g. sudo mount /dev/sda2 sda2; sudo mount /dev/sda5 sda5; sudo mount /dev/sda6 sda6), then run
sudo update-grub
os-prober
and then reinstall grub to /dev/sda:
sudo grub-install /dev/sda
and then reboot and it is done.

----------------------------------

Recap what i did to dual boot gentoo, arch, and ubuntu.

1. install gentoo live cd
2. use live cd to boot to the system and partitions using fdisk. make many partitions for future os.
3. install gentoo following the guide in https://wiki.gentoo.org/wiki/Handbook:AMD64 . in summary, install the file system to sda5, kernel image to sda2, swap to sd3 and then install grub2.
4. install ubuntu using ubuntu livecd. just choose install along side gentoo. the grub will be replaced by ubuntu and gentoo is disappear. (if i want to make gentoo as the first option in boot then i can use gentoo live cd to got gentoo and chroot to the install gentoo filesystem and then reinstall the grub and add an entry of ubuntu to the /etc/grub.d/40_custom; a better way is to use ubuntu as the default system and use update-grub and os-prober to add gentoo to ubuntu's grub.cfg)
5. whichever way, i can log in to gentoo again, and then install archlinux to sda6 following https://wiki.archlinux.org/index.php/Install_from_Existing_Linux. then i can add archlinux to either gentoo's grub or ubuntu's grub, depending on which will be used as default.


In summary, i have to install the kernel (/boot) and filesystem in a new partition and then i just add the new os to one of the grub in the default system. however, only one grub in one os will be used.

Reference:
http://ubuntuforums.org/showthread.php?t=1739833 
http://askubuntu.com/questions/506082/ubuntu-grub-menu-after-installing-centos





