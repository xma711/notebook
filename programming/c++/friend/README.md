Friend
--------------

If class A friends class B, class A allows class B to access its private and protected attributes.

Does this decrease or enhance encapsulation?  
Some say yes, some say no.

If class A creates getter and setter function for private attributes, it doesn't need to friend class B.  
But this may make class A more 'public' than it is supposed to be.  
So 'friend' can actually allows A to select who can modify its private attributes, 
which is equivalent to set getter and setter functions for some classes.

However, friend does create tighter coupling between 2 classes..   

More discussion: http://stackoverflow.com/questions/17434/when-should-you-use-friend-in-c
