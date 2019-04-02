Installation
--------------

Follow https://wiki.gentoo.org/wiki/Handbook:AMD64 to install Gentoo for Linux 64.

It is actually very similar to create a SD card for single-board computers like BBB and raspberry pi.

WiFi
--------
need to configure the kernel as :
enable the following option in the kernel config:

Device Drivers ---> Generic Driver Options ---> Fallback user-helper invocation for firmware loading (CONFIG_FW_LOADER_USER_HELPER_FALLBACK=y) 

reference: http://forums.gentoo.org/viewtopic-t-1001638.html

of course need to configure other kernel parameters and install the linux-firmware.

Reference: http://wiki.gentoo.org/wiki/Wifi

After the WiFi is detected, then follow the guide in ../wifi/README.md to set up the WiFi connection using wpa_supplicant
