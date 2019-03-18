Basics
----------------

Internally, ns2 modules are implemented by C++.

The outer shell of ns2 is implemented by otcl, which links up the c++ modules.

Externally, users use tcl or otcl to create network scenario.



Internal
---------------
Each module is inherited from a very baisc c++ class, which provides an interface for it to bind to otcl and provides a pointer for it to link to the next module.
