LoRa
----------------------

ref: https://www.link-labs.com/what-is-lora/

LoRa itself is a physical layer protocol, \
which does not describe any system functionalities above the physical layer.  

LoRa defines a modulation format.
It generates a stable chirp (??) using a fac-N phase lock loop (PLL) (??).


LoRa alliance
---------------------

LoRa alliance is to standardize the MAC features for LoRa.  
the analogy is to going from having a BPSK radio chip to having a WiFi network.

the output is LoRaWAN.


LoRaWAN
--------------------

LoRaWAN network architecture is typically a star-of-stars topology 
in which gateways are a transparent bridge relaying messages 
between end-devices and a central network server in the backend.

it is designed primarily for uplink-only applications with many endpoints..
or applications that need only a few downlink messages.

LoRaWAN is a server-side implementation of a multiple access protocl 
designed to minimize collisions with a large number of endpoints. 
it requires a server application to run the MAC functions over a network connection.

the LoRaWAN network server manges the data rate and RF output for each end-device individually
by means of an adaptive data rate (ADR) scheme that is typically updated once every 24 hrs.

question: if LoRaWAN is a server-side implementation, the what is the MAC protocol implementation for gateway and end devices?

question: it seems we need a server, a gateway and end devices. will this complicate things?


more info
----------------

another ref: http://embeddedexperience.blogspot.sg/2015/08/lora-network-server.html

the network server plays central role.  
gateway is intended to be a simple packet forwarder.

there are multiple LoRa network server providers: IBM LRSC, Activity ThingPark, Orbiwise UbiQ.  

this means that with LoRa devices and gateways, it could still be useless if we don't have a network server..


competitors
-----------------

NB-IoT and Sigfox.
