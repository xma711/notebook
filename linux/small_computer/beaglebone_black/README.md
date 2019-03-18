Some important things to consider
-------------------------------------

1. how to upgrade the kernel to 4.1, coz it also supports device tree.

2. need to read the bbb manual to understand it better.


Device tree
-----------------
Reference: https://learn.adafruit.com/introduction-to-the-beaglebone-black-device-tree/exporting-and-unexporting-an-overlay
reference: http://www.raspberry-pi-geek.com/Archive/2014/03/Capemgr-keeps-track-of-the-BeagleBone-Black-s-expansion-boards-known-as-capes

from kernel 3.8, bbb use device tree to setup its pins maps, if my understand is correct.. 
There is also this device tree overlay. it is like adding things to the existing device tree.
For example, those interface like ttyO2 I2C-1 enabled in uEnv.txt are overlays.

For kernel beyond 3.8, it seems that the device tree is not there.. (Device tree is back in kernel 4.1)

Capemgr exposes its userspace interface through the /sys/devices/bone_capemgr.* directory via the sysfs filesystem. 
The slots file within this directory is used to interact with Capemgr. 
When Capemgr loads an overlay, it allocates the overlay to a "slot" within Capemgr. 
To determine which Capemgr slots currently contain an overlay, cat out the slots file.

```
Ok, let's next navigate to where we can view which overlays are enabled by the bone cape manager:
    root@beaglebone:/lib/firmware# cd /sys/devices/bone_capemgr.*

Next up, cat the contents of the slots file:
    root@beaglebone:/sys/devices/bone_capemgr.8# cat slots

It should look something like this, assuming you haven't customized your Angstrom installation very much:
    0: 54:PF--- 
    1: 55:PF--- 
    2: 56:PF--- 
    3: 57:PF--- 
    4: ff:P-O-L Bone-LT-eMMC-2G,00A0,Texas Instrument,BB-BONE-EMMC-2G
    5: ff:P-O-L Bone-Black-HDMI,00A0,Texas Instrument,BB-BONELT-HDMI

According to the BeagleBone documentation, "the first 3 slots are assigned by EEPROM IDs on the capes". The next two are overlays loaded at boot. Number 4 is the EMMC memory built in that you're mostly likely booting your Angstrom distribution from. The 5th overlay is for enabling the HDMI component.

If you were to now export another overlay, such as our favorite UART1 overlay, you would see a new option listed as number 6. Let's try that by exporting the UART1 dtbo file:
    root@beaglebone:/sys/devices/bone_capemgr.8# echo BB-UART1 > slots

We're taking the output of echo, "BB-UART1", and writing it to the slots file to enable the drivers and device for UART1 using the overlay. Now, let's check that the overlay loaded properly:
    root@beaglebone:/sys/devices/bone_capemgr.8# cat slots

We should now have the UART1 device loaded up, and ready to go:
    0: 54:PF--- 
    1: 55:PF--- 
    2: 56:PF--- 
    3: 57:PF--- 
    4: ff:P-O-L Bone-LT-eMMC-2G,00A0,Texas Instrument,BB-BONE-EMMC-2G
    5: ff:P-O-L Bone-Black-HDMI,00A0,Texas Instrument,BB-BONELT-HDMI
    6: ff:P-O-L Override Board Name,00A0,Override Manuf,BB-UART1

Now, let's say you're done with using the UART1 device, and need those pins for something else. One way to remove the overlay would be to restart your BeagleBone. The other way would be to unexport it.
You can export it by executing the following command:
    root@beaglebone:/sys/devices/bone_capemgr.8# echo -6 > slots
```

The first four slots (0-3) are reserved for overlays associated with capes that have been physically plugged in to the BBB. 
The I2C bus address is a hexadecimal byte used by capes to request that the cape be placed in a particular slot.

