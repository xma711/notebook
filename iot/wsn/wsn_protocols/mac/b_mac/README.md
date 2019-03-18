B-mac
------------------

Improve from s-mac.

It doesn't need nodes to be sync.

Nodes just follow their own sleep-wakeup schedule.

Whenever some nodes want to send something, 
they send a long preample (at least as long as the sleep time)
to let nearby nodes know about a coming pkt when they wake up.
Then the nodes can receive the packet when they are awake.

Rts/cts/ack are considered higher-layer requirements.
They are disabled by default.
High layer can enable them when needed.

About listening to the channel, b-mac uses this clear channel assessment (cca) method.
A node sample the energy level when channel is clear and get a noise floor.
When they need to check the channel, they listen to the channel and try to obtain outliers that are smaller than the noise floor.
If there are such outliers, the channel must be clear.

Comparing to some other protocols that take a sample to check if a channel is free,
cca increases the reliabilty of checking.

B-mac is much better than s-mac.
