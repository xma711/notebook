About this folder
---------------------

Mainly about wireless sensor networks, but may or may not be battery-powered.

However, this folder will also have some stuff relating to mobile ad hoc network (MANET),
which is slightly different from WSN.

A sensor node in WSN is usually thought to be very resource-limited, 
however, in my experience, the nodes are not necessarily such nodes.  
Rather, they may be quite powerful, like beaglebone black.

Regarding a network with powerful nodes that collect sensor data without power constrain, is it still called a wireless sensor network?  
Maybe it should be called a "wireless mesh network"..

What about powerful nodes that collect sensor data but run on solar power?  
Maybe it can still be considered as a wireless sensor network, just that the nodes are not so mainstream.

None of them should be considered as a MANET, because none of them need mobility. 


Some references
---------------------

National Instruments: what is a wireless sensor network? http://www.ni.com/white-paper/7142/en/  
components of a WSN node: radio, battery, microcontroller, analog circuit and sensor interface. 


Difference between WSN and IoT
----------------------------------

Ref: https://www.quora.com/What-is-the-difference-between-WSN-and-IOT

WSN: things (sensor nodes) connected without a wire to gather data.  
IoT: WSN + Internet + App + Cloud computing + etc ... (maybe also intelligence)

WSN is like the eyes and ears of the Internet of Things. 
It is a bridge connecting the real world to the digital world.  
IoT is like a brain. 
It can both store the real world data and also be used to monitor the real world parameters,
make meaningful interpretation and even make decisions based on the sensed data..


From WSN to IoT
----------------------------

Ref: paper "Evolution of Wireless Sensor Networks towards the Internet of Things: a Survey" by L. Mainetti, 2011.

WSNs --> high heterogeneity --> different proprietary and non-proprietary solutions, 
delaying a large-scale deployment of WSN technologies to obtain a virtual wide sensor network able to integrate all existing sensor networks.

"the current trend is to use the internet protocol to achieve native connectivity between WSNs and the internet".
(Personally i think this eases many problems.)

"following trend of web mashups", end users can create applications mixing 
real-world devices such as home appliances with virtual services on the web.

Non-ip solutions: Zigbee, Z-Wave, Insteon, Waveenis (the latter 2 may already die..)..  

Zigbee: phy layer + mac layer + network layer + application layer. phy and mac are defined by 802.15.4, rest by zigbee specification.   
Support tree and mesh topology;
development of applications relies on application profiles, such as the zigbee home automation public application profile and the smart energy profile.  
A new zigbee specification RF4CE offers a simplified version for star topology only.

Z-wave: 5 layers: phy + mac + transfer + routing + application.  
Allow reliable transmission of short msgs from a control unit to nodes in the network.  
Settings: automation in residential and light commercial environments.  
2 types of devices: controller and slave.

Ip-based solutions: 6LoWPAN defines the format for adaptation between IPv6 and IEEE 802.15.4.  
6lowpan --> scale across large network infrastructure with mobility.  
6lowpan architecture is made up of low-power wireless area networks, 
which are connected to other ip networks thru edge routers.  
Edge routers play an important role of handling 6lowpan compression and neighbor discovery and 
also the transparent mapping of the full IPv6 and the lowpan IPv6 format.

Another high level protocol is CoAP, a bit like the light weight http.  
(however, i think it is too high level and has nothing to do with making the WSNs more connected..)

