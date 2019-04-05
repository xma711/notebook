Opnet is also event-driven.

Protocol
------------------
Each protocol can be implemented using a state machine.

Each protocol starts with an init state, then goes into the idle state. 
Then it waits for something to happen.
When a particular event happens, it goes to the respective state and after completing the works comes back to the idle state.


Node
---------------------
A node can be created by the node editor, which links all the modules together.


Scenario/project
------------------------
Each scenario (or so-called project) are made of by nodes. user places nodes in the project editor and set the nodes' parameters and the system-wide parameters.
