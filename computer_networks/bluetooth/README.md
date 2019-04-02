Bluetooth protocol stack
------------------------------------

Reference: https://stackoverflow.com/questions/1046669/bluetooth-protocol

the Bluetooth protocol stack includes its own transport protocols: L2CAP and RFCOMM,
where RFCOMM links use the L2CAP layer.

It is possible to use IP tunneling over Bluetooth encapsulating UDP packets over RFCOMM links.


Bluez
------------------

Bluez is the Bluetooth stack for Linux kernel OS. 

For archlinux:  
pacman -S bluez  
pacman -S bluez-utils

use bluez thru hciconfig and hcitool
---------------------------

Check Bluetooth hci id:
	- hciconfig (should see hci0)

turn associated Bluetooth up/down:
	- sudo hciconfig hci0 up/down

hcitool comes from the bluez-utils package.

Discover nearby Bluetooth devices:
	- hcitool scan
which give results something like
```
Scanning ...
	C4:62:EA:A9:26:E6	Galaxy Note3
```

The software always uses the MAC address to reference a given device.

(l2ping sends a L2CAP echo request to the Bluetooth MAC address bd_addr given in dotted hex notation.)

Ping a device:
	- l2ping C4:62:EA:A9:26:E6 (it works. sometimes failed though)

reference: http://www.stlinux.com/kernel/bluetooth/how-to-run-BlueZ


use Bluetooth via python
---------------------------
Install header files:
sudo apt-get install libbluetooth-dev

install package:
sudo pip install pybluez


reference: http://stackoverflow.com/questions/7485750/sending-messages-or-datas-with-bluetooth-via-python


issues and solutions
---------------

If phone cannot transfer files to Ubuntu, need to enable it at "personal file sharing" interface.

Reference: http://askubuntu.com/questions/131570/how-do-you-make-ubuntu-accept-files-sent-over-bluetooth






