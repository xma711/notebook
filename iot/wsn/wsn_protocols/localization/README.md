bulusu
--------------------------

quite a simple protocol.

just distribute some reference nodes with known locations in an OPEN area. 
the communication ranges are purposely overlapping.

a sensor node will just listen to these reference nodes for S samples from each reference point, 
and check how many packets it receives.  
if the value Nrcvd/Nsent > a threshold, then the reference point is counted; 
else the reference point is ignored.

so the node will have a list of reference points.  
to estimate its own location, simply compute the centroid of these references points.  
ie x_est = sum of x from all valid reference points / number of valid reference points, 
and same for y_est.

the localization error is sqrt( (x_est - x_true)^2 + (y_est -y_true)^2 ).

note that this protocol doesn't work in indoor environment coz its assumption on radio propagation
is that it is spherical propagation model.


cricket
----------------------------
 
many beacon nodes. 
each of them transmites a radio signal and an ultrasonic signal at the same time.  
because radio speed is much faster, a node will receives the radio first.
then the node can switch to listen to the ultrasonic signal.
based on the time difference, the node can compute the distance between itself to the beacon.

there are many beacons nodes, so the node has to correlate the pairs {radio, ultrasonic} signals. 
later the node will pick the best beacon to be the reference point.

to pick the best beacon, it can choose the one that it receives the most frequently,
so the one that has the shortest distance to it,
or the one that has the smalest modal whatever to it (not clear..).


bat
---------------------------

bat is similar to cricket,
but instead of beacons nodes transmit, 
a sensor node with a transimtter named bat will transit signal instead.

steps:  
a base station broadcast a radio signal, 
and after listening this, a bat broadcasts a ultrasonic signal.

reference points hear both the radio and the ultrasonic, so they can compute the location of the bat.  
they then store the info to a database.
