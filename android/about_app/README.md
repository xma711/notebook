Android apps
--------------------

Things about Android apps!!!


Activity
----------------------

Reference: http://www.tutorialspoint.com/android/android_acitivities.htm  
and http://stackoverflow.com/questions/8180180/android-can-somebody-please-explain-what-is-activity-context-intent-in-android

activity represents the presentation layer of an android application,
e.g. a screen which the user sees.
An android application can have several activities and it can be switched between them during runtime of the application.

A simpler explanation is that "an activity is a page in your application".

It uses similar way as the main() function in c++ or c or java..  
An activity starts with a call on onCreate() callback method.  
Then there are onStart(), onResume(), onPause(), onStop(), onDestroy() callback methods
that define the life cycle of an activity.
(this sounds rather like the entire app life cycle...)


ContentProvider
-----------------------

ContentProvider provides data to applications

Context is an abstract class that contains a lot of methods needed by its subclasses: mostly activity and service.

Intents
-----------------------

Intents are asynchronous messages which allow the application to request functionality from other services or activities.  
An application can call directly a service or activity (explicit intent)  
or ask the android system for registered services and applications for an intent (implicit intents).

For example, the application could ask via an intent for a contact application.  
Applications register themselves to an intent via an IntentFilter.  
Intents are a powerful concepts as they allow creation of loosely coupled applications.

Intent is a link between two pages.
Bundles all the details necessary to do something, 
send a message to the system,
or go to another page of an application..

