Libelium Waspmote
-----------------------

Ref: http://www.libelium.com/products/waspmote/wsn/  
check this ref for the overall wsn structure.  
It includes a cloud backend also, and it can be seen as IoT too.

Waspmote --- meshlium gateway (local storage available) ---> cloud


Meshlium: gateway
-----------------------

Ref: http://www.libelium.com/products/meshlium/

mostly thru some GUI (Manager System web interface).

But also can also ssh into meshlium (https://www.libelium.com/forum/viewtopic.php?f=4&t=19134&sid=6c8d7fb2cf814c19a1dec8cd186123c6).

It runs a linux OS (Debian).

According to the "quickstart_guide_meshlium.pdf", it is not recommended to run command in shell 
coz failures derived from a wrong usage of the shell will not be covered under warranty.

This could be the biggest obstacle for us if we want add other programs into the gateway. 
But it should be possible and should not be too hard.

To use ssh, the user name is root, passwd is libelium. 

The GUI thing is nothing but a program. our programs should be able to coexit with it.

One way i m thinking is that we use the normal way to send data to the cloud, 
and also we run some stuff in the node to do some edge computing if needed!

A guide to add our own application: https://www.libelium.com/v11-files/Tutorials_mesh_extreme/tutorial002.php

btw singapore's LTE band is mostly in 3 and 7, so we should have the EU/BR version for LTE for meshlium.

For xbee-pro, we should have the 2.4 GHz. there are 2 versions, one has 18dBm (1.6km) and the other 10 dBm (750m in EU model)

singapore's power voltage is 230V. the adaptor for meshlium is 220V. should be fine to use.


