Run a program
--------------------
Nodejs program_name

or just run nodejs in a terminal, and it will be an interactive shell like python

tutorial
---------------
Http://www.tutorialspoint.com/nodejs/nodejs_first_application.htm


patterns
-----------------------

Because node.js is async programming, one obvious pattern of a program is that every task is async.
Then i can just anyhow arrange these tasks and let them run. 
The mindset is very different from writting procedural programming.

Another pattern is that if certain task can be executed after some other tasks, 
then i can use async module to arrange them in certain order.
But this order exists within the async function only and other tasks outside are still running asynchronously with this async function.

If every task is strictly sequential, then async.series() can handle this;
but i don't know whether node.js is the best choice of programming language in this case.


Install new package
-----------------------

Npm install module_name (the module will be installed in the current directory)

to list all the locally installed module: npm ls

to install a module globally: npm install module_name -g

to list globally installed module: npm ls -g

too see the details of a package, i can use node_modules/module_name/package.json.

To uninstall a module: npm uninstall module_name.

To update a module: npm update module_name

to search a module: npm search module_name


create a module
--------------------

One can create a module and publish to a public repo so everyone can download it

refer to my_own_codes/: greeting_export.js and greeting_import.js

events 
--------------------

This is very fundamental. 
Many complicated modules are built on top of events and they are events!

Similar to qualnet events. but each event name can be binded to multiple listeners (functions)

when an EventEmitter instance faces any error, it emits an error event.
When new listener (just a function) is added, newListener event is fired and
when a listener is removed, removeListener event is fired.

Refer to all the APIs at http://www.tutorialspoint.com/nodejs/nodejs_event_emitter.htm

see examples: my_own_codes/2events.js, my_own_codes/listen_to_event.js


functions
----------------
See examples: in my_own_codes/: async_functions_while_loop.js  callback_function.js  function.js  seq_functions_while_loop.js  simplefunction.js

anyway, function can be c-like; 
or i can set a variable equals to this function header, and then the variable behaves like the function.

No references are passed into a function; 
unless the argument's content is already a reference (like var x = {value:1}, then x is already a reference)

other notes:

1. when call a function, if it has no arguments, still have to call it by function_name(). like c, the () cannot be omitted.  
	however, unlike c, even if i forget to put the (), it won't complain, which makes it harder to be debugged

2. a callback function as an argument to another function shouldn't have arguments.   
	e.g. "SetTimoeout(callback(), 2000)" is wrong. the callback function won't be executed in 2s. it will be executed immediately!  
	the correct way is "SetTimoeout(callback, 2000)".  
	the reason that a callback function has no argument is that it should be a function pointer only; 
	the caller will use this callback function to execute something like callback() or callback(other arguments) inside the caller function.

3. nodejs won't wait for the return of a function. but once the callback in a function is executed, the thread will execute this callback until it is done, 
	before moving on to the next callback.   
	note that callback function shouldn't have any blocking, which defeats the purpose of nodejs.   
	delays should be handled by timers.

4. function and other traditional objects (like int, string) are very similar.  
	a function can be declared and used immediately, or saved to a variable first (var func = function() {...} ) and use the variable later.

5. if a function is to return an object, the function can be used as if it is the object that has been returned, which is very different from c.  
	e.g. if function() is to create a server, in nodejs, i can use function().listen(8081) , which is equivalent to  
	server = function(); server.listen(8081)

6. any callback function (or normal function) (function a) declared inside another function (function b) has access to all the resources defined in the parent function (i.e. function b).  
	function a has access to function b's resources even if it is used as an callback argument to another function (function c) inside function b.  
	this is important because a callback function inside a primary function can imagine the primary function is always alive and it can continue whatever actions needed on the 
	resources of primary function at a later time.  
	i don't have to think about how to pass something to a callback function at a later time.

7. inside a function, if i want to set a timer to handle something later (need to pass in arguments to the callback for the setTimeout()), i can use a function wrapper with no argument to wrap around a callback function that can have aruguments from the primary function.  
	refer to my_own_codes/: create_sync_function.js 
