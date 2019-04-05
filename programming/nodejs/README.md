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
Then we can just anyhow arrange these tasks and let them run. 
The mindset is very different from writing procedural programming.

Another pattern is that if certain task can be executed after some other tasks, 
then we can use async module to arrange them in certain order.
But this order exists within the async function only and other tasks outside are still running asynchronously with this async function.

If every task is strictly sequential, then async.series() can handle this;
but it is questionable that node.js is the best choice in this case.


Install new package
-----------------------

Npm install module_name (the module will be installed in the current directory)

To list all the locally installed module: npm ls

To install a module globally: npm install module_name -g

To list globally installed module: npm ls -g

To see the details of a package, we can use node_modules/module_name/package.json.

To uninstall a module: npm uninstall module_name.

To update a module: npm update module_name

To search a module: npm search module_name


create a module
--------------------

One can create a module and publish to a public repo so everyone can download it

Refer to my_own_codes/: greeting_export.js and greeting_import.js


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

Anyway, function can be c-like; 
or we can set a variable equals to this function header, and then the variable behaves like the function.

No references are passed into a function; 
unless the argument's content is already a reference (like var x = {value:1}, then x is already a reference)

Other notes:

1. When call a function, if it has no arguments, still have to call it by function_name(). like c, the () cannot be omitted.  
	However, unlike c, even if we forget to put the (), it won't complain, which makes it harder to be debugged

2. A callback function as an argument to another function shouldn't have arguments.   
	e.g. "SetTimoeout(callback(), 2000)" is wrong. the callback function won't be executed in 2s. it will be executed immediately!  
	The correct way is "SetTimoeout(callback, 2000)".  
	The reason that a callback function has no argument is that it should be a function pointer only; 
	The caller will use this callback function to execute something like callback() or callback(other arguments) inside the caller function.

3. Nodejs won't wait for the return of a function. but once the callback in a function is executed, the thread will execute this callback until it is done, 
	Before moving on to the next callback.   
	Note that callback function shouldn't have any blocking, which defeats the purpose of nodejs.   
	Delays should be handled by timers.

4. Function and other traditional objects (like int, string) are very similar.  
	A function can be declared and used immediately, or saved to a variable first (var func = function() {...} ) and use the variable later.

5. If a function is to return an object, the function can be used as if it is the object that has been returned, which is very different from c.  
	e.g. if function() is to create a server, in nodejs, we can use function().listen(8081) , which is equivalent to  
	server = function(); server.listen(8081)

6. Any callback function (or normal function) (function a) declared inside another function (function b) has access to all the resources defined in the parent function (i.e. function b).  
	Function a has access to function b's resources even if it is used as an callback argument to another function (function c) inside function b.  
	This is important because a callback function inside a primary function can imagine the primary function is always alive and it can continue whatever actions needed on the 
	resources of primary function at a later time.  
	We don't have to think about how to pass something to a callback function at a later time.

7. Inside a function, if we want to set a timer to handle something later (need to pass in arguments to the callback for the setTimeout()), we can use a function wrapper with no argument to wrap around a callback function that can have arguments from the primary function.  
	Refer to my_own_codes/: create_sync_function.js 
