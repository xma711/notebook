S-mac
---------------

A relatively fixed schedule of sleep-awake schedule.

Each active slot has: SYNC, RTC, CTS and DATA.

They need to sync to each other so that they can wake up at the same time.

However, if some nodes follow a different schedules, 
other nodes have to follow both schedules if they learn about that there are two different schedule in the network.

The cons of s-mac is that it is inflexible. 
It is basically a blackbox and upper layer cannot change any parameters.

B-mac is a better protocol. see b-mac details.