The slot status field has five characters that describe the current state of a particular slot on the Capebus. 
Each character position in the slot status field represents a state that the slot is in and is either a letter (state is active) or a dash (state is not active). 
The five states are, from left to right in the slot status field, 
	- "P" (slot has been probed for a cape), 
	- "F" (probing failed for this slot), 
	- "O" (an override has placed the cape in this slot), 
	- "l" (cape is still being loaded), 
	- and "L" (cape loading has completed).

The available binary overlay files can be found in /lib/firmware. 
Name of overlay device tree: [PART_NUM]-[VER].dtbo, where [PART_NUM] is the part number and [VER] is the hardware version associated with the overlay.

To load an overlay manually from userspace, the overlay must be a compiled .dtbo file that is located in the firmware directory of the root filesystem. 
The part number associated with the overlay (not the full file name of the .dtbo file) is echo'd into the slots file to load the overlay. 
For example, to load the overlay file MY_OVERLAY-00A0.dtbo, which is located in the firmware directory, use the following command:  
user@beaglebone:~# sudo echo MY_OVERLAY > /sys/devices/bone_capemgr.*/slots

btw, to export the device with a specific version number, use sth like: "BB-BONE-LCD4-01:00A1".


Capes
-------------------------
Reference: http://www.raspberry-pi-geek.com/Archive/2014/03/Capemgr-keeps-track-of-the-BeagleBone-Black-s-expansion-boards-known-as-capes (very useful)

A true cape uses the I2C2 bus (pins P9.19 and P9.20) to identify itself to the Capebus at boot time.

If the identification is recognized, the kernel will load the appropriate overlay automatically 
to mux the pins appropriately and set up the necessary kernel device drivers.

To handle any dynamic changes that must be made to the static device tree, the Capemgr (Cape Manager) kernel mechanism is used. 
Capemgr supports the loading of device tree data from userspace.

When booting a BBB system without any capes attached, 
many of the pins available via the P8 and P9 connectors are already allocated for specific purposes, 
because some pins are physically wired to specific lines on the board, 
and some are muxed by the device tree.
	- power related: p9-1 to p9-10, p9-43 to p9-46, p8-1 and p8-2.
	- i2c-2: p9-19,20
	- hdmi video: p8-27 to p8-46
	- emmc: p8-(3 to 6, 20 to 25)
	- hdmi audio: p9-(25, 28, 29, 31)

check what pins are used by capes
----------------------------------

Reference: http://www.valvers.com/embedded-linux/beaglebone-black/step04-gpio/
another useful reference talking about gpios and the device tree: http://kilobaser.com/blog/2014-07-15-beaglebone-black-gpios

to see the what pins are used by capes/device trees, use   
cat /sys/kernel/debug/pinctrl/44e10800.pinmux/pingroups  
(reference: cat /sys/kernel/debug/pinctrl/44e10800.pinmux/pingroups)  
however, the pins are not directly mapped to the p8 and p9 pins.  
To find out the exact pins, use the documents from https://github.com/derekmolloy/boneDeviceTree/tree/master/docs to map the pin number to the exact p9 or p8 pins in bbb.


This path has useful stuff relating to pins: /sys/kernel/debug/pinctrl/44e10800.pinmux

another reference: http://elinux.org/EBC_Exercise_11a_Device_Trees

however, apparently, not all pins will be shown here. for example, after exporting the analog pins device tree overlay, the pins are not shown here.

Also, when using LCD, exporting the analog pins device tree doesn't complain, but the pins cannot be used. there could be some confliction between the hidden LCD pins and analog pins.

HDMI
------------------------
Reference: http://www.raspberry-pi-geek.com/Archive/2014/03/Capemgr-keeps-track-of-the-BeagleBone-Black-s-expansion-boards-known-as-capes/%28offset%29/2

btw, The device tree specifies two nodes for the HDMI cape: 
	- one node for a "full HDMI cape" that provides both audio and video data (BB-BONELT-HDMI) 
	- and one node for a "video-only HDMI cape" that provides only video data (BB-BONELT-HDMIN).

