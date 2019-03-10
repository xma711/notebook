installation
--------------

follow https://wiki.gentoo.org/wiki/Handbook:AMD64 to install gentoo for linux 64.

it is actually very similar to create a sd card for single-board computers like bbb and raspberry pi.

wifi
--------
need to configure the kernel as :
enable the following option in the kernel config:

Device Drivers ---> Generic Driver Options ---> Fallback user-helper invocation for firmware loading (CONFIG_FW_LOADER_USER_HELPER_FALLBACK=y) 

reference: http://forums.gentoo.org/viewtopic-t-1001638.html

of course need to configure other kernel parameters and install the linux-firmware.

reference: http://wiki.gentoo.org/wiki/Wifi

After the wifi is detected, then follow the guide in ../wifi/README.md to set up the wifi connection using wpa_supplicant
