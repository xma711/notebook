Steps
---------------

Using Nexus S as an example.

Reference: http://wiki.cyanogenmod.org/w/Install_CM_for_crespo

1. unlock bootloader:   
	- adb reboot bootloader  
	- fastboot oem unlock  
	- accept device's agreement

2. install custom recovery:  
	- adb reboot bootloader  
	- fastboot flash recovery recovery_image.img

3. install the os:  
	- adb push os.zip /sdcard/  
	- (in recovery os), "wipe" and then "install"

anyway just follow the guide in the link.
