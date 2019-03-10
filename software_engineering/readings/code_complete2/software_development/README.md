software development

reference: code complete 2

activities
------------------
Distinct activies that go into software development:
	- problem definition
	- requirements development
	- construction planning
	- software architecture, or high-level design
	- detailed design
	- codeing and debugging
	- unit testing
	- integration testing
	- integration
	- system testing
	- corrective maintenance

metaphor
--------------
Treating software construction as similar to building construction suggests that
careful preparation is needed and illuminates the difference between larger and small projects.


prerequisites
---------------------
including:
	- problem definition
	- requirement development
	- software architecture

Measure twice, cut once.

if you emphasize quality at the beginning of the project, you plan for, require and design a high-quality product.
... in software development, you do such planning when you define the problem, when you specify the solution and when you design the solution.

if you emphasize quality in the middle of the project, you emphasize construction practices. (focus of the book)

if you emphasize quality at the end of the project, you emphasize system testing. 
... testing can't detect a flaw such as building the wrong product or building the right product in the wrong way. 
such flaws must be worked out earlier than in testing - before construction begins.

industry data from 1970s to the present day indicates that projects will run best
if appropriate preparation activities are done before construction begins in earnest.

why isn't sam coding anything? (WISCA phenomenon)

programmers are at the end of the software food chain.
the architect consumes the requirements; 
the designer consumes the architecture; 
and the coder consumes the design.

purging an error by the beginning of construction allows rework to be done 10 to 100 times less expensively than 
when it's done in the last part of the process, during system test or after release.

about architecture:

The quality of the architecture determines the conceptual integrity of the system.
that in turn determines the ultimate quality of the system.

a puzzle of 12 subsystems is harder to put together, and if you can't put it together, 
you won't understand how a class you're developing contributes to the system.

a building block should have one area of responsibility, 
and it should know as little as possible about other building blocks' areas of responsibility.

the communication rules for each building block should be well defined.
the architecture should describe which other building blocks the building block can use directly,
which it can use indirectly, and which it shouldn't use at all.

the architecture should clearly describe a strategy for handling changes.

good software architecture is largely machine- and language-independent. 
by being as independent of the construction environment, you avoid the temptation to overarchitect the system 
or to do a job that you can do better during construction.

architecture shouldn't contain anything just the please the boss. 
it shouldn't contain anything that's hard for you to understand.
if it doesn't make sense to you, how can you implement it?

class designs: aim for 80/20 rule: specify the 20% of the classes that make up 80% of the system's behavior.

regarding error processing:

some people have estimated that as much as 90% of a program's code is written for exceptional, error processing cases or housekeeping.

error is best treated at the architectural level.

is error processing corrective or merely detective? if corrective, the program can attempt to recover from errors. 
if it's merely detective, the program can continue or quit. in either case, it should notify the user that it detected an error.

is error detection active or passive? the system can actively anticipate errors - e.g. checking user inputs. 
in either case, the choice has user-interface implications.

how does the program propagate errors? it can immediately discard the data that caused the error;
it can treat the error as an error and enter an error-processing state, etc.

what are the conventions for handling error messages? the architecture should establish conventions for error messages.

how will exceptions be handled? the architecture should address when the code can throw exceptions, 
how they will be logged, how they will be documented..

what is the level of responsibility of each class for validating its input data?

the most radical solutions to building software is not to build it at all - to buy it instead 
or to download open-source software for free. 
you can buy GUI controls, database managers, image processors, graphics and charting components, 
internet communications components, etc.

amount of time to spend on upstream prerequisites
--------------------------------------------
Generally, a well-run project devotes about 10% to 20% of its efforts 
and about 20% to 30% of its schedule to requirements, architecture, and up-front planning. 
these figures don't include time for detailed design - that's part of construction.

if requirements are unstable on any project - formal or informal - 
treat requirements work as its own project. 
estimate the time for the rest of the project AFTER you've finished the requirements.

checklist for upstream prerequisites:
	- have you identified the kind of software project your're working on and tailored your approach appropriately?
	- are the requirements sufficiently well defined and stable enough to begin construction?
	- is the architecture sufficiently well defined to begin construction?
	- have other risks unique to your particular project been addressed, such that construction is not exposed to more risk than necessary?

key points:
	- the overarching goal of preparing for construction is risk reduction.
	- if you want to develop high-quality software, attention to quality must be part of the software-development process from beginning to the end. 
attention to the quality at the beginning has a greater influence on product quality than attention at the end.
	- part of a programmer's job is to educate bosses and coworkers about the software-development process, 
including the importance of adequate preparation before programming begins.
	- the kind of project your're working on significantly affects construction prerequisites. 
many projects should be highly iteractive and some should be more sequential.
	- if a good problem definition hasn't been specified, you might be solving the wrong problem during construction.
	- if good requirements work hasn't been done, you might have missed important details of the problem.
requirements changes cost 20 to 100 times as much in the stages following construction as they do earlier, 
so be sure the requirements are right before you start programming.
	- if good architecture design hasn't been done, you might be solving the right problem the wrong way during construction. 
the cost of architectural changes increases as more code is written for the wrong architecture, 
so be sure the architecture is right, too.
	- understand what approach has been taken to the construction prerequisites on your project, 
and choose your construction approach accordingly.

programming languages
-----------------------
programmers are more productive using a familiar language than an unfamiliar one. (30% more productive)

languages such as c++, java, visual basic have been credited with improving productivity, reliability, simplicity, 
and comprehensibility by factors of 5 to 15 over low-level languages such as assembly and c.

before construction begins, spell out the programming conventions you'll use. 
coding-convention details are at such a levle of precision that they're nearly impossible to retrofit into software after it's written.

if you are in the late part of the technology wave, you can plan to spend most of your day steadily writing new functionality.
if you are in the early part of the wave, you can assume that you'll spend a sizeable portion of your time trying to 
figure out your programming language's undocumented features, debugging errors, revising codes etc.

understanding the distinction between programming in a language and progrmming into one is critical to understanding this book. 
programmers who program into a language first decide what thought they want to express, 
and then they determine how to express those thoughts using the tools provided by their specific language.

some projects use pair programming and test-first development, 
while others use solo development and formal inspections.

key points:
	- every programming language has strengths and weakness. 
be aware of the specific strenghs and weaknesses of the language you're using.
	- establish programming conventions before you begin programming. 
it is nearly impossible to change code to match them later.
	- most construction practices exist than you can use on any single project. 
consciously choose the practices that are best suited to your project.
	- remember to programming into the language, rather than programming in it.
	- your position on technology wave determines what approaches will be effective. 
identify where you are on the technology wave, and adjust your plans and expectations accordingly.


