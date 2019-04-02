MQTT
------------------------------

Reference: https://en.wikipedia.org/wiki/MQTT

MQTT is a pub-sub-based messaging protocol.

It uses TCP/IP.

There is a message broker.  
One popular choice is Mosquitto, an open source mqtt broker. (https://mosquitto.org/) 

There are subscribers and publishers.  
Both pub and sub use topics to send or receive messages or files.


MQTT-SN
-------------

Reference: http://www.steves-internet-guide.com/mqtt-sn/

MQTT-SN uses UDP instead of TCP of its transport.

"MQTT-SN is designed to work in the same way as MQTT".  
"In that regard MQTT-SN usually requires a connection to the broker before it can send and receive messages."

Like MQTT, MQTT-SN supports QoS of 0, 1 and 2.
In addition, MQTT-SN supports publish QoS o 3 or -1,
using which it doesn't require an initial connection to have been set up.

MQTT-SN can register with a broker a (long) topic and obtain a topic id in return (it can use the topic in the usual way too).
This obviously is to reduce message overhead when publishing or subscribing using the topic id.  
Note that topic id is not global.
For different MQTT-SN clients, the same topic id may not refer to same (long) topic.

MQTT-SN broker is not the same as MQTT broker.
One MQTT-SN broker implementation is RSMB: http://www.steves-internet-guide.com/mqtt-sn-rsmb-install/

If one really wants to use MQTT-SN with a MQTT broker, a MQTT-SN gateway is needed
(https://www.eclipse.org/paho/components/mqtt-sn-transparent-gateway/)
.


