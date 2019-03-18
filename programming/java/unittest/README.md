Unit testing in Java
-----------------------------
Can use JUnit.

Check the content between tip 48 and 49 in book "the pragmatic programmer".


Install junit package
-----------------------------------------
Follow this link: http://www.tutorialspoint.com/junit/junit_environment_setup.htm

please pay attention to the junit*.jar filename, because using the wrong name in the CLASSPATH 
will cause javac not able to find the junit package. 
(cannot just copy and paste from the link.)

Anyway, the steps to install junit are:
```
Step 1 - verify Java installation in your machine. Now open console and execute the following java command. ...
Step 2: Set JAVA environment. export JAVA_HOME=
Step 3: Download Junit archive. ...
Step 4: Set JUnit environment. ... export JUNIT
Step 5: Set CLASSPATH variable. ...
Step 6: Test JUnit Setup. ...
Step 7: Verify the Result.

# step 2:
export JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64
export PATH=$PATH:$JAVA_HOME/bin/

# step 4 and 4:
export JUNIT_HOME=/usr/local/JUNIT
export CLASSPATH=$CLASSPATH:$JUNIT_HOME/junit-4.10.jar
```
