ERST
--------------------

unlike TCP, ERST wants to make sure a sink has enough data for an event detection.

in a normal WSN application, usually the sink doesn't need 100% data reception from all nodes
for event detections.

assume the required reliability = R (number of packets needed during a slot),
and r = observed reliability.

also nodes are able to detect whether the network is congested by checking their buffer. 
if they receive too many packets their buffer will tend to be full or more than that. 
nodes can inform sink about the congestion status.

then the sink will form a state: (congestion_status, r/R).  
if the state is (NC, LR or r/R<1), it means it is not congested and reliability is too low.
sink will then inform the nodes to increase the frequency f based on an equation fi+1 = fi/ni 
where ni = ri/Ri.
and then nodes will increase frequency in the next slot.

for every different state, sink will take some actions.
the only exception is the state OOR, which is the optimal state with n = 1 roughly.  
then sink will let the nodes use the same frequency.

check the paper for more details, esp about the state transition diagram.

