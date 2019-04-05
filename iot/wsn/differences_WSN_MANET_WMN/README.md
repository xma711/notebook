Deconflict of concepts
------------------------------

The follows are found online, not from the module.

The concepts of WSN, MANET and wireless mesh networks can be confusing.  
To make things clear, the concepts are summarized as below:  

	- WSN: fixed wireless sensor network. must have sensors. 
		Boards can be both powerful (like BBB, raspberry pi) or not powerful (like Arduino). 
		They can be solar powered or mains-powered.
		The routing protocols needed are less required to handle mobility.  

	- MANET: mobile ad hoc network. topology is changing. routing is the main issue. 
		There can be a mobile ad hoc wireless sensor network, 
		and then it will be considered as a combination of MANET and WSN. 
		The routing protocols need to handle mobility, like AODV, DSR, DSDV etc. 

	- Wireless mesh network: simply an extension of internet; 
		Like WiFi APs without the cables (WMN Routers). it is relatively high-speed network, and is close to human daily usages. 
		There can be WMN clients (an end terminal itself that provides applications) that cannot provide network to others 
		But they can mesh among themselves as well as the WMN Routers. 
		The routing protocols need to handle mobility, e.g. 802.11s-draft, AODV..  
		There could be new MAC protocols to allows WMN routers to have higher bandwidth (CSMA based have some limits)

See below for more detailed comparisons.


Differences among WSN, MANET and wireless sensor networks
----------------------------------------------------------

Interestingly, the differences are not on the literal meaning of the names.  
Otherwise wireless mesh networks must be the superset of WSN and MANET because all them use mesh routing. 
And MANET must be a superset of WSN because MANET can deal with both mobile and fixed nodes.

The differences lie on the real-world applications of the networks and the names are not detailed enough.

To make things less confusing, wireless sensor network should be called: wireless mesh sensor (power-constrained) fixed network;  
MANET should be called: mobile ad hoc wireless mesh network;  
wireless mesh network: wireless mesh more-powerful not-power-constrained network; (can be mobile or not mobile or hybrid)


What is Wireless sensor network (WSN)
------------------------------------

Reference: http://www.scribd.com/doc/50634760/MANET-vs-WSN#scribd

A WSN consists of spatially distributed autonomous to monitor physical or environmental conditions, 
such as temperature, sound, vibration, pressure, motion or pollutants 
and to cooperatively pass their data through the network to a main location (gateway..).

Applications:  
	- indoor/outdoor environmental monitoring  
	- structural monitoring  
	- health and wellness monitoring (wireless body network)  
	- inventory location awareness (more like IOT)  
	- industrial automation

What is mobile ad-hoc network (MANET)
-------------------------

Reference: http://www.scribd.com/doc/50634760/MANET-vs-WSN#scribd

what is MANET:  
	- self-configuring network of mobile routers connected by wireless links (forms arbitrary topology & rapid unpredictable topological changes)  
	- each device in a MANET is free to move independently in any direction; each must forward traffic unrelated to its own use, and therefore each is a router itself.

Application of MANET:  
	- battlefield communication  
	- sensor networks!! (this means sensor network is a subset of MANET, although sensor networks are usually not mobile)  
	- personal area networks (PAN) using laptops, smartphones, smartwears etc  


Differences between WSN and "mobile ad-hoc network MANET
-------------------------------------------------------------------------------------------

Based on https://www.quora.com/What-is-the-difference-between-wireless-sensor-networks-and-ad-hoc ,
WSN's topology is more stable (nodes are fixed), so routes are fixed most of the time. 
Of course, nodes in WSN are to sense something.

On the other hand, ad-hoc usually means mobile or changing topology. 
The network must repeatedly reconfigure its routes. 
MANET doesn't have a fixed central controller and so they have to reconfigure their routes collectively.  
Examples of MANETS are networks formed by devices installed within cars (VANET) to monitor accidents, traffic and so on, 
or a network consisting of drones.

Based on my own experience, a network that made of commercial airplanes can be considered as a MANET too.

In some sense, MANET is a super set of WSN. 
MANET can handle both mobile and fixed nodes.
The nodes in MANET can have sensors or don't have sensors.
The nodes in MANET can have or not have energy constrain. 
Therefore, WSN can be considered as a subset of MANET (but the impression of MANET focuses on the changing-topology characteristics). 

Of course, there can be a mobile wireless sensor network, which is equivalent to MANET whose purpose is to collect sensor data on mobile nodes.


Based on http://www.scribd.com/doc/50634760/MANET-vs-WSN#scribd , 
the similarities between MANET and WSN are:  
	- both are distributed wireless networks that has no significant network infrastructure in place  
	- both need multihop routing (each node is a router)  
	- both are usually battery-powered and therefore there is a big concern on power consumption  
	- self-management is necessary

the differences are:
	- MANETs are usually close to humans, in the sense that most nodes are devices that are meant to be used by human beings (not sure if this claim is true..) 
		while sensor networks instead focuses on interaction with the environment (this point is about the application domain)  
	- density of deployment in WSN can be orders of magnitude higher than that in MANET  
	- data rate is usually higher in MANET (if MANET is considered the network of PDAs, laptops, smartphones etc)  
	- WSN nodes are usually cheaper and simpler  
	- WSN has tighter requirements on network lifetime and energy, as WSN nodes' batteries are difficult to be replaced  
	- WSN usually has redundant nodes to serve an area

	
What is wireless mesh network
--------------------------------------------------

Reference: http://computer.howstuffworks.com/how-wireless-mesh-networks-work.htm

it is more like an extension of the wired Ethernet.  
Ethernet nodes are wiredly connected to the router and the nodes are not meshly connected (the typical topology is star, with router in the center).

Wireless mesh network is like Ethernet, but nodes are communicating wirelessly, and able communicate with each other (mesh routing).

Therefore, wireless mesh network is very close to humans.
It is more about spreading the internet via many wireless nodes to a bigger area. 
The nodes are in the "powerful" category.

In a wireless mesh network, only one node needs to be physically wired to a network connection. 
The one wired node then shares its internet connection wirelessly with all other nodes in its vicinity. 
The more nodes, the further the connection spreads, creating a wireless "cloud of connectivity" that can serve a small office or a city of millions.

The application domain of wireless mesh network is really different from WSN or MANET. 
