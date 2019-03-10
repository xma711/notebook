android apps
--------------------

things about Android apps!!!


Activity
----------------------

reference: http://www.tutorialspoint.com/android/android_acitivities.htm  
and http://stackoverflow.com/questions/8180180/android-can-somebody-please-explain-what-is-activity-context-intent-in-android

activity represents the presentation layer of an android application,
e.g. a screen which the user sees.
an android application can have several activities and it can be switched between them during runtime of the application.

a simpler explanation is that "an activity is a page in your application".

it uses similar way as the main() function in c++ or c or java..  
an activity starts with a call on onCreate() callback method.  
then there are onStart(), onResume(), onPause(), onStop(), onDestroy() callback methods
that define the life cycle of an activity.
(this sounds rather like the entire app life cycle...)


ContentProvider
-----------------------

contentProvider provides data to applications

Context is an abstract class that contains a lot of methods needed by its subclasses: mostly activity and service.

Intents
-----------------------

intents are asynchronous messages which allow the application to request functionality from other services or activities.  
an application can call directly a service or activity (explicit intent)  
or ask the android system for registered services and applications for an intent (implicit intents).

for example, the application could ask via an intent for a contact application.  
applications register themselves to an intent via an IntentFilter.  
Intents are a powerful concepts as they allow creation of loosely coupled applications.

Intent is a link between two pages.
bundles all the details necessary to do something, 
send a message to the system,
or go to another page of an application..

