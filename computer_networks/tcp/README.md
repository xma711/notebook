How does TCP work?
---------------------------

It is a transport-layer protocol, to ensure reliability.

Each host maintains 3 windows: congestion window, advertised window and transmission window.  

Congestion window is for sender to indicate the maximum number of segments (packets) a sender can transmit without congesting the network; 
the number is based on the feedback (e.g. ACKs, lost packets..) from the network.  
	- if sender cannot receive ACK with RTO, it immediately reduces its congestion window to one segment & expoentially backs off its RTO..
	
Advertised window is for receiver to indicate to the sender in the ACK that the amount of data 
the receiver is ready to receive in the future.  
Normally it is equal to the available buffer size at the receiver to prevent buffer overflow.

Transmission window: deterimine the maximum number of segments that the sender can transmit at one time 
without receiving any acks from the receiver. 
The size is determined as the minimum of the sender's congestion window and receiver's advertised window.

TCP uses a cumulative ACK mechanism.  
When a sender receives an ACK about the nth packet, it knows all packet < n have been received (not including n).

When receiver receives an out-of-order segment, it will send a duplicated ack to the sender. 
In wireline network, an out-of-order delivery usually implies a packet loss (the packet missing is the one lost).

If 3 duplicate cumulative ACKs are received, the sender assumes the packet is lost.

Another case that sender thinks that a packet is lost is when an ACK never comes within the RTO (retransmission timeout) interval. 
RTO = RTT (round-trip time) + 4 * mean deviation.

Upon detecing lost packet, the sender will retransmit the lost packet. (just the single packet? or the packet indicated in ack + all packets after?)


TCP in cellular networks
-------------------------

The usual scenario:  
Mobile Host (MH) --- Base station (BS) ---- FH (fixed host)

MH -- BS link is unreliable but may not be congested.  
The packets lost in the link will make FH to think the end-to-end link (FH --- MH) is congested and FH will reduce the congestion window unnecessarily.
TCP performance will be bad.

Two ways to handle this:  
	1. separate MH -- FH connections to 2 connections, one normal TCP between BS and FH and one wireless-link aware TCP between MH and BS. 
		however, this violates the end-to-end semantics of TCP

	2. snooping module at the BS. When FH sends data to MH, BS caches data that have not been acked. 
		when MH sends duplicated ACKs, FH retransmits the data to MH, without forwarding the duplicated ACKs to FH, 
		so that FH won't shrink its congestion window. 
		when MH sends data to FH, the TCP selective ACKs option is used. 
		when BS detects missing packets, BS will send selective ACKs to the MH so that MH will transmit the lost packets within one RTT. 

