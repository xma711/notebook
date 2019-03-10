b-mac
------------------

improve from s-mac.

it doesn't need nodes to be sync.

nodes just follow their own sleep-wakeup schedule.

whenever some nodes want to send something, 
they send a long preample (at least as long as the sleep time)
to let nearby nodes know about a coming pkt when they wake up.
then the nodes can receive the packet when they are awake.

rts/cts/ack are considered higher-layer requirements.
they are disabled by default.
high layer can enable them when needed.

about listening to the channel, b-mac uses this clear channel assessment (cca) method.
a node sample the energy level when channel is clear and get a noise floor.
when they need to check the channel, they listen to the channel and try to obtain outliers that are smaller than the noise floor.
if there are such outliers, the channel must be clear.

comparing to some other protocols that take a sample to check if a channel is free,
cca increases the reliabilty of checking.

b-mac is much better than s-mac.
