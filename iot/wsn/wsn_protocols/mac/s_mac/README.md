s-mac
---------------

a relatively fixed schedule of sleep-awake schedule.

each active slot has: SYNC, RTC, CTS and DATA.

They need to sync to each other so that they can wake up at the same time.

however, if some nodes follow a different schedules, 
other nodes have to follow both schedules if they learn about that there are two different schedule in the network.

the cons of s-mac is that it is inflexible. 
it is basically a blackbox and upper layer cannot change any parameters.

b-mac is a better protocol. see b-mac details.
