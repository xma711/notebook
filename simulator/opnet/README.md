opnet is also event-driven.

protocol
------------------
each protocol can be implemented using a state machine.

each protocol starts with an init state, then goes into the idle state. 
then it waits for something to happen.
when a particular event happens, it goes to the respective state and after completing the works comes back to the idle state.


node
---------------------
a node can be created by the node editor, which links all the modules together.


scenario/project
------------------------
each scenario (or so-called project) are made of by nodes. user places nodes in the project editor and set the nodes' parameters and the system-wide parameters.
