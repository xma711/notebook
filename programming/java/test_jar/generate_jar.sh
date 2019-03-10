#!/bin/bash

# compile java file
javac HelloWorld.java

# create .jar file from output of last line and the manifest file
jar cfm helloWorld.jar manifest.mf HelloWorld.class

# execute it
java -jar helloWorld.jar
