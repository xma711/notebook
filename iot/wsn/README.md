about this folder
---------------------

mainly about wireless sensor networks, but may or may not be battery-powered.

however, this folder will also have some stuff relating to mobile ad hoc network (MANET),
which is slightly different from WSN.

a sensor node in wsn is usually thought to be very resource-limited, 
however, in my experience, the nodes are not necessarily such nodes.  
rather, they may be quite powerful, like beaglebone black.

regarding a network with powerful nodes that collect sensor data without power constrain, is it still called a wireless sensor network?  
maybe it should be called a "wireless mesh network"..

what about powerful nodes that collect sensor data but run on solar power?  
maybe it can still be considered as a wireless sensor network, just that the nodes are not so mainstream.

none of them should be considered as a MANET, because none of them need mobility. 


some references
---------------------

National Instruments: what is a wireless sensor network? http://www.ni.com/white-paper/7142/en/  
components of a WSN node: radio, battery, microcontroller, analog circuit and sensor interface. 


difference between WSN and IoT
----------------------------------

ref: https://www.quora.com/What-is-the-difference-between-WSN-and-IOT

WSN: things (sensor nodes) connected without a wire to gather data.  
IoT: WSN + Internet + App + Cloud computing + etc ... (maybe also intelligence)

WSN is like the eyes and ears of the Internet of Things. 
it is a bridge connecting the real world to the digital world.  
IoT is like a brain. 
it can both store the real workd data and also be used to monitor the real world parameters,
make meaningful interpretation and even make decisions based on the sensed data..


from WSN to IoT
----------------------------

ref: paper "Evolution of Wireless Sensor Networks towards the Internet of Things: a Survey" by L. Mainetti, 2011.

WSNs --> high heterogeneity --> different proprietary and non-proprietary solutions, 
delaying a large-scale deployment of wsn technologies to obtain a virtual wide sensor network able to integrate all existing sensor networks.

"the current trend is to use the internet protocol to achieve native connectivity between WSNs and the internet".
(not sure if this is true; but personally i think this ease many problems.)

"following trend of web mashups (??)", end users can create applications mixing 
real-world devices such as home appliances with virtual services on the web.

non-ip solutions: Zigbee, Z-Wave, Insteon, Waveenis (the latter 2 may already die..)..  

Zigbee: phy layer + mac layer + network layer + application layer. phy and mac are defined by 802.15.4, rest by zigbee specification.   
support tree and mesh topologies;
development of applications relies on application profiles, such as the zigbee home automation public application profile and the smart energy profile.  
A new zigbee specification RF4CE offers a simplified version for star topology only.

z-wave: 5 layers: phy + mac + transfer + routing + application.  
allow reliable transmission of short msgs from a control unit to nodes in the network.  
settings: automation in residential and light commercial environments.  
2 types of devices: controller and slave.

ip-based solutions: 6LoWPAN defines the format for adaptation between IPv6 and IEEE 802.15.4.  
6lowpan --> scale across large network infrastructure with mobility.  
6lowpan architecture is made up of low-power wireless area networks, 
which are connected to other ip networks thru edge routers.  
edge routers play an important role of handling 6lowpan compression and neighbordiscovery and 
also the transparent mapping of the full ipv6 and the lopan ipv6 format.

another high level protocol is CoAP, a bit like the light weight http.  
(however, i think it is too high level and has nothing to do with making the wsns more connected..)

