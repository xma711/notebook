friend
--------------

if class A friends class B, class A allows class B to access its private and protected attributes.

does this decrease or enhance encapsulation?  
some say yes, some say no.

if class A creates getter and setter function for private attributes, it doesn't need to friend class B.  
but this may make class A more 'public' than it is supposed to be.  
so 'friend' can actually allows A to select who can modify its private attributes, 
which is equivalent to set getter and setter functions for some classes.

however, friend does create tighter coupling between 2 classes..   

more discussion: http://stackoverflow.com/questions/17434/when-should-you-use-friend-in-c
