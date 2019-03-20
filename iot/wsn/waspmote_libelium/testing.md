Waspmote factory default program
------------------------------------

After i uploaded this program to waspmote, it will output "H#" when xbee pro s1 or s2 are plugged in.  
	- it seems the setup function is repeatedly called.  
It turns out that it is because the usb power cannot provide enough current for bbb+xbee.  
Have to plug in the battery to make it work.

When LoRa is plugged in, no communication module is detected.

When i used LoRaWAN, it can detect the module and tries to send a frame.


Smart cities board
-------------------------

After plugging in the temperature/humidity/pressure sensor, and run the SCP_V30_05_Temperature_humidity_and_pressure_sensor file,
it works fine.

The only thing is that temperature seems to drop slowly.
A process of stablizing?


LoRaWAN p2p
------------------

Test with 1 sender and 1 receiver. works fine.  
The codes used are "LoRaWAN_P2P_02_send/receive_packets"


Xbee + gateway
--------------------

It uses 9600 baud rate instead of 115200.

The gateway dongle also uses 9600 baud rate.  
Connect the gateway dongle to computer, just do a "screen /dev/ttyUSBx" will do.
The msgs received will be printed on the screen.
