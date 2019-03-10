### use makefile to perform unittests in all the subdriectories.
### It is uses find to find out all the test program files, and run each of them using nodeunit 
### Any *.js file with a test in the name will be found by 'find' in this case. -> this should be defined by myself

### strangely, cannot use test as the target name, probably it is is reserved word in Makefile

unittest:
	/usr/bin/nodeunit $(shell find . -name test*.js)

