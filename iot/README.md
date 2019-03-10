What is IoT
-------------------------

Based on "Evolution of wireless sensor networks towards the internet of things: a survey" by L. Maninetti, 2011, 
IoT can be defined as a worldwide network of uniquely addressable interconnected objects,
based on standard communication protocols.
(this definition seems to focus more on the reachability of objects.)

based on https://www.quora.com/What-is-the-difference-between-WSN-and-IOT,  
WSN = things (sensor nodes) connected without a wire to gather data.  
IoT = WSN + Internet + App + Cloud computing + etc ...

based on wikipedia, global standards initiative on iot (IoT-GSI) defines the IoT as "the infrastructure of the information society".  

the wikipedia article itself defines IoT as the internetworking of physical devices, vehicles, buildings 
and other items -- embedded with electronics, software, sensors, actuators and network connectivity 
that enable these objects to collect and exchange data. 
(this definition seems to focus more on the variety of things..)


my own understanding
--------------------------------

*** motivation ***

daily things or objects (e.g. light, washing machine) are used to be not-communicative, except maybe those designed to do so (like computer, phone, satellite).  
1. when we want to know the status of the objects, we manually observe it (if there is lucky to have some status indicator);
2. when we want to switch on or off the objects, we manually do it. 
 
in daily life, this is usually not troublesome because we get used to it.
but still, there is room to improve the efficiency and save us time to do more important things.  
but what if point 1 and 2 can be done automatically by the object, or at least remotely by human?

e.g. what if we don't have to worry about cleaning house, turning off all appliances after leave house? what if air conditioners can self-adjust its temperature based on human reactions of body temperature? or maybe voice control the whole house?

the time save may already justify the usage of IoT at home.
but this is a small aspect.
the bigger aspect is the smart city and manufacturing sector.

let's talk about smart city first.  
private cars, traffic lights, parking lots, street lights, taxi, and even roads are all things.  
these things normally don't have much intelligence in them.

but what if cars are so smart they can drive by themselves?  
this will decrease road conjestion (because every car will try to choose a least conjested road), 
increase safety (no human errors).

traffic lights that can coordinate among themselves (or decide by a remote server) to dynamically make the path have more green time for the road that have more traffic? imagine the time for allowing cars to pass is a limited resource, so this is a problem of optimization of the usage of time given the traffic conditions. 

automate taxi can reduce cost of hiring a human and therefore free man power to do something more impoortant.

enough of smart city's smart traffic aspects. 
there are other aspects of smart city, like smart grid, that know the power usages of each household at realtime and able to make better power balancing decisions.  
and of course we need to have smart enviroment sensor network to report the environment conditions of the whole city so that city planners know better what to do.

what about the manufacturing sector?

automation is already there in manufacturing. can we do better?  
machines can break down.
but what if machines can report their health at real time?  
with these information, we can do predictive maintance, which save costs when machines suddenly break down.


*** technology ***

point 1 above indicates the need of sensors that capture some information of an object, which are useful for us to know the status of the object.  
to automate point 2, it indicates that the object needs some kind of communication capability, and computing power,
so that an object can act like a tiny computer that can report data and accept control msgs and do some actions and even make some decisions.  
therefore, sensors, communication, computing power seem the minimum requirements for IoT technology.

another aspect is the power consumption. 
for objects that stays indoor or have direct power connections, the power consumption may not be a critical issue.
but for objects in the remote area (e.g. enviroment monitoring), they will need to have extremely low power consumption and even able to harvest energy.

the sensors needed depend on the objects. 
e.g. smart air conditioners may need a sensor to detect human body temperatue;
smart cars need camera to capture the road condition and road signs.
smart traffic light system need some sensors (camera e.g.) to know the traffic conditions.
smart cranes need strain gauges to know if they have cracks.
machines need some kind of sensors to know their internal health.

some objects may not need any sensors (e.g. smart light bulb at home).

communication capability is needed for all smart objects.
at home, they could use wifi or even ethernet.  
at places where there is no wifi or ethernet, they need to use other communication technologies, 
like 802.15.4, or bluetooth, or z-wave, or other emerging low power communcation tech.

the requirement for computation power varies greatly for different objects.  
things like coffee machine may need a small computing power,
but things like smart cars will need to have powerful computing power.

of course, these are the lowest level of technolgies.  
higher-level technologies are needed.
e.g., what is the networking protocols? 
how to address each object? ipv6?
what is the managing platform?

the problem now is that we have too many ways of doing the same thing,
but no one agrees with each other.

to address so many different objects individually using a common way ('individually' and 'common' are the keys),
ipv6 seems a good way to go.  
of course, it is not the only way. we address a network of things as one entity and give it an ip address, but things inside the network can be addressed in any way.  
this will create many different types of subnetwork of things. 
if there is already a subnetwork of things using one addressing scheme, it is hard to add one more thing that uses another way of addressing. this is problematic.  
the best way is still that there is a common standard to address any objects.

