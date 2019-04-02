LoRa
----------------------

Ref: https://www.link-labs.com/what-is-lora/

LoRa itself is a physical layer protocol, \
which does not describe any system functionalities above the physical layer.  

LoRa defines a modulation format.
It generates a stable chirp (??) using a fac-N phase lock loop (PLL) (??).


LoRa alliance
---------------------

LoRa alliance is to standardize the MAC features for LoRa.  
The analogy is to going from having a BPSK radio chip to having a WiFi network.

The output is LoRaWAN.


LoRaWAN
--------------------

LoRaWAN network architecture is typically a star-of-stars topology 
in which gateways are a transparent bridge relaying messages 
between end-devices and a central network server in the backend.

It is designed primarily for uplink-only applications with many endpoints..
Or applications that need only a few downlink messages.

LoRaWAN is a server-side implementation of a multiple access protocol 
designed to minimize collisions with a large number of endpoints. 
It requires a server application to run the MAC functions over a network connection.

The LoRaWAN network server manages the data rate and RF output for each end-device individually
by means of an adaptive data rate (ADR) scheme that is typically updated once every 24 hrs.

Question: if LoRaWAN is a server-side implementation, the what is the MAC protocol implementation for gateway and end devices?

Question: it seems we need a server, a gateway and end devices. will this complicate things?


More info
----------------

Another ref: http://embeddedexperience.blogspot.sg/2015/08/lora-network-server.html

the network server plays central role.  
Gateway is intended to be a simple packet forwarder.

There are multiple LoRa network server providers: IBM LRSC, Activity ThingPark, Orbiwise UbiQ.  

This means that with LoRa devices and gateways, it could still be useless if we don't have a network server..


Competitors
-----------------

NB-IoT and Sigfox.
