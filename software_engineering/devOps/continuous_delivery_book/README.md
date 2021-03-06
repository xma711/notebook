Objective
------------------

Every change that is made to an application's configuration, source code, environment, or data,
triggers the creation of a new instance of the deployment pipeline.

A deployment pipeline is an automated implementation of your application's build, deploy, test and release process.

The aims:  
	1. it makes every part of the process of building, deploying, testing and releasing software visible to everybody involved, aiding collaboration.  
	2. it improves feedback so that problems are identified, and so resolved, as early in the process as possible.  
	3. it enables teams to deploy and release any version of their software to any environment at will through a fully automated process. 


Configuration
--------------------

We should treat configuration files like source codes.  
They have to be version-controlled of course.  
The whole environment (production or testing) should be able to be produced from the scripts and configurations file from the repository alone.  
The configuration files for the app have to be maintained in this way too.

More over, configuration files should be tested too.

One way to make sure the production or testing environment can be produced from configuration files could be to use docker.  
By writing the Dockerfile for different env, it is easy to produce the OS.  
However, for network-wide environment, we may still need to use some scripts to auto deploy the docker images to multiple machines.


Continuous integration
-----------------------------

Every commit should trigger the the automated testing of the whole repository.  
Unit testing is definitely one of the automated tests.  
What else?  
The other 2 tests we need are component tests and acceptance tests.  
Component tests test the behavior of several components of your application. (how to decide which group of components to be tested together is another question).  
Acceptance tests test that the application meets the acceptance criteria decided by the business, 
including both the functionality provided by the application and its characteristics such as capacity, availability, security and so on.  
Acceptance tests are best written in such a way that they run against the whole application in a production-like environment.

CI tools: Jenkins (previously known as Hudson), and CruiseControl.

There are some tools to check coding style/practices: Simian (identify duplication), JDepend for Java, CheckStyle that test for bad coding practices, and FindBugs.


Testing strategy
-----------------------

One book to talk about more technical details on testing: Agile Testing, by Lisa Crispin and Janet Gregory.

As mentioned before, there are 3 types of tests: unit tests, component tests and user acceptance tests.  
These tests do not just test the functional aspects of the system, 
they also (have to) test other aspects like capacity, security and other nonfunctional requirements.

To run automated (functional) acceptance tests written in a behavior-driven development (BDD) style, 
there are a few tools: Cucumber, JBehave, Condordion and Twist.  
Usually they follow a "given-when-then" model for tests.  
There is a cucumber plugin for Jenkins.

User acceptance tests are slightly higher level.  
The lowest level is unit tests.  however, they may miss the bugs resultant from the interactions of different components.   
Then it should be component tests, which are to test larger clusters of functionality. this may involve database, filesystem, setup..  
There also another one, called deployment tests, which are used for check if the application is correctly installed, configured, able to contact any services it requires and that it is responding.  


