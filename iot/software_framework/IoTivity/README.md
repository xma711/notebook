IoTivity
--------------

Ref: https://blogs.s-osg.org/layered-architecture-iotivity/

IoTivity is radio-independent.

It has a few high level layers (using OSI model as a reference).  
It can be seen that it has its own network layer, security stuff, its own managing layer/service above network layer.

Connectivity abstraction: this layer provides a common platform for all "bearers" like Bluetooth EDR, IPV4/V6 stack, XMPP..  

Security: security is provided at 2 layers: transport and application.  
	- transport: encryption of packets. relies on Datagram transport layer security (DTLS) to provide encryption.  
	- application: access control list (ACL) to control access to resources.

C stack: OIC representation and payload are defined in the c stack.  
The protocol used in this layer is CoAP, a HTTP-like lightweight protocol.

C++ API: a thin layer that exposes the c stack API to other modules.
It is intended for the server and clients to use this API to write the IoT application on top of the C stack.
