Broken window theory
---------------------------

One broken window, left unrepaired for a substantial length of time, 
will accelerate a building's damage.

If you find yourself working on a project with quite a few broken windows,
it is all too easy to slip into the mindset of
"all the rest of this code is crap, i will just follow suit."

Tip: don't leave broken windows (bad designs, wrong decisions, or poor code) unrepaired.
Fix each one as soon as it is discovered.


Knowledge is expiring asset
------------------------------

Your knowledge becomes out of data as new techniques, languages and environments are developed.

We need to continuously invest in knowledge portfolio, much like the financial portfolio.


Communication
----------------------

Both verbally and thru documents/emails.

Know what you want to say;  
know your audience;  
choose your moment;  
choose a style;  
make it look good;  
involve your audience;  
be a listener;  
get back to people


DIY - Don't Repeat Yourself
------------------------

When we write client-server application using different languages, and need to represent some shared structure on both,
it seems unavoidable to write the same structure in two different ways.  
The solution to remove the need for duplication is to  write a simple filter or code generator, 
that generate structure in different languages from a common metadata file.
(actually, this is to add one more layer of abstraction, as taught in computer architecture module.)

External document and code both contain representation of the same knowledge.   
(now i understand why doxygen is a useful tool. it generates document from codes.)

Comments in header and implementation file ->
there is no point duplicating a function or class header comment between the two files.
Use the header files to document interface issues,
and the implementation files to document the details that users of your code don't need to know.

Shortcuts make for long delays!!!
Try to avoid being lazy by simply coping a section of codes from one file to another.

It takes disciplines and willingness to spend time up front to save pain later.


Orthogonality
---------------------

In math, two lines are orthogonal if they meet at right angles.

In computing, it signifies a kind of independence or decoupling.

In a well-designed system, the database code will be orthogonal to the user interface:
you can change the interface without affecting the database,
and swap databases without changing the interface.

We want to design components that are self-contained:
independent, and with a single, well-defined purpose.
When components are isolated from one another, 
you can change one without having to worry about the rest.

Two benefits: increased productivity and reduced risk.

When teams are organized with lots of overlap,
members are confused about responsibilities.
Every change needs a meeting of the entire team,
because any one of them might be affected.

One way to organize teams into groups with well-defined responsibilities and minimal overlap:
separate infrastructure from application.
Each major infrastructure component (database, communication interface, middleware layer etc) gets its own subteam.
Each obvious division of application functionality is similarly divided.  
A measure of the orthogonality of a project team: 
see how many people need to be involved in discussing each change that is requested.
The larger the number, the less orthogonal the group.

There is an easy test for orthogonal design. 
Once you have your components mapped out,
ask yourself: if i dramatically change the requirements behind a particular function,
how many modules are affected?
In an orthogonal system, the answer should be one.
E.g. moving a button on a GUI panel should not require a change in the database schema.

When you bring in a toolkit/library, ask yourself whether it imposes changes on your code that shouldn't be there.
If it requires you to create or access objects in a special way, then it's not orthogonal.
(my own thinking: one solution maybe is to add one more layer in your code, 
so that when the toolkit is replaced by another one, most of the codes don't have to be changed.)

How to maintain orthogonality:  
	- keep your code decoupled. 
	write shy codes - modules that don't reveal anything unnecessary to other modules
	and don't rely on other modules' implementations.  
	- avoid global data. 
	every time your code references global data, it ties itself into the other components that share that data.
	better just pass any required context into your modules.
	in object-oriented applications, context is often passed as parameters to objects' constructors.  
	- avoid similar functions.

Building unit tests is itself an interesting test of orthogonality.
Do you have to drag in a large percentage of the rest of the system 
just to get a test to compile or link?
If so, the module is not well decoupled from the rest of the system.

Orthogonality also applies to documentation.
The axes are content and presentation.
With truly orthogonal documentation, you should be able to change 
the appearance dramatically without changing the content.
(one obvious example is Latex. However, it takes longer time to write in latex than in word.)

Orthogonality is closely related to the DRY principle.
If you use the principle of orthogonality, combined closely with the DRY principle,
you will find that the system you develop are more flexible,
more understandable, and easier to debug, test and maintain.


Assertion
---------------

Whenever you find yourself thinking "but of course that could never happen",
add code (assertion) to check it.  
(if it can't happen, use assertions to ensure that it won't.)

But don't use assertions in place of necessary error handling.

E.g. for program like waiting for user input,
a user may input wrongly. 
A nicer way is to handle to error by printing why the input is wrong and asking the user to enter again.  
(imagine a wrong input at a field when buying airticket will cause the whole session to crash..)

Your first line of defense is checking for any possible error,
and your second is using assertions to try to detect those you've messed.

Turning off assertions when you deliver a program to production 
is like crossing a high wire without a net
because you once made it across in practice.

However, we need to make sure the assertions used has no side effects.  
We shouldn't do something like "Test.ASSERT(iter.nextElements() != null); object obj = iter.nextElement();"
because it has the side effects of moving the iterator past the element being fetched.  
This problem is kind of "Heisenberg" - debugging that changes the behavior of the system being debugged.


Exception
---------------------

If your code tries to open a file for reading and that file doesn't exist, should an exception be thrown?

It depends.

If the file should have been there, then an exception is needed.
Something unexpected happened - a file you were expecting to exist seems to have disappeared.
On the other hand, if you have no idea whether the file should exist or not,
then it doesn't seem exceptional if you can't find it,
and an error return is appropriate.

Throw exceptions for exceptional problems.

Programs that use exceptions as part of their normal processing suffer from all the readability
and maintainability problems of classic spaghetti code.
These programs break encapsulation:
routines and their callers are more tightly coupled via exception handling.


Allocate and free
------------------

The routine or object that allocates a resource should be responsible for deallocating it.