The full HDMI cape overlay is given a higher priority by the device tree, so Capemgr will attempt to load it first before loading the video-only HDMI overlay. 
If Capemgr successfully loads the full HDMI overlay, then its attempt to load the video-only HDMI overlay will fail.


ADC on beaglebone black
-----------------------------------

Reference: http://www.linux.com/learn/tutorials/787511-how-to-get-analog-input-on-the-beaglebone-black  
reference: http://beaglebone.cameon.net/home/reading-the-analog-inputs-adc

There are 6 ADCs on beaglebone black: AIN0 to AIN6. VDD_ADC is 1.8v, the reference voltage. 
Thus the maximum voltage that can be sampled is 1.8V.
The chip is 12bit, so that get numbers in the range 0-4095.

Enable:  
	echo cape-bone-iio > /sys/devices/bone_capemgr.*/slots

check:  
	cat /sys/devices/bone_capemgr.*/slots

find the pins:  
	find /sys -iname "ain*"

most likely it is at "/sys/devices/ocp.3/helper/AINx"

to get the reading from AIN0 e.g.: cat /sys/devices/ocp.3/helper/AIN0

the disadvantage is that 9 pins will be used at one go.

To use the dafruit-BBIO package for python to get readings, pip install Adafruit_BBIO.
Reference: https://learn.adafruit.com/setting-up-io-python-library-on-beaglebone-black/adc  
use this lib directly, i can get 833Hz on one channel only. 
There should be some ways to speed up the sampling frequency, because the internal ADC is at least 1MHz.

When the LCD screen is used, activating the device tree is okay. but once i try to run AC.setup(), there is this error:
```
RuntimeError: Unable to setup ADC system. Possible causes are: 
  - A cape with a conflicting pin mapping is loaded 
  - A device tree object is loaded that uses the same name for a fragment: helper
```

control bbb built-in leds
-----------------

Http://robotic-controls.com/book/export/html/69

in summary, go to /sys/class/leds/beaglebone\:green\:usrX/  [X=0/1/2/3]

and cat none/heartbeat/timer > trigger


enable /dev/ttyACM0 using microUSB
------------------------------------

Reference: https://kwantam.github.io/BBKNotes1.html (enable g_serial for ttyACM0)
http://hipstercircuits.com/serial-over-usb-on-beaglebone/ (need getty to make the console work)
http://unix.stackexchange.com/questions/71064/automate-modprobe-command-at-boot-time-on-fedora (load kernel module automatically)
https://github.com/crondog/arch-flo (enable serial-getty\@ttyGS0.service)

connect a microUSB cable from a computer to bbb.

1. add a file "g_serial.conf" to /etc/modules-load.d/  (the content of the file is "g_serial") (which will make the systemd-modules-load.service load the kernel module)
2. systemctl enable serial-getty\@ttyGS0.service
3. add ttyGS0 to /etc/securetty (important. cannot have any space after "ttyGS0")

### (obsolete) need to do a "modprobe g_serial" to enable the module. (make sure g_mass_storage module is not loaded)
### (no need this one)then, "agetty -L ttyGS0 115200 linux" to tell init to start serial login on ttyGS0 in runlevel 2 and 3


GPIOs
-----------------

Http://kilobaser.com/blog/2014-07-15-beaglebone-black-gpios

there are 65 possible digital I/Os, mostly on the p8 side.

Control the pin at /sys/class/gpio/ folder.

Enable a gpio (e.g. gpio60): echo 60 > /sys/class/gpio/export  (where 60 is the gpio number, not pin number)

set direction as output: echo out > /sys/class/gpio/gpio60/direction

set value as 1/0: echo 1/0 > /sys/class/gpio/gpio60/value

direction	Decides whether this is an input or output pin. Writing in or out to this file, changes the behaviour of the value-file accordingly.

Value	if direction is in, reading this file tells you if the external signal connected to the pin is 1 (3.3V) or 0 (0V)
if direction is out, writing to this file sets the voltage we output on the pin to either 3.3V (1) or 0V (0)

