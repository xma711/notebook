objective
------------------

every change that is made to an application's configuration, source code, environment, or data,
triggers the creation of a new instance of the deployment pipeline.

a deployment pipeline is an automated implementation of your application's build, deploy, test and release process.

the aims:  
	1. it makes every part of the process of building, deploying, testing and releasing software visible to everyboday involved, aiding collaboration.  
	2. it improves feedback so that problems are identified, and so resoved, as early in the process as possible.  
	3. it enables teams to deploy and release any version of their software to any environment at will through a fully automated process. 


configuration
--------------------

we should treat configuration files like source codes.  
they have to be version-controlled of course.  
the whole environment (production or testing) should be able to be produced from the scripts and configurations file from the repository alone.  
the configuration files for the app have to be maintained in this way too.

more over, configuration files should be tested too.

i think one way to make sure the production or testing environment can be produced from configuration files is to use docker.  
by writing the Dockerfile for different env, it is easy to produce the OS.  
however, for network-wide environment, we may still need to use some scripts to auto deploy the docker images to multiple machines.


continuous integration
-----------------------------

every commit should trigger the the automated testing of the whole repository.  
unit testing is definitely one of the automated tests.  
what else?  
the other 2 tests we need are component tests and acceptance tests.  
component tests test the behaviour of several components of your application. (how to decide which group of components to be tested together is another question).  
acceptance tests test that the application meets the acceptance criteria decided by the business, 
including both the functionality provided by the application and its characteristics such as capacity, availability, security and so on.  
acceptance tests are best written in such a way that they run against the whole application in a production-like environment.

CI tools: jenkins (previously known as Hudson), and CruiseControl.

there are some tools to check coding style/practices: Simian (identify duplication), JDepend for Java, CheckStyle that test for bad coding practices, and FindBugs.


Testing strategy
-----------------------

one book to talk about more technical details on testing: Agile Testing, by Lisa Crispin and Janet Gregory.

as mentioned before, there are 3 types of tests: unit tests, component tests and user acceptance tests.  
these tests do not just test the functional aspects of the system, 
they also (have to) test other aspects like capacity, security and other nonfunctional requirements.

to run automated (functional) acceptance tests written in a behavior-driven development (BDD) style, 
there are a few tools: Cucumber, JBehave, Condordion and Twist.  
usually they follow a "given-when-then" model for tests.  
There is a cucumber plugin for Jenkins.

how the question is: how to write an automated acceptance test? 
(i need other materials to pick this skill up. in fact, the chapter 8 of this book will elaborate more on automated acceptance testing.)

user acceptance tests are slightly higher level.  
the lowest level is unit tests.  however, they may miss the bugs resultant from the interactions of different components.   
then it should be component tests, which are to test larger clusters of functionality. this may involve database, filesystem, setup..  
there also another one, called deployment tests, which are used for check if the application is correctly installed, configured, able to contact any services it requires and that it is responding.  


thinking
--------------------

can i apply continuous delivery to my personal life?  
what does this even mean?  

i should have some goals in life.  
whatever i do, i should contribute to these goals.  
i should see the feedbacks of an action as early as possbile; and if an action leads to no contribution, then i should stop it.  

how can i build a pipeline from actions to goals?  
is it a mental pipeline or a physical pipeline?  
one way i can think of is that i can have some programs running somewhere, and if i take an action, i should record it down in the system.
then the system will immediately give me feedbacks!  
this sounds like a good idea!  
for obvious ones i should know the answer easily.  
for complicated actions, if possible the system should do some machine learning to extract basic actions/features from it and then go through the system to decide whether it is good or not.
