Plug and play.

Cat cat /sys/devices/bone_capemgr.*/slots

 3: 57:P---L 4D 4.3 LCD CAPE- 4DCAPE-43      ,00A1,4D SYSTEMS      ,BB-BONE-LCD4-01

the interface that links to the screen is /dev/tty1.

Echo "hello world" > /dev/tty1  will make the message appear on the screen.

Reference for bbb overlays: https://learn.adafruit.com/introduction-to-the-beaglebone-black-device-tree/exporting-and-unexporting-an-overlay

reference for the module: http://www.4dsystems.com.au/product/4DCAPE_43/

another model has the same capability: BB-BONE-LCD4-01-ND (but it seems it does not enable the BB-BONE-LCD4-01 overlay device tree).
