adb
------------------------

android debugger.

in my computer the binary is located at /home/xma/Android/Sdk/platform-tools

to make a phone recognizable by adb, the developer option in the phone has to be enabled (tap build number 7 times). 
then in the developer option, the "usb debug" has be enabled.  
lastly, the phone has to be restarted.

A cheatsheet of adb can be found here: https://github.com/maldroid/adb_cheatsheet/blob/master/cheatsheet.pdf

a particularly useful command is "adb shell", which logs into the device.  
and then suddenly it becomes a familiar linux machine!

another command is "adb logcat", which can see the logs from the whole system of the android device.  

btw to add a log inside android app, use "Log.d("xxx", "xxx");" inside codes.


emulator
-----------------------

Tools -> Android -> AVD manager -> (add or start a new emulator)

if the system complains that there is no /dev/kvm, then need to enable the vt-d (virtualization technology) in bios.  
just google and follow the steps. 
one reference can be found here: https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/5/html/Virtualization/sect-Virtualization-Troubleshooting-Enabling_Intel_VT_and_AMD_V_virtualization_hardware_extensions_in_BIOS.html

after start an emulator, then adb can see it: adb devices.  
in fact, from this part onward, it seems like a real device.
