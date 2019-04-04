About annotation
-----------------------

The syntax is @Something, usually before a method.  
It looks like python decorator, but they are very different.

In python, a decorator takes a functon and returns another function.

In java, it is, as its name implies, something to provide extra information..

One reference is: https://docs.oracle.com/javase/tutorial/java/annotations/

ultimately, annotations is a form of metadata.
It provides data about a program that is not part of the program itself.
It has no direct effect on the operation of the code they annotate.

The uses of annotations:  
1. information for the compiler  
2. compile-time and deployment-time processing  
3. runtime processing

E.g.  
@Override
void aMethod() { ... }

about the "@Override" thing: https://stackoverflow.com/questions/94361/when-do-you-use-javas-override-annotation-and-why

the link above provides a good example (on "Override") to explain why annotation is useful.  
When you think you are overriding a method, write the @Override annotation.
Then, if you make a spelling mistake on the method name, the compiler will warn that you are not overriding any method from parent.  
Also, it makes the code easier to be understood..
