waspmote factory default program
------------------------------------

after i uploaded this program to waspmote, it will output "H#" when xbee pro s1 or s2 are plugged in.  
	- don't know what this means..  
	- it seems the setup function is repeatedly called.  
it turns out that it is because the usb power cannot provide enough current for bbb+xbee.  
has to plug in the battery to make it work.

when LoRa is plugged in, no communication module is detected.

when i used LoRaWAN, it can detect the module and tries to send a frame.


smart cities board
-------------------------

after plugging in the temperature/humidity/pressure sensor, and run the SCP_V30_05_Temperature_humidity_and_pressure_sensor file,
it works fine.

the only thing is that temperature seems to drop slowly.
a process of stablizing?


LoRaWAN p2p
------------------

test with 1 sender and 1 receiver. works fine.  
the codes used are "LoRaWAN_P2P_02_send/receive_packets"


Xbee + gateway
--------------------

i have saved the default xbee config in dropbox.  
it uses 9600 baud rate instead of 115200.

the gateway dongle also uses 9600 baud rate.  
connect the gateway dongle to computer, just do a "screen /dev/ttyUSBx" will do.
the msgs received will be printed on the screen.