active_low	If 1, the meaning of 1 and 0 in the value-file is reversed: 0 (3.3V) and 1 (0.V)

to get the correct gpio number (which is not pin number), just use a table to map the pin number to gpio number. e.g. p9 pin 12 corresponds gpio_60.  
(to make things more confusing, p9 pin 12 is also GPIO1[28], but the GPIO controller will treat it as 28+32=60.)  
One table can be found here: http://beagleboard.org/support/bone101

Recompile u-boot and kernel
---------------------------------

Reference: https://jkridner.wordpress.com/2014/06/04/yet-another-set-of-notes-on-building-beaglebone-kernel/

extract from the reference: 

sudo apt-get install gcc-arm-linux-gnueabihf lzop pastebinit ncurses-dev

git clone git://git.denx.de/u-boot.git

cd u-boot

make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- am335x_evm_config

cp tools/mkimage ~/bin

cd

git clone git://github.com/beagleboard/kernel

cd kernel

git checkout 3.8

./patch.sh

cd kernel

cp ../configs/beaglebone .config

make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- menuconfig

make -j8 ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- uImage dtbs modules

pastebinit .config

(don't know why, cannot get the image in this way)



another way of compiling uboot and kernal
------------------------------------------
Reference: https://eewiki.net/display/linuxonarm/BeagleBone+Black

follow "Bootloader: U-Boot" section to "Linux Kernel" section to build u-boot.img and the zImage kernel and device tree (dtb).

I copy the zImage and device tree to the /dev/mmcblk0p2 root/boot folder in the bbb emmc. make symbolic links to all files so that appear on /boot folder first layer. (symbolic links needed for zImage, arm*.dtb files)

and copy u-boot.img and MLO to /dev/mmcblk0p1. 

The uEnv.txt looks like:
"
mmcroot=/dev/mmcblk0p2 rw
 
optargs=coherent_pool=1M capemgr.enable_partno=BB-UART1,BB-I2C1
"

the first line is necessary to make the filesystem read and write. or it will be read only.

After reboot and it works.

One problem is that the xbee dongle is not detected and appear in the /dev/ttyUSB* list.

The problem is solved by copy the firmware and modules folders to the respective positioins /usr/lib/firmware and /usr/lib/modules



power
-------------------

With this model of cpu:  
Model name:            ARMv7 Processor rev 2 (v7l)  
CPU max MHz:           1000.0000  
CPU min MHz:           300.0000  

and running with archlinux, the power consumption is about 200mA x 5V = 1W from the experiment i did.

To reduce power consumption, the cpu frequency can be lowered from the default 1000MHz to 300MHz.   
For 300MHz, the power consumption is about 135mA x 5V = 0.657W which is 32.5% reduction in power consumption.

A script can be written to achieve this (the whole point is to echo powersave to scaling_governor in the cpufreq path):

```
#!/bin/sh

SYS_CPUFREQ_ROOT=/sys/devices/system/cpu/cpu0/cpufreq/

if ! grep -q powersave ${SYS_CPUFREQ_ROOT}/scaling_available_governors; then
	echo powersave option not available! quitting...
	exit 0
fi

echo powersave > ${SYS_CPUFREQ_ROOT}/scaling_governor
```

a useful tool is called cpufrequtils, which can used for checking cpu info and set cpu parameters.  
See reference: http://zeldor.biz/2012/11/beaglebone-optimize-power-consumption/


some points from reading BBB SRM Rev C.1
------------------------------------------
1. power button can be used to put BBB to sleep and then to wake it up (i tested with Archlinux. bbb failed to wake up with some stack problem)

2. If powered from the USB port, it is limited to 500mA max and VDD_5V rail (P9 5 and 6) is not provided to the expansion headers, 
so capes that require the 5V rail to supply the cape directly will not have that rail available for use. 
However, 5v is still available in SYS_5V (p9 7 and 9), which comes from the TPS62517C PWIC. 