how to create a standard that every manufacturers can manufacture their own things but all things can be plugged in to the same internet of things seamlessly?  
this is one big goal.
and maybe it will never come true.  
maybe in the end it is still fragmented: a few big manufacturers still have their own proprietary subnetworks.

or maybe integrating to one single type of network is not desired naturally, 
because different networks serves and exists in differnt scenario.
e.g. smart traffic lights network is very different from the smart home network..

maybe there will be different standards for differnt types of network.  
there could be a standard for smart home applicances;
another standard for smart cars;
another standard for manufacturing machines...

this is getting more confusing and complicated.

maybe personal computer is a place to seek inspiration.
different vendors creates differnt computers, which may run differnt OSes,
but all of they can communicate to each other.

1st step: consider all smart things to common tiny computers.
they all have sensors, communication capability and computing power.

2nd step: let's assume they are have the same addressing scheme: ipv6.
so each object can be reached directly by ipv6. 
this seems to make more advanced communication among different things much easier.

3rd step: we don't care about the physical and mac technologies. we are able to talk to each node.
if an object can link to internet directly, great.
if not, there must be a gateway there to handle the low level communication between the object and the gateway, just like the case in wifi.

4th step: after able to reaching each node (or vice versa), 
each node can have a lightweight https (or something else; let's call it a light-weight high-level communication protocol) 
to post data to a server or whatever computer, and receive data from remote server/computers (and even other objects). 
this light-weigh high-level communication protocol is very important to ensure different types of objects will be able to handle the same type of messages.

5th step: each object will have it own high-level applications that act on the data sensed or received.. this is to realize different objectives for different objects.

following steps 1 to 5, there seems to have a lot of possibilities for a general IoT network!


*** security ****

security is a super big issue here.

with more smart objects connected to the internet, 
the larger the surface for hackers to attack.

privacy can be violated if smart home is hacked.  
city can be thrown into chaos if smart traffic light system is hacked.  

there need to be some strict ways to do the communications in IoT.
and of course the software loaded in the smart objects have to be very reliable and have no loopholes for attackers to hack..

many standards
-----------------

question: standard of what? communication only? or message format?

there are  
	- Thread from google, 
	- AllJoyn from AllSeen Alliance, enlisting Cisco, Microsoft, LG, and HTC as memeber.  
	- Open Interconnect Consortium (open source) (An implementation: IoTivity)
	- Industrial internet consortium  
	- Google's Brillo

Summary: http://www.pcworld.com/article/3018835/internet-of-things/what-you-need-to-know-about-home-iot-standards-at-ces.html  
AllJoyn vs IoTivity: http://stackoverflow.com/questions/27947856/iotivity-vs-alljoyn-what-is-the-difference
Brillo vs Apple HomeKit vs AllJoyn vs IoTivity: http://www.techradar.com/news/world-of-tech/which-is-the-best-internet-of-things-platform-1302416
Brillo: http://www.forbes.com/sites/janakirammsv/2015/10/29/google-brillo-vs-apple-homekit-the-battleground-shifts-to-iot/#347395e84cac


IoT general
--------------------

reference: https://en.wikipedia.org/wiki/Internet_of_things

Internet of Things (IoT) is the internetworking of physical devices, vehicles,
buidlings and other items - embedded with electronics, software, sensors, actuators and network connectivity
that enable these objects to collect and exchange data.

some more specific technologies:  
	smart grid, smart homes, intelligent transportation and smart citites.

address: may use IPv6.

applications:  
	- environmental monitoring  
	- the subsea internet of things (applications related to aquativ sports)  
	- infrastructure management: bridges, railway tracks, wind farms  
	- manufacturing: management of manufacturing equiments, or within the manufacturing process control; predictive maintenance; IIOT: industrial internet of things    
	- energy management  
	- medical and healthcare  
	- building and home automation  
	- transportation  
	- comuser applications

to ensure unique addressability of things, each object may have an ipv6 address or URI.

alternatively, there could be a semantic web.. (semantic web can be explained in another folder)

intelligence: ambient intelligence and autonomous control.  
in the future may be a non-deterministic and open network in which auto-organized or intelligent entities (web services, SOA components),
virtual objects (avatars) will be interoperable and able to act independently
depending on the context, circumstances or environments.

architecture: could be event-driven architecture. 

network architecture: IPv6; or fog computing (edge processing)..  
some lightweight data transport protocols: COAP, MQTT, ZeroMQ.

size: 50 to 100 trillion objects (by when? globally?)

3 core sectors: enterprise, home and government. 

problem: "basket of remotes", where we will have hundreds of applications to interface with hundreds of devices
that don't share protocols for speaking with one another.  
	many manufacturers have begun releasing their devices with open APIs to address this problem.

frameworks:  
	- some focus on data logging: Jasper Tech and Xively  
	- software-development environment to create the software to work with the hardware used in the IoT: IBM's cognitive IoT, XMPP's initiative in Chatty Things  
	- REST (isn't this network architecture???)

enabling technologies: RFID, NFC, LiFi, Optical tag, bluetooth LE, ZigBee, Z-Wave, Thread, LTE-Advanced, WiFi-Direct, HaLow, HomePlug, MoCA, Ethernet

simulation: OPNET, NetSim, NS2

Government regulation on IoT: data security, data consent, data minimization.

criticism:  	
	- platform fragmentation  
	- privacy: some consider the possiblity that big data infrastructures such as IoT are inherently incompatible with privacy  
	- increased prevalence of digital surveillance (also privacy)  
	- concerns of the ability of IoT to erode people's control over their own lives  
	- security!!! (see next point)

security:  
	- may move too fast but pay little attention to security challenges  
	- IoT appliances can already spy on people in their own homes  
	- vehicle computer systems can be exploited remotely  
	- transport lights can be hacked too, creating chaos   
	- an open market for aggregated sensor data could server the interests of commerce as well as help criminals identify vulnerable targets  
	- there is this Internet of Thing Security Foundation (IoTSF) to handle security concerns


vision
---------------------

reference: http://computer.howstuffworks.com/internet-of-things.htm

smart homes: our appliances do our bidding automatically. 
the alrm sounds and the coffee pot starts brewing the moment you want to start your day.  
light come on as you walk through the house.  
some unseen computing device responds to your voice commands to read your schedule and
messages to you while you get ready.
your car drives you to work via the best route, 
freeing your up to your reading or prep for morning meeting while in transit.

sensors in city infrastructure can help reduce road congestion
and warn us when infrastructure is in danger of crumbling.

gadgets out in the open can monitor for changing environmental conditions
and warn us of impednding disasters.


IoT explained in howstuffworks
------------------------------
reference: http://computer.howstuffworks.com/internet-of-things.htm

smart devices can sometimes talk to other related devices (machine-to-machine communication),
and act on the info they get from one another.  
humans can interact with the gadgets..  
but the devices do most of the work on their own without human intervention.

embedded processing, sensing and communication equipment is being added to nearly any devices,
from bathroom scales to refrigerator, and even shoes.
there are also smart thermostats, smoke alarms, and security cameras.

what is internet of things (some points):  
	- once there are more devices (even from different manufacturers) can work with other devices,
we will be  able to automate lots of mundane tasks..

the tech behind iot:  
	- M2M communications
	- bluetooth, 6LowPan, 802.15.4, NFC, ZigBee, Z-Wave  
	- thru router; by via cellular  
	- computing hardware + embedded programming + sensors + communication hardware  
	- power harvesting..  
	- cloud-based software

technical issues:  
	- no universal standards or platforms to allow seamless interaction between all smart gadgets yet  
		-- different platforms: AllJoyn, IoTivity, Thread  
		-- smart device platform: Apple's HomeKit, google's project Brillo, SmartThings, Ninja blocks, evrythng, samsung's artik and wink..  
	- adoptation of ipv6 

devices:  
	- fitness trackers, heart monitors, smartwatches, smart clothing, tracker for pets  
	- household appliances: thermostats, water heaters, security cameras, lights ...  
	- connected garage doors and digital door locks  
	- smart devices for monitroing for hazardous road conditions, pollution levels, and water and energy consumption.  
	- smart cars, smart traffic lights  
	- healthcare: embedded sensors in hospital beds; tiny computing equipment that can be injected into the human body  
	- manufacturing: devices for monitoring status and condition of products; inventory tracking  
	- agriculture: monitor soll and crops; livestock can be tagged and located

security and privacy concerns:
	- target ads from big data analytics, which may cause some uncomfort to some people  
	- danger of connected devices being hacked  
	

economics impacts:  
	- automate processes and increase efficiency; reduce time lost to unexpected machine or system breakdowns  
	- increase some types of jobs (related to gadgets and data) but reduce some mundane jobs  


more references
------------------------

iot standards war: http://internetofthingsagenda.techtarget.com/blog/IoT-Agenda/Will-industry-muscle-win-in-the-IoT-standards-war

iot platforms like Amazon IoT Hub, WSO2 IoT platform, Watson IoT platform, Xively: 
http://www.cio.com/article/3085449/internet-of-things/iot-platform-wars-the-battle-for-the-4th-enterprise-platform.html

iot standards war: http://www.theregister.co.uk/2016/05/11/google_open_sources_thread_in_bid_to_win_iot_standards_war/

another on iot standard war: http://www.xda-developers.com/mirror-mirror-on-the-wall-will-smart-homes-rock-the-hall/

